#!/usr/bin/env python3
"""kb-notes 知识库校验与索引生成工具（仅用标准库）。

用法：
    python3 tools/kb.py check          # 校验全部笔记 + 索引是否最新（CI 用）
    python3 tools/kb.py index          # 重新生成 README.md 索引区块

校验项见 README「笔记规范」一节。frontmatter 只支持仓库实际使用的 YAML 子集
（标量 + 短横线列表），遇到未知写法直接报错，避免规范悄悄漂移。
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

ROOT = Path(__file__).resolve().parent.parent
NOTES_DIR = ROOT / "notes"
README = ROOT / "README.md"

BEGIN_MARK = "<!-- BEGIN INDEX: 由 tools/kb.py 生成，勿手改 -->"
END_MARK = "<!-- END INDEX -->"

# frontmatter 字段顺序即为强制顺序
SCALAR_FIELDS = ("version", "id", "title", "source", "summary", "created", "updated", "favorite")
LIST_FIELDS = ("tags", "related")
FIELD_ORDER = ("version", "id", "title", "tags", "source", "summary", "created", "updated", "favorite", "related")

TS_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$")
ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_RE = re.compile(r"note://([A-Za-z0-9\-]+)")


@dataclass
class Note:
    path: Path
    slug: str
    fm: Dict[str, object] = field(default_factory=dict)
    order: List[str] = field(default_factory=list)
    body: str = ""

    @property
    def rel(self) -> str:
        return str(self.path.relative_to(ROOT))

    @property
    def title(self) -> str:
        return str(self.fm.get("title") or self.slug)

    @property
    def summary(self) -> str:
        return str(self.fm.get("summary") or "")

    @property
    def tags(self) -> List[str]:
        return list(self.fm.get("tags") or [])  # type: ignore[arg-type]

    @property
    def related(self) -> List[str]:
        return list(self.fm.get("related") or [])  # type: ignore[arg-type]


@dataclass
class Problem:
    level: str  # "error" | "warn"
    where: str
    message: str


def parse_frontmatter(text: str, where: str) -> Tuple[Dict[str, object], List[str], str, List[Problem]]:
    """解析受限 YAML frontmatter，返回 (字段, 出现顺序, 正文, 问题)。"""
    problems: List[Problem] = []
    if not text.startswith("---\n"):
        return {}, [], text, [Problem("error", where, "缺少 YAML frontmatter（文件未以 `---` 开头）")]
    end = text.find("\n---\n", 3)
    if end == -1:
        return {}, [], text, [Problem("error", where, "frontmatter 没有结束分隔符 `---`")]

    block = text[4:end]
    body = text[end + 5 :]
    fm: Dict[str, object] = {}
    order: List[str] = []
    current_list: Optional[str] = None

    for lineno, line in enumerate(block.splitlines(), start=2):
        if not line.strip():
            current_list = None
            continue
        item = re.match(r"^ {2}-\s+(.*)$", line)
        if item:
            if current_list is None:
                problems.append(Problem("error", f"{where}:{lineno}", "列表项没有归属的字段"))
                continue
            fm[current_list].append(item.group(1).strip())  # type: ignore[union-attr]
            continue
        kv = re.match(r"^([a-z_]+):(?:[ \t]+(.*))?$", line)
        if not kv:
            problems.append(Problem("error", f"{where}:{lineno}", f"无法解析的 frontmatter 行：{line!r}"))
            current_list = None
            continue
        key, value = kv.group(1), (kv.group(2) or "").strip()
        if key in fm:
            problems.append(Problem("error", f"{where}:{lineno}", f"字段 `{key}` 重复"))
        order.append(key)
        if value == "":
            fm[key] = []
            current_list = key
        else:
            fm[key] = value
            current_list = None
    return fm, order, body, problems


def load_notes() -> Tuple[List[Note], List[Problem]]:
    notes: List[Note] = []
    problems: List[Problem] = []
    for path in sorted(NOTES_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        where = str(path.relative_to(ROOT))
        fm, order, body, errs = parse_frontmatter(text, where)
        problems.extend(errs)
        notes.append(Note(path=path, slug=path.stem, fm=fm, order=order, body=body))
    return notes, problems


def check_fields(note: Note) -> List[Problem]:
    problems: List[Problem] = []
    if not note.fm:
        return problems  # 解析阶段已报错

    present = [k for k in note.order]
    missing = [k for k in FIELD_ORDER if k not in note.fm]
    unknown = [k for k in present if k not in FIELD_ORDER]
    if missing:
        problems.append(Problem("error", note.rel, f"frontmatter 缺字段：{', '.join(missing)}"))
    if unknown:
        problems.append(Problem("error", note.rel, f"frontmatter 含未知字段：{', '.join(unknown)}"))
    if not missing and not unknown and present != list(FIELD_ORDER):
        problems.append(Problem("error", note.rel, f"frontmatter 字段顺序应为：{', '.join(FIELD_ORDER)}"))

    for key in SCALAR_FIELDS:
        if isinstance(note.fm.get(key), list):
            problems.append(Problem("error", note.rel, f"`{key}` 应为标量，实际是列表"))
    for key in LIST_FIELDS:
        if key in note.fm and not isinstance(note.fm[key], list):
            problems.append(Problem("error", note.rel, f"`{key}` 应为列表"))

    version = note.fm.get("version")
    if isinstance(version, str) and not version.isdigit():
        problems.append(Problem("error", note.rel, f"`version` 应为整数，实际是 {version!r}"))
    if note.fm.get("favorite") not in (None, "true", "false"):
        problems.append(Problem("error", note.rel, f"`favorite` 应为 true/false，实际是 {note.fm['favorite']!r}"))

    note_id = note.fm.get("id")
    if isinstance(note_id, str):
        if note_id != note.slug:
            problems.append(Problem("error", note.rel, f"`id` ({note_id}) 与文件名 ({note.slug}) 不一致"))
        if not ID_RE.match(note_id):
            problems.append(Problem("error", note.rel, f"`id` 不符合 kebab-case：{note_id}"))

    for key in ("title", "summary", "source"):
        value = note.fm.get(key)
        if isinstance(value, str) and not value.strip():
            problems.append(Problem("error", note.rel, f"`{key}` 不能为空"))

    created, updated = note.fm.get("created"), note.fm.get("updated")
    for key, value in (("created", created), ("updated", updated)):
        if isinstance(value, str) and not TS_RE.match(value):
            problems.append(Problem("error", note.rel, f"`{key}` 应为 ISO-8601 毫秒 UTC（YYYY-MM-DDThh:mm:ss.sssZ），实际是 {value!r}"))
    if isinstance(created, str) and isinstance(updated, str) and TS_RE.match(created) and TS_RE.match(updated):
        if updated < created:
            problems.append(Problem("error", note.rel, f"`updated` ({updated}) 早于 `created` ({created})"))

    tags = note.fm.get("tags")
    if isinstance(tags, list):
        if not tags:
            problems.append(Problem("error", note.rel, "`tags` 至少要有 1 个标签"))
        dupes = sorted({t for t in tags if tags.count(t) > 1})
        if dupes:
            problems.append(Problem("error", note.rel, f"`tags` 重复：{', '.join(dupes)}"))
    return problems


def check_graph(notes: List[Note]) -> List[Problem]:
    problems: List[Problem] = []
    by_slug = {n.slug: n for n in notes}
    ids: Dict[str, List[str]] = {}
    for note in notes:
        note_id = note.fm.get("id")
        if isinstance(note_id, str):
            ids.setdefault(note_id, []).append(note.rel)
    for note_id, owners in sorted(ids.items()):
        if len(owners) > 1:
            problems.append(Problem("error", owners[0], f"`id` {note_id} 被多个文件占用：{', '.join(owners)}"))

    for note in notes:
        related = note.related
        dupes = sorted({r for r in related if related.count(r) > 1})
        if dupes:
            problems.append(Problem("error", note.rel, f"`related` 重复：{', '.join(dupes)}"))
        for target in related:
            if target == note.slug:
                problems.append(Problem("error", note.rel, "`related` 不能引用自身"))
                continue
            peer = by_slug.get(target)
            if peer is None:
                problems.append(Problem("error", note.rel, f"`related` 指向不存在的笔记：{target}"))
            elif note.slug not in peer.related:
                problems.append(Problem("error", note.rel, f"`related` 不对称：{note.slug} → {target}，但 {target} 未回链"))

        for target in sorted(set(LINK_RE.findall(note.body))):
            if target not in by_slug:
                problems.append(Problem("error", note.rel, f"正文 note:// 链接断链：{target}"))

        if not related and not LINK_RE.findall(note.body):
            problems.append(Problem("warn", note.rel, "孤立笔记：既无 related 也无正文 note:// 链接"))
    return problems


MIN_SUBSTANCE = 150
MAX_SENTENCE_REUSE = 2
MIN_SENTENCE_LEN = 20


def substance_lines(body: str) -> List[str]:
    """正文里真正承载知识的行：剔除标题、引用摘要、表格分隔与纯导航链接行。"""
    kept: List[str] = []
    for raw in body.splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or line.startswith(">") or line.startswith("|"):
            continue
        if re.match(r"^[-*]?\s*\[[^\]]+\]\(note://[A-Za-z0-9\-]+\)[：:]?\s*$", line):
            continue
        kept.append(line)
    return kept


def sentences(body: str) -> Set[str]:
    """按中文句读切句，去掉 Markdown 链接壳，只保留够长的句子。"""
    out: Set[str] = set()
    for line in substance_lines(body):
        plain = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", line).lstrip("-*0123456789. ")
        for piece in re.split(r"[。；！？]", plain):
            piece = piece.strip()
            if len(piece) >= MIN_SENTENCE_LEN:
                out.add(piece)
    return out


def check_substance(notes: List[Note]) -> List[Problem]:
    """堵住模板灌水复发：正文过薄，以及同一句话被复制到多篇。"""
    problems: List[Problem] = []
    for note in notes:
        size = sum(len(re.sub(r"\s", "", line)) for line in substance_lines(note.body))
        if size < MIN_SUBSTANCE:
            problems.append(Problem("error", note.rel, f"正文实质内容只有 {size} 字（不含标题/摘要/纯链接行），低于下限 {MIN_SUBSTANCE}"))

    owners: Dict[str, List[str]] = {}
    for note in notes:
        for sentence in sentences(note.body):
            owners.setdefault(sentence, []).append(note.rel)
    for sentence, files in sorted(owners.items()):
        if len(files) > MAX_SENTENCE_REUSE:
            preview = sentence if len(sentence) <= 40 else sentence[:40] + "…"
            problems.append(Problem("error", sorted(files)[0], f"样板句被 {len(files)} 篇复用：「{preview}」（{', '.join(sorted(files))}）"))
    return problems


def build_tree(notes: List[Note]) -> List[Tuple[str, List[Tuple[int, Note]]]]:
    """按 related 图切分连通分量，每个分量从根节点 BFS 展开成树。"""
    by_slug = {n.slug: n for n in notes}
    unvisited: Set[str] = set(by_slug)
    components: List[List[str]] = []
    while unvisited:
        seed = min(unvisited)
        comp, queue = [], [seed]
        unvisited.discard(seed)
        while queue:
            cur = queue.pop(0)
            comp.append(cur)
            for peer in sorted(by_slug[cur].related):
                if peer in unvisited:
                    unvisited.discard(peer)
                    queue.append(peer)
        components.append(sorted(comp))

    def root_of(comp: List[str]) -> str:
        # 根 = 作为前缀覆盖同分量其他 id 最多的笔记；并列取更短、字典序更小的
        return min(comp, key=lambda s: (-sum(1 for o in comp if o != s and o.startswith(s + "-")), len(s), s))

    trees: List[Tuple[str, List[Tuple[int, Note]]]] = []
    for comp in components:
        root = root_of(comp)
        # BFS 定层：每个节点挂在最先发现它的节点下，深度即到根的最短距离
        children: Dict[str, List[str]] = {slug: [] for slug in comp}
        seen = {root}
        queue = [root]
        while queue:
            cur = queue.pop(0)
            for peer in sorted(by_slug[cur].related):
                if peer not in seen:
                    seen.add(peer)
                    children[cur].append(peer)
                    queue.append(peer)
        for slug in comp:  # 分量内理论上不会漏，兜底防御
            if slug not in seen:
                seen.add(slug)
                children[root].append(slug)

        rows: List[Tuple[int, Note]] = []

        def walk(slug: str, depth: int) -> None:
            rows.append((depth, by_slug[slug]))
            for child in children[slug]:
                walk(child, depth + 1)

        walk(root, 0)
        trees.append((root, rows))
    trees.sort(key=lambda t: (-len(t[1]), t[0]))
    return trees


def render_index(notes: List[Note]) -> str:
    lines: List[str] = [BEGIN_MARK, ""]
    lines.append(f"共 {len(notes)} 篇笔记。")
    lines.append("")
    lines.append("## 知识树")
    lines.append("")
    for root, rows in build_tree(notes):
        head = rows[0][1]
        lines.append(f"### {head.title}")
        lines.append("")
        for depth, note in rows:
            indent = "  " * depth
            lines.append(f"{indent}- [{note.title}](notes/{note.slug}.md) — {note.summary}")
        lines.append("")
    lines.append("## 全部笔记")
    lines.append("")
    lines.append("| id | 标题 | 标签 |")
    lines.append("| --- | --- | --- |")
    for note in sorted(notes, key=lambda n: n.slug):
        tags = " / ".join(note.tags)
        lines.append(f"| [{note.slug}](notes/{note.slug}.md) | {note.title} | {tags} |")
    lines.append("")
    lines.append(END_MARK)
    return "\n".join(lines)


def splice_readme(index_md: str) -> str:
    text = README.read_text(encoding="utf-8") if README.exists() else ""
    start, end = text.find(BEGIN_MARK), text.find(END_MARK)
    if start == -1 or end == -1 or end < start:
        raise SystemExit(f"README.md 缺少索引标记 {BEGIN_MARK} / {END_MARK}，无法生成")
    return text[:start] + index_md + text[end + len(END_MARK) :]


def cmd_index(_: argparse.Namespace) -> int:
    notes, problems = load_notes()
    fatal = [p for p in problems if p.level == "error"]
    if fatal:
        for p in fatal:
            print(f"error  {p.where}: {p.message}", file=sys.stderr)
        print("frontmatter 解析失败，先修好再生成索引。", file=sys.stderr)
        return 1
    README.write_text(splice_readme(render_index(notes)), encoding="utf-8")
    print(f"README.md 索引已更新（{len(notes)} 篇）。")
    return 0


def cmd_check(_: argparse.Namespace) -> int:
    notes, problems = load_notes()
    if not notes:
        print(f"error  {NOTES_DIR}: 没有找到任何笔记", file=sys.stderr)
        return 1
    for note in notes:
        problems.extend(check_fields(note))
    problems.extend(check_graph(notes))
    problems.extend(check_substance(notes))

    if not [p for p in problems if p.level == "error"]:
        expected = splice_readme(render_index(notes))
        actual = README.read_text(encoding="utf-8") if README.exists() else ""
        if expected != actual:
            problems.append(Problem("error", "README.md", "索引已过期，运行 `python3 tools/kb.py index` 重新生成"))

    errors = [p for p in problems if p.level == "error"]
    warns = [p for p in problems if p.level == "warn"]
    for p in errors + warns:
        stream = sys.stderr if p.level == "error" else sys.stdout
        print(f"{p.level:<5}  {p.where}: {p.message}", file=stream)
    print(f"检查 {len(notes)} 篇笔记：{len(errors)} 个错误，{len(warns)} 个警告。")
    return 1 if errors else 0


def main() -> int:
    parser = argparse.ArgumentParser(description="kb-notes 校验与索引工具")
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("check", help="校验笔记规范、链接与索引新鲜度").set_defaults(func=cmd_check)
    sub.add_parser("index", help="重新生成 README.md 索引区块").set_defaults(func=cmd_index)
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
