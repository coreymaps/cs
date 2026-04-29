#!/usr/bin/env python3
"""Convert /content/project/<slug>/index.md to /projects/<slug>.html.

Reads frontmatter (title, summary, external_link), markdown body, and emits a
static page that matches the rest of the site's typography and structure.
"""
import os
import re
from pathlib import Path
import markdown

ROOT = Path("/Users/coreyscher/projects/cs")
SRC = ROOT / "content" / "project"
OUT = ROOT / "projects"
OUT.mkdir(parents=True, exist_ok=True)

# slug -> (title, summary, external_link, has_image_ext)
ORDER = [
    "gaza-2024", "lebanon_damage", "la_fires", "ukraine",
    "graves", "china_floods", "fires_papua", "herbicide",
    "kite-fires", "tba_subsidence", "himat-glacier-melt", "wax-lake",
    "power-law-scaling",
    "agu-2024", "agu_2023", "arset_humanitarian",
]


def parse_frontmatter(text):
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    fm_raw, body = parts[1], parts[2]
    fm = {}
    for line in fm_raw.splitlines():
        m = re.match(r'^(\w+):\s*"?([^"\n]*)"?\s*$', line)
        if m:
            fm[m.group(1)] = m.group(2).strip().strip('"')
    return fm, body.lstrip("\n")


def find_image(slug):
    for ext in ("jpg", "png", "jpeg"):
        if (ROOT / "assets" / "projects" / f"{slug}.{ext}").exists():
            return f"/assets/projects/{slug}.{ext}"
    return None


PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} — Corey Scher</title>
  <link rel="stylesheet" href="/assets/style.css">
</head>
<body>
  <main class="article project-page">
    <p class="back"><a href="/projects.html">← Projects</a></p>
    {hero}
    <h1 class="project-title">{title}</h1>
    {summary_html}
    <div class="project-body">
{body_html}
    </div>
  </main>
</body>
</html>
"""


md = markdown.Markdown(extensions=["tables", "fenced_code", "md_in_html"])


def merge_title_link_columns(text):
    """In any markdown pipe-table whose header has both Title and Link columns,
    drop the Link column and turn each Title cell into [title](link)."""
    out_lines = []
    i = 0
    lines = text.splitlines()
    while i < len(lines):
        line = lines[i]
        # detect a header row + separator row of a markdown table
        if (line.strip().startswith("|") and i + 1 < len(lines)
                and re.match(r'^\s*\|[\s:|-]+\|\s*$', lines[i+1])):
            header_cells = [c.strip() for c in line.strip().strip("|").split("|")]
            lower = [h.lower() for h in header_cells]
            if "title" in lower and "link" in lower:
                t_idx = lower.index("title")
                l_idx = lower.index("link")
                # rewrite header (drop link col)
                new_header = [c for j, c in enumerate(header_cells) if j != l_idx]
                out_lines.append("| " + " | ".join(new_header) + " |")
                # rewrite separator
                sep_cells = [s.strip() for s in lines[i+1].strip().strip("|").split("|")]
                new_sep = [c for j, c in enumerate(sep_cells) if j != l_idx]
                out_lines.append("|" + "|".join(new_sep) + "|")
                # rewrite body rows
                j = i + 2
                while j < len(lines) and lines[j].strip().startswith("|"):
                    cells = [c.strip() for c in lines[j].strip().strip("|").split("|")]
                    if len(cells) > max(t_idx, l_idx):
                        title_cell = cells[t_idx]
                        link_cell = cells[l_idx]
                        if link_cell.startswith("http"):
                            cells[t_idx] = f"[{title_cell}]({link_cell})"
                        new_cells = [c for k, c in enumerate(cells) if k != l_idx]
                        out_lines.append("| " + " | ".join(new_cells) + " |")
                    else:
                        out_lines.append(lines[j])
                    j += 1
                i = j
                continue
        out_lines.append(line)
        i += 1
    return "\n".join(out_lines)


for slug in ORDER:
    src_file = SRC / slug / "index.md"
    if not src_file.exists():
        print(f"missing: {slug}")
        continue
    raw = src_file.read_text()
    fm, body = parse_frontmatter(raw)
    title = fm.get("title", slug).strip('"')
    summary = fm.get("summary", "").strip('"')
    external = fm.get("external_link", "").strip()

    img = find_image(slug)
    hero = f'<figure class="project-hero"><img src="{img}" alt=""></figure>' if img else ""
    summary_html = f'<p class="project-summary">{summary}</p>' if summary else ""

    body = merge_title_link_columns(body)
    md.reset()
    body_html = md.convert(body)

    html = PAGE.format(
        title=title,
        hero=hero,
        summary_html=summary_html,
        body_html=body_html,
    )
    (OUT / f"{slug}.html").write_text(html)
    print(f"wrote: projects/{slug}.html  (img={'yes' if img else 'no'}, body_chars={len(body_html)})")

print("\nDone.")
