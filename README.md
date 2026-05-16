# R2 Site · Bloco 2 entregue

Onda T5 (Blog completo) + Onda T8 parcial (sitemap, robots, CNAME).

## O que tem de novo

### Blog (10 arquivos)
- `blog/index.html` · Hub com 8 posts em lista editorial + filtro por categoria
- `blog/posts/` · 8 posts em HTML estático (4 do Rogel, 4 do Ricardo)
- `blog/posts-md/exemplo-novo-post.md` · Modelo para criar posts futuros

### Scripts Python
- `build-blog.py` · Converte Markdown para HTML usando o template editorial
- `gen-sitemap.py` · Gera o sitemap.xml automaticamente
- `blog_helper.py` · Função interna usada pelo build-blog (não precisa editar)
- `build_helper.py` · Helper para páginas internas (não precisa editar)

### Infraestrutura
- `sitemap.xml` · 22 URLs com prioridades e changefreq por padrão
- `robots.txt` · Permite tudo, aponta para sitemap
- `CNAME` · Domínio `www.solucoesr2.com.br` para GitHub Pages

## Os 8 posts

| # | Autor | Categoria | Título | Tempo |
|---|---|---|---|---|
| 1 | Rogel | Tributário | Reforma Tributária no Varejo: o que muda para supermercados em 2027 | 6 min |
| 2 | Ricardo | Empresa Familiar | Sucessão familiar: o que a próxima geração precisa para destravar | 6 min |
| 3 | Rogel | Tributário | Como identificar créditos tributários esquecidos | 5 min |
| 4 | Rogel | Tributário | Recuperação tributária: como funciona o modelo no êxito | 5 min |
| 5 | Ricardo | Gestão Financeira | BI para varejo: por onde começar | 5 min |
| 6 | Ricardo | Empresa Familiar | Profissionalizar empresa familiar sem matar a cultura | 5 min |
| 7 | Rogel | Empresa Familiar | Holding familiar: quando faz sentido e quando é só estrutura cara | 6 min |
| 8 | Ricardo | Gestão Financeira | Margem real ou aparente: qual número você está olhando? | 5 min |

Todos têm:
- Drop cap no primeiro parágrafo
- Subtítulos H2 com filete superior
- Pull quotes editoriais em creme com filete dourado
- Tabelas com cabeçalho gold em micro caps
- Listas com numerais romanos italic gold (ordenadas) ou bullets gold (não ordenadas)
- Bloco "Sobre o autor" no rodapé
- 3 posts relacionados ao final
- Schema.org Article com metadados completos
- OG tags + canonical

## Como criar um novo post

Duplique `blog/posts-md/exemplo-novo-post.md`, edite o front matter e o conteúdo, e rode:

```bash
python3 build-blog.py blog/posts-md/seu-novo-post.md
```

O HTML aparece em `blog/posts/seu-novo-post.html` com o mesmo layout dos outros.

Para regenerar **todos** os posts (útil se você editar o template):

```bash
python3 build-blog.py --all
```

Sintaxe Markdown suportada:
- `## H2` e `### H3`
- `**negrito**`, `*italico*`, `` `código` ``, `[link](url)`
- Listas com `-` (bullet) ou `1. 2. 3.` (numeradas)
- `> bloco de citação`
- Tabelas com `|` (estilo GitHub)

## Como atualizar o sitemap

Sempre que adicionar páginas novas:

```bash
python3 gen-sitemap.py
```

Lê os HTMLs do projeto e gera `sitemap.xml` com prioridades adequadas.

## Como testar localmente

```bash
cd r2-site-bloco-2
python3 -m http.server 8000
# abre http://localhost:8000
# navegue para /blog/ para ver o hub
```

## Estatísticas finais (cumulativas)

- **22 páginas HTML** (Home + Sobre + 5 Serviços + 6 Setores + 1 Blog hub + 8 Posts)
- **base.css:** 80 KB (com componentes editoriais de blog)
- **main.js:** 4 KB
- **Posts:** 135 KB total (média de 17 KB cada)
- **sitemap.xml:** 22 URLs
- **Em-dashes:** 0 em todos os 22 HTMLs
- **H1 por página:** 1 em todas (validado)

## Pendências para go-live

(Inalterado desde o Bloco 1.)

1. **Web3Forms key** · trocar `YOUR_ACCESS_KEY_HERE` no `index.html`
2. **Logos parceiros** Tax Group + Dr. Fiscal
3. **Bios completas dos sócios** na página `sobre.html`
4. **CNPJ da R2** para política de privacidade (próximo bloco)

## Próximo: Bloco 3

- **Onda T6** · Contato + Obrigado + 404 + FAQ + Trabalhe Conosco + Parceiros
- **Onda T7** · Política de Privacidade + Política de Cookies + Termos de Uso

Avise quando puder começar.
