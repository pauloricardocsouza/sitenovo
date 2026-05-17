# Guia de deploy · R2 Soluções Empresariais

Passo a passo para colocar o site no ar. Tudo abaixo é necessário antes do go-live.

## 1. Web3Forms (formulários funcionais)

O site tem **5 formulários** que enviam mensagens via Web3Forms (serviço gratuito, sem cadastro pesado):

- `index.html` (Isca 01 · diagnóstico)
- `contato.html`
- `trabalhe-conosco.html`
- `materiais/checklist-reforma-tributaria.html`
- `materiais/guia-governanca-empresa-familiar.html`

### Como configurar

1. Acesse https://web3forms.com
2. Clique em "Create Access Key", informe seu email (`r2@solucoesr2.com.br`)
3. Copie a access key que aparecer
4. Substitua em todos os HTMLs de uma vez:

```bash
cd r2-site-final
find . -name "*.html" -exec sed -i 's/YOUR_ACCESS_KEY_HERE/cole-sua-chave-aqui/g' {} \;
```

5. Verifique que substituiu em 5 arquivos:

```bash
grep -rn "YOUR_ACCESS_KEY_HERE" .
# deve retornar zero ocorrências
```

6. Teste enviando um formulário (vai chegar no email cadastrado).

## 2. CNPJ da R2

Procure por `CNPJ a definir`:

- `politica-privacidade.html` (uma ocorrência)
- `termos-uso.html` (uma ocorrência)

Substitua pelo CNPJ real da R2 Soluções Empresariais.

```bash
sed -i 's/CNPJ a definir/00.000.000\/0001-00/g' politica-privacidade.html termos-uso.html
```

## 3. Bios dos sócios

Em `sobre.html`, há placeholders para as bios completas. Procure por `[Bio detalhada a definir]` e substitua por 3-4 linhas em italic editorial sobre cada sócio (formação, experiência, perfil de atuação).

Sugestão de tom: prosa editorial em terceira pessoa, focada em competência técnica e trajetória, evitando autopromoção.

## 4. Logos dos parceiros

Em `index.html`, `sobre.html` e `parceiros.html`, os logos de Tax Group e Dr. Fiscal estão como **placeholder texto**.

Quando você tiver os PNGs (com autorização formal de uso), substitua:

```html
<!-- Antes -->
<div class="parceiro__logo-placeholder">TAX GROUP</div>

<!-- Depois -->
<img src="assets/logo-tax-group.png" alt="Tax Group" class="parceiro__logo">
```

Salve os PNGs em `assets/` com fundo transparente. Recomendação: ~120px de altura.

## 5. Os 2 PDFs de materiais

As **landing pages** estão prontas e os formulários recebem o lead. Falta produzir os 2 PDFs:

- `materiais/checklist-reforma-tributaria.html` → PDF com sete eixos
- `materiais/guia-governanca-empresa-familiar.html` → PDF de 24 páginas

Opções:
- Diagramar no Canva/Figma e exportar PDF
- Pegar o conteúdo das LPs e formatar em Word/Indesign
- Contratar um designer para fazer a versão impressa

O envio do PDF é manual (via email a partir do lead recebido) ou automatizado via Web3Forms + Zapier.

## 6. DNS no Wix

No painel da Wix:

1. Acesse Domínios > seu domínio `solucoesr2.com.br`
2. Vá em "Avançado" > "DNS"
3. Adicione um registro CNAME:
   - Nome: `www`
   - Aponta para: `seu-usuario-github.github.io`
   - TTL: padrão
4. (Opcional, mas recomendado) Redirecione `solucoesr2.com.br` (sem www) para `www.solucoesr2.com.br`

A propagação leva de 5 minutos a algumas horas.

## Deploy no GitHub Pages

```bash
cd r2-site-final

# Inicializar repositório
git init
git add .
git commit -m "Site R2 v1.0"
git branch -M main

# Crie um repositório vazio em github.com primeiro
git remote add origin https://github.com/SEU-USUARIO/r2-site.git
git push -u origin main
```

No GitHub:
- Settings > Pages
- Source: Deploy from a branch
- Branch: `main` / root
- Save
- Aguarde 1-3 minutos
- Custom domain: `www.solucoesr2.com.br` (já está configurado pelo arquivo CNAME)
- Marque "Enforce HTTPS" depois que o certificado SSL for emitido (1-24h)

## Checklist final pré go-live

- [ ] Web3Forms key configurada e testada (envie 5 emails de teste)
- [ ] CNPJ preenchido em política e termos
- [ ] Bios completas no Sobre
- [ ] Logos parceiros (ou placeholder editorial ok)
- [ ] PDFs produzidos (ou plano de envio manual definido)
- [ ] DNS configurado no Wix
- [ ] Push para GitHub feito
- [ ] GitHub Pages ativo
- [ ] HTTPS ativo
- [ ] Sitemap submetido ao Google Search Console
- [ ] Sitemap submetido ao Bing Webmaster Tools

## Pós go-live

### Análise de tráfego (opcional)

Se quiser GA4 ou Plausible, hooks LGPD-compatíveis estão no `main.js`. O analytics só é carregado após o usuário aceitar cookies de análise. Para ativar:

1. Edite `scripts/main.js`
2. Encontre o trecho `loadAnalytics()` (vazio por padrão)
3. Adicione o script do GA4 ou Plausible dentro dessa função
4. Salve, commit, push

### Manutenção contínua

A R2 pode publicar sem desenvolvedor:

- **Post novo:** ver `README.md` na raiz
- **Pequena alteração de texto:** edite HTML, commit, push
- **Página nova:** crie HTML, regere sitemap, commit, push

### Performance e SEO

Esperado no PageSpeed Insights:
- Performance: 95+
- Acessibilidade: 95+
- Best Practices: 100
- SEO: 100

Se algum desses ficar baixo após o deploy, verifique:
- Fontes externas (Google Fonts) com `preconnect`
- Imagens dos parceiros otimizadas e com `loading="lazy"`
- CSS crítico inline (já está)

---

**Boa sorte com o lançamento.**
