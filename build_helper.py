"""
Build helper - R2 Site
Gera páginas internas com header, footer, FAB e banner LGPD compartilhados.
Uso interno na construção do site. Não é parte do deploy.
"""

# ========== Componentes compartilhados ==========

HEAD_BASE = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="theme-color" content="#003848">
  <link rel="canonical" href="{canonical}">

  <meta property="og:type" content="website">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:locale" content="pt_BR">
  <meta property="og:site_name" content="R2 Soluções Empresariais">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,300;1,6..72,400;1,6..72,500&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="{css_path}">
</head>
<body>

  <a class="skip-link" href="#main">Ir para o conteúdo principal</a>
"""


def header(base_path):
    """Header completo. base_path: '' para root, '../' para subpasta."""
    return f"""
  <header class="masthead" role="banner">
    <div class="masthead__stripe"></div>
    <div class="container">
      <div class="masthead__topbar">
        <div class="masthead__topbar-left">Consultoria ativa desde 2018</div>
        <div class="masthead__topbar-right">
          <a href="tel:+5575991117430">(75) 99111-7430</a>
          <a href="mailto:r2@solucoesr2.com.br">r2@solucoesr2.com.br</a>
          <span>LGPD · Sigilo absoluto</span>
        </div>
      </div>

      <div class="masthead__main">
        <a href="{base_path}index.html" class="masthead__brand" aria-label="R2 Soluções Empresariais - Home">
          <img src="{base_path}assets/logo-r2-cream-web.png" alt="R2 Soluções Empresariais" width="76" height="28">
          <span class="masthead__brand-divider" aria-hidden="true"></span>
          <span class="masthead__brand-tag">Est. 2018 · Feira de Santana, BA</span>
        </a>

        <nav class="masthead__nav" aria-label="Navegação principal">
          <a href="{base_path}index.html">Home</a>
          <a href="{base_path}sobre.html">Sobre</a>
          <a href="{base_path}servicos/index.html">Serviços</a>
          <a href="{base_path}setores/index.html">Setores</a>
          <a href="{base_path}cases.html">Cases</a>
          <a href="{base_path}blog/index.html">Blog</a>
          <a href="{base_path}contato.html">Contato</a>
        </nav>

        <div class="masthead__cta">
          <a href="{base_path}contato.html" class="btn btn--cream">Diagnóstico gratuito</a>
        </div>

        <button class="masthead__hamburger" aria-label="Abrir menu" aria-controls="nav-drawer">
          <span></span>
          <span></span>
          <span></span>
        </button>
      </div>
    </div>
  </header>

  <nav id="nav-drawer" class="nav-drawer" aria-hidden="true">
    <button class="nav-drawer__close" aria-label="Fechar menu">Fechar ×</button>
    <ul class="nav-drawer__list">
      <li><a href="{base_path}index.html">Home</a></li>
      <li><a href="{base_path}sobre.html">Sobre</a></li>
      <li><a href="{base_path}servicos/index.html">Serviços</a></li>
      <li><a href="{base_path}setores/index.html">Setores</a></li>
      <li><a href="{base_path}cases.html">Cases</a></li>
      <li><a href="{base_path}blog/index.html">Blog</a></li>
      <li><a href="{base_path}contato.html">Contato</a></li>
    </ul>
    <div class="nav-drawer__cta">
      <a href="{base_path}contato.html" class="btn btn--cream btn--lg" style="width:100%; justify-content:center;">Diagnóstico gratuito</a>
    </div>
  </nav>
"""


def footer(base_path, scripts_path):
    return f"""
  <footer class="footer" role="contentinfo">
    <div class="container">
      <div class="footer__grid">
        <div class="footer__col footer__col--r2 footer__col-r2">
          <div class="footer__name">R2 Soluções Empresariais</div>
          <p>
            Rua Professor Fernando São Paulo, 238<br>
            Ponto Central · Feira de Santana, BA<br>
            CEP 44075-045
          </p>
          <p style="margin-top:16px;">
            <a href="tel:+5575991117430">(75) 99111-7430</a><br>
            <a href="tel:+5575999992113">(75) 99999-2113</a><br>
            <a href="mailto:r2@solucoesr2.com.br">r2@solucoesr2.com.br</a><br>
            <a href="https://www.instagram.com/r2solucoesempresariais" target="_blank" rel="noopener">@r2solucoesempresariais</a>
          </p>
        </div>

        <div class="footer__col">
          <div class="footer__col-head">Serviços</div>
          <div class="footer__list">
            <a href="{base_path}servicos/tributario.html">Tributário</a>
            <a href="{base_path}servicos/gestao-administrativa.html">Gestão Administrativa</a>
            <a href="{base_path}servicos/gestao-financeira.html">Gestão Financeira</a>
            <a href="{base_path}servicos/gestao-comercial.html">Gestão Comercial</a>
          </div>
        </div>

        <div class="footer__col">
          <div class="footer__col-head">Setores</div>
          <div class="footer__list">
            <a href="{base_path}setores/empresas-familiares.html">Empresa Familiar</a>
            <a href="{base_path}setores/varejo-supermercados.html">Varejo</a>
            <a href="{base_path}setores/atacado-distribuicao.html">Atacado</a>
            <a href="{base_path}setores/postos-combustiveis.html">Postos</a>
            <a href="{base_path}setores/industria-manufatura.html">Indústria</a>
          </div>
        </div>

        <div class="footer__col">
          <div class="footer__col-head">Recursos</div>
          <div class="footer__list">
            <a href="{base_path}blog/index.html">Blog</a>
            <a href="{base_path}cases.html">Cases</a>
            <a href="{base_path}parceiros.html">Parceiros</a>
            <a href="{base_path}contato.html">Diagnóstico gratuito</a>
          </div>
        </div>

        <div class="footer__col">
          <div class="footer__col-head">Contato</div>
          <div class="footer__list">
            <a href="{base_path}contato.html">Página de contato</a>
            <a href="{base_path}faq.html">Perguntas frequentes</a>
            <a href="{base_path}trabalhe-conosco.html">Trabalhe conosco</a>
          </div>
        </div>
      </div>

      <div class="footer__bottom">
        <div>© 2026 R2 Soluções Empresariais</div>
        <div class="footer__bottom-links">
          <a href="{base_path}politica-privacidade.html">Política de Privacidade</a>
          <a href="{base_path}politica-cookies.html">Política de Cookies</a>
          <a href="{base_path}termos-uso.html">Termos de Uso</a>
        </div>
      </div>
    </div>
  </footer>

  <a href="https://wa.me/5575991117430?text={{wa_text}}"
     target="_blank" rel="noopener"
     class="fab"
     aria-label="Falar com a R2 pelo WhatsApp">
    <svg viewBox="0 0 24 24" aria-hidden="true">
      <path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/>
    </svg>
  </a>

  <div class="lgpd-banner" role="dialog" aria-label="Aviso de privacidade">
    <div class="container">
      <div class="lgpd-banner__inner">
        <p class="lgpd-banner__text">
          Usamos cookies para gerar estatísticas anonimizadas e melhorar sua experiência. Você decide. Mais detalhes na <a href="{base_path}politica-privacidade.html">Política de Privacidade</a>.
        </p>
        <div class="lgpd-banner__buttons">
          <button class="btn btn--cream lgpd-banner__accept">Aceitar</button>
          <button class="btn btn--ghost-light lgpd-banner__reject">Apenas necessários</button>
        </div>
      </div>
    </div>
  </div>

  <script src="{scripts_path}" defer></script>
</body>
</html>
"""


def build_page(filename, title, description, canonical, body_html, depth=0, wa_text=None):
    """
    depth: 0 = raiz (index.html, sobre.html, etc), 1 = subpasta (servicos/, setores/, blog/)
    """
    base_path = "../" if depth == 1 else ""
    css_path = base_path + "styles/base.css"
    scripts_path = base_path + "scripts/main.js"

    if wa_text is None:
        wa_text = "Ol%C3%A1%2C%20vim%20do%20site%20da%20R2%20e%20queria%20conversar."

    head = HEAD_BASE.format(
        title=title,
        description=description,
        canonical=canonical,
        css_path=css_path,
    )

    hdr = header(base_path)
    ftr = footer(base_path, scripts_path).replace("{wa_text}", wa_text)

    main = f'\n  <main id="main">\n{body_html}\n  </main>\n'

    return head + hdr + main + ftr


if __name__ == "__main__":
    print("Use build_page() para gerar páginas individuais.")
