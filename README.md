# R2 Soluções Empresariais · Site institucional

Versão final pronta para deploy. **38 páginas HTML · 700 KB · 36 URLs no sitemap · zero em-dashes · mobile validado (0 overflows).**

## Como rodar localmente

```bash
cd r2-site-final
python3 -m http.server 8000
# abrir http://localhost:8000
```

HTML/CSS/JS puro. Sem dependências, sem build, sem instalação.

## Estrutura

```
r2-site-final/
├── index.html                         Home
├── sobre.html, contato.html, cases.html, faq.html, parceiros.html
├── trabalhe-conosco.html, obrigado.html, 404.html
├── politica-privacidade.html, politica-cookies.html, termos-uso.html
│
├── servicos/                          Hub + 4 pilares (tributário, adm, fin, com)
├── setores/                           Hub + 5 setores (varejo, atacado, postos, ind, familiar)
├── blog/                              Hub + 8 posts assinados (4 Rogel, 4 Ricardo)
│   └── posts-md/                      Source Markdown dos posts (não publicado)
├── materiais/                         Hub + 4 materiais (2 interativos, 2 LPs de PDF)
├── ebook/                             E-book HTML 8 capítulos
│
├── styles/base.css                    Sistema editorial (77 KB)
├── scripts/main.js                    Nav drawer, FAB, banner LGPD (5 KB)
├── assets/                            4 versões da logo
│
├── build-blog.py                      Gera posts a partir de Markdown
├── gen-sitemap.py                     Regenera sitemap.xml automaticamente
├── blog_helper.py, build_helper.py    Helpers internos
│
├── sitemap.xml                        36 URLs com prioridades
├── robots.txt
└── CNAME                              www.solucoesr2.com.br
```

## Pendências para go-live

São 6 itens que dependem de você. Estão documentados em detalhe no `README-DEPLOY.md`.

1. Web3Forms access key (substituir `YOUR_ACCESS_KEY_HERE` em 5 formulários)
2. CNPJ da R2 nas páginas legais
3. Bios completas de Rogel e Ricardo no Sobre
4. Logos Tax Group + Dr. Fiscal (com autorização)
5. Os 2 PDFs dos materiais ricos
6. DNS Wix: CNAME `www` → `seu-usuario.github.io`

## Como atualizar conteúdo depois

**Post novo:**
```bash
cp blog/posts-md/exemplo-novo-post.md blog/posts-md/meu-post.md
# editar o .md (front matter + Markdown)
python3 build-blog.py blog/posts-md/meu-post.md
# adicionar manualmente no blog/index.html
python3 gen-sitemap.py
```

**Página nova:**
- Criar HTML usando estrutura existente como base
- Rodar `python3 gen-sitemap.py`

**Texto:**
- Editar HTML direto, commit, push

## Deploy no GitHub Pages

```bash
cd r2-site-final
git init && git add .
git commit -m "Site R2 v1.0"
git branch -M main
git remote add origin https://github.com/SEU-USUARIO/r2-site.git
git push -u origin main
```

No GitHub: Settings > Pages > Source: `main` branch > Save.
No Wix: CNAME `www` → `SEU-USUARIO.github.io`.

---

**R2 Soluções Empresariais · v1.0 final · 17 de maio de 2026**
