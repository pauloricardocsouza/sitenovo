#!/usr/bin/env python3
"""
build-blog.py · R2 Soluções Empresariais
Gera HTML de blog posts a partir de arquivos Markdown.

Uso:
  python3 build-blog.py NOVO-POST.md
  python3 build-blog.py --all       # reconstrói todos os posts em blog/posts/

Estrutura esperada do arquivo .md (com front matter YAML):

---
slug: meu-post
title: Meu título com <em>destaque</em>
deck: Subtítulo do post em uma frase.
author: Rogel Carneiro
date: 2026-05-20
read: 6 min
category: Tributário
related:
  - slug: outro-post-1
    category: Tributário
    title: Outro título
  - slug: outro-post-2
    category: Empresa Familiar
    title: Mais um título
  - slug: outro-post-3
    category: Gestão Financeira
    title: Terceiro título
---

# Subtítulo H2 do post

Parágrafo 1.

Parágrafo 2 com **negrito** e *itálico*.

## Outro H2

- item de lista
- outro item

> bloco de citação
"""

import os
import sys
import re
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parent
POSTS_MD_DIR = ROOT / "blog" / "posts-md"
POSTS_HTML_DIR = ROOT / "blog" / "posts"

AUTHOR_BIOS = {
    "Rogel Carneiro": "Sócio-fundador da R2 Soluções Empresariais. Atuação em tributário, governança societária e Reforma Tributária.",
    "Ricardo Souza": "Sócio-fundador da R2 Soluções Empresariais. Atuação em BI, gestão de dados, profissionalização de operações e empresas familiares.",
}

MONTHS_PT = {
    "01": "janeiro", "02": "fevereiro", "03": "março", "04": "abril",
    "05": "maio", "06": "junho", "07": "julho", "08": "agosto",
    "09": "setembro", "10": "outubro", "11": "novembro", "12": "dezembro",
}


def parse_front_matter(text):
    """Parser simples de front matter YAML. Suporta apenas o subset que usamos."""
    if not text.startswith("---"):
        raise ValueError("Arquivo precisa começar com '---' (front matter YAML)")
    end = text.find("---", 3)
    if end < 0:
        raise ValueError("Front matter não fechou com '---'")
    fm_text = text[3:end].strip()
    body = text[end+3:].strip()

    fm = {}
    related = []
    current_rel = None
    in_related = False

    for line in fm_text.split("\n"):
        if not line.strip():
            continue
        if line.startswith("related:"):
            in_related = True
            continue
        if in_related:
            if line.startswith("  - "):
                if current_rel:
                    related.append(current_rel)
                current_rel = {}
                rest = line[4:].strip()
                if ":" in rest:
                    k, v = rest.split(":", 1)
                    current_rel[k.strip()] = v.strip()
            elif line.startswith("    "):
                k, v = line.strip().split(":", 1)
                if current_rel is None:
                    current_rel = {}
                current_rel[k.strip()] = v.strip()
            else:
                in_related = False
                if current_rel:
                    related.append(current_rel)
                    current_rel = None
        if not in_related and ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()

    if current_rel:
        related.append(current_rel)
    if related:
        fm["related"] = related

    return fm, body


def md_to_html(md):
    """Conversão Markdown -> HTML em escopo mínimo, suficiente para R2 posts."""
    lines = md.split("\n")
    out = []
    in_p = []
    in_list = None  # 'ul' or 'ol'
    in_quote = False
    in_table = False
    table_rows = []

    def flush_p():
        nonlocal in_p
        if in_p:
            paragraph = " ".join(in_p).strip()
            paragraph = inline_md(paragraph)
            out.append(f"<p>{paragraph}</p>")
            in_p = []

    def close_list():
        nonlocal in_list
        if in_list:
            out.append(f"</{in_list}>")
            in_list = None

    def close_quote():
        nonlocal in_quote
        if in_quote:
            out.append("</blockquote>")
            in_quote = False

    def close_table():
        nonlocal in_table, table_rows
        if in_table and table_rows:
            out.append('<table>')
            out.append('<thead><tr>')
            for cell in table_rows[0]:
                out.append(f'<th>{inline_md(cell)}</th>')
            out.append('</tr></thead><tbody>')
            for row in table_rows[2:]:  # pular linha separadora
                out.append('<tr>')
                for cell in row:
                    out.append(f'<td>{inline_md(cell)}</td>')
                out.append('</tr>')
            out.append('</tbody></table>')
            table_rows = []
            in_table = False

    def inline_md(s):
        # **negrito**, *italico*, [link](url), `code`
        s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"(?<!\*)\*([^\*]+)\*(?!\*)", r"<em>\1</em>", s)
        s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
        s = re.sub(r"\[(.+?)\]\((.+?)\)", r'<a href="\2">\1</a>', s)
        return s

    for line in lines:
        stripped = line.strip()

        # Tabela
        if stripped.startswith("|") and stripped.endswith("|"):
            flush_p(); close_list(); close_quote()
            in_table = True
            cells = [c.strip() for c in stripped.strip("|").split("|")]
            table_rows.append(cells)
            continue
        elif in_table:
            close_table()

        # H2 / H3
        m = re.match(r"^(#{2,3})\s+(.+)$", stripped)
        if m:
            flush_p(); close_list(); close_quote(); close_table()
            level = len(m.group(1))
            text = inline_md(m.group(2))
            out.append(f"<h{level}>{text}</h{level}>")
            continue

        # Listas
        if stripped.startswith("- "):
            flush_p(); close_quote()
            if in_list != "ul":
                close_list()
                out.append("<ul>")
                in_list = "ul"
            out.append(f"<li>{inline_md(stripped[2:])}</li>")
            continue
        if re.match(r"^\d+\.\s+", stripped):
            flush_p(); close_quote()
            if in_list != "ol":
                close_list()
                out.append("<ol>")
                in_list = "ol"
            text = re.sub(r"^\d+\.\s+", "", stripped)
            out.append(f"<li>{inline_md(text)}</li>")
            continue

        # Quote
        if stripped.startswith("> "):
            flush_p(); close_list()
            if not in_quote:
                out.append("<blockquote>")
                in_quote = True
            out.append(inline_md(stripped[2:]))
            continue

        # Linha vazia
        if not stripped:
            flush_p(); close_list(); close_quote(); close_table()
            continue

        # Parágrafo
        in_p.append(stripped)

    flush_p()
    close_list()
    close_quote()
    close_table()

    return "\n".join(out)


def date_pt(iso):
    """2026-05-20 -> 20 de maio de 2026"""
    parts = iso.split("-")
    if len(parts) != 3:
        return iso
    y, m, d = parts
    return f"{int(d)} de {MONTHS_PT.get(m, m)} de {y}"


def render_post(fm, body_html):
    """Renderiza o post completo usando build_post() do blog_helper.
    Quando o script roda standalone (deploy), o build_helper pode não existir.
    Por isso temos uma versão inline minimalista também.
    """
    try:
        sys.path.insert(0, str(ROOT))
        from blog_helper import build_post
        related = fm.get("related", [])
        return build_post(
            slug=fm["slug"],
            title=fm["title"],
            deck=fm["deck"],
            author=fm["author"],
            author_bio=AUTHOR_BIOS.get(fm["author"], ""),
            date_iso=fm["date"],
            date_pt=date_pt(fm["date"]),
            read_time=fm.get("read", "5 min"),
            category_slug=fm.get("category_slug", fm["category"].lower().replace(" ", "-")),
            category_label=fm["category"],
            body_html=body_html,
            related=related
        )
    except ImportError:
        raise SystemExit("Erro: blog_helper.py não encontrado. Coloque na mesma pasta de build-blog.py.")


def build_one(md_path):
    text = Path(md_path).read_text(encoding="utf-8")
    fm, body_md = parse_front_matter(text)
    body_html = md_to_html(body_md)
    html = render_post(fm, body_html)
    out = POSTS_HTML_DIR / f"{fm['slug']}.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    return out


def build_all():
    if not POSTS_MD_DIR.exists():
        print(f"Pasta {POSTS_MD_DIR} não existe. Crie e coloque os .md dentro.")
        return
    found = list(POSTS_MD_DIR.glob("*.md"))
    if not found:
        print(f"Nenhum .md encontrado em {POSTS_MD_DIR}")
        return
    for md in found:
        try:
            out = build_one(md)
            print(f"  {out.relative_to(ROOT)}")
        except Exception as e:
            print(f"  ERRO em {md.name}: {e}")
    print(f"\nTotal: {len(found)} post(s) gerado(s).")


def main():
    parser = argparse.ArgumentParser(description="Gera HTML de blog posts a partir de Markdown.")
    parser.add_argument("md_file", nargs="?", help="Arquivo .md para converter")
    parser.add_argument("--all", action="store_true", help="Reconstrói todos os posts em blog/posts-md/")
    args = parser.parse_args()

    if args.all:
        build_all()
    elif args.md_file:
        out = build_one(args.md_file)
        print(f"OK: {out}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
