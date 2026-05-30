#!/usr/bin/env python3
"""
gen-sitemap.py · R2 Soluções Empresariais
Gera sitemap.xml automaticamente a partir dos arquivos HTML do site.

Uso:
  python3 gen-sitemap.py

Roda na raiz do projeto. Procura todos os .html exceto os filtrados.
"""

import os
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BASE_URL = "https://www.solucoesr2.com.br"

# Páginas excluídas (técnicas/lp/sem valor de SEO)
EXCLUDE = {
    "404.html",
    "obrigado.html",
}

# Prioridades por padrão de URL
PRIORITIES = [
    (lambda u: u == "/", "1.0", "weekly"),
    (lambda u: u in ("/sobre.html", "/contato.html", "/cases.html"), "0.9", "monthly"),
    (lambda u: u.startswith("/servicos/"), "0.9", "monthly"),
    (lambda u: u.startswith("/setores/"), "0.9", "monthly"),
    (lambda u: u == "/blog/", "0.8", "weekly"),
    (lambda u: u.startswith("/blog/posts/"), "0.7", "monthly"),
    (lambda u: u.startswith("/materiais/"), "0.6", "monthly"),
    (lambda u: u in ("/faq.html", "/parceiros.html", "/trabalhe-conosco.html"), "0.5", "yearly"),
    (lambda u: u in ("/politica-privacidade.html", "/politica-cookies.html", "/termos-uso.html"), "0.3", "yearly"),
]


def url_for(path):
    """Converte path de arquivo em URL. /index.html vira /."""
    p = "/" + str(path).replace(os.sep, "/")
    if p.endswith("/index.html"):
        p = p[:-10]  # mantém a barra
    return p


def priority_for(url):
    for matcher, prio, freq in PRIORITIES:
        if matcher(url):
            return prio, freq
    return "0.5", "monthly"


def collect_pages():
    pages = []
    for path in ROOT.rglob("*.html"):
        rel = path.relative_to(ROOT)
        if rel.name in EXCLUDE:
            continue
        # Pular arquivos em pastas técnicas
        parts = rel.parts
        if any(p in ("posts-md", "node_modules", ".git", "revisao-copy") for p in parts):
            continue
        url = url_for(rel)
        mtime = datetime.fromtimestamp(path.stat().st_mtime).strftime("%Y-%m-%d")
        pages.append((url, mtime, path))
    return sorted(pages)


def build_sitemap(pages):
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for url, lastmod, _ in pages:
        prio, freq = priority_for(url)
        full = BASE_URL + url
        lines.append("  <url>")
        lines.append(f"    <loc>{full}</loc>")
        lines.append(f"    <lastmod>{lastmod}</lastmod>")
        lines.append(f"    <changefreq>{freq}</changefreq>")
        lines.append(f"    <priority>{prio}</priority>")
        lines.append("  </url>")
    lines.append("</urlset>")
    return "\n".join(lines) + "\n"


def main():
    pages = collect_pages()
    if not pages:
        print("Nenhuma página encontrada.")
        sys.exit(1)
    xml = build_sitemap(pages)
    out = ROOT / "sitemap.xml"
    out.write_text(xml, encoding="utf-8")
    print(f"sitemap.xml gerado com {len(pages)} URLs.")
    for url, _, _ in pages[:5]:
        print(f"  {url}")
    if len(pages) > 5:
        print(f"  ... e mais {len(pages)-5}")


if __name__ == "__main__":
    main()
