/* ============================================================
   R2 Soluções Empresariais
   main.js · interações do site
   ============================================================ */

(function () {
  'use strict';

  /* ---------- 1 · Nav mobile drawer ---------- */
  const hamburger = document.querySelector('.masthead__hamburger');
  const drawer = document.querySelector('.nav-drawer');
  const drawerClose = document.querySelector('.nav-drawer__close');

  function openDrawer() {
    if (!drawer) return;
    drawer.classList.add('open');
    drawer.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
  }

  function closeDrawer() {
    if (!drawer) return;
    drawer.classList.remove('open');
    drawer.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
  }

  if (hamburger) hamburger.addEventListener('click', openDrawer);
  if (drawerClose) drawerClose.addEventListener('click', closeDrawer);

  // Fecha drawer ao clicar em link interno
  if (drawer) {
    drawer.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', closeDrawer);
    });
  }

  // ESC fecha drawer
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && drawer && drawer.classList.contains('open')) {
      closeDrawer();
    }
  });

  /* ---------- 2 · Smooth-scroll para âncoras internas ---------- */
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (e) {
      const href = this.getAttribute('href');
      if (!href || href === '#') return;
      const target = document.querySelector(href);
      if (target) {
        e.preventDefault();
        const offset = 80;
        const top = target.getBoundingClientRect().top + window.pageYOffset - offset;
        window.scrollTo({ top: top, behavior: 'smooth' });
      }
    });
  });

  /* ---------- 3 · LGPD banner ---------- */
  const LGPD_KEY = 'r2_lgpd_consent';
  const banner = document.querySelector('.lgpd-banner');
  const btnAceitar = document.querySelector('.lgpd-banner__accept');
  const btnRecusar = document.querySelector('.lgpd-banner__reject');

  function showBanner() {
    if (!banner) return;
    setTimeout(function () {
      banner.classList.add('visible');
    }, 800);
  }

  function hideBanner() {
    if (!banner) return;
    banner.classList.remove('visible');
  }

  function setConsent(value) {
    try {
      localStorage.setItem(LGPD_KEY, JSON.stringify({
        value: value,
        ts: Date.now()
      }));
    } catch (err) {
      // localStorage indisponível (modo anônimo, cookies bloqueados)
    }
    hideBanner();
    if (value === 'accepted') {
      enableAnalytics();
    }
  }

  function getConsent() {
    try {
      const raw = localStorage.getItem(LGPD_KEY);
      if (!raw) return null;
      return JSON.parse(raw);
    } catch (err) {
      return null;
    }
  }

  function enableAnalytics() {
    // Placeholder para GA4 / GTM
    // Ativar somente após consentimento.
    if (window._r2_analytics_loaded) return;
    window._r2_analytics_loaded = true;
    // TODO: injetar GTM ou GA4 aqui quando configurado
    // Exemplo:
    // const s = document.createElement('script');
    // s.async = true;
    // s.src = 'https://www.googletagmanager.com/gtag/js?id=G-XXXXXXX';
    // document.head.appendChild(s);
  }

  if (banner) {
    const consent = getConsent();
    if (!consent) {
      showBanner();
    } else if (consent.value === 'accepted') {
      enableAnalytics();
    }
  }

  if (btnAceitar) btnAceitar.addEventListener('click', function () { setConsent('accepted'); });
  if (btnRecusar) btnRecusar.addEventListener('click', function () { setConsent('rejected'); });

  /* ---------- 4 · Marcar item ativo na nav ---------- */
  function markActiveNavItem() {
    const path = window.location.pathname.replace(/\/$/, '') || '/';
    document.querySelectorAll('.masthead__nav a, .nav-drawer__list a').forEach(function (link) {
      const href = link.getAttribute('href');
      if (!href) return;
      const cleanHref = href.replace(/\/$/, '') || '/';
      if (cleanHref === path || (cleanHref !== '/' && path.indexOf(cleanHref) === 0)) {
        link.classList.add('active');
      }
    });
  }
  markActiveNavItem();

  /* ---------- 5 · Form submission feedback ---------- */
  document.querySelectorAll('form[data-r2-form]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      // Web3Forms integration: o form já tem action e access_key.
      // Aqui só damos feedback visual durante envio.
      const submitBtn = form.querySelector('[type="submit"]');
      if (submitBtn) {
        submitBtn.setAttribute('disabled', 'true');
        const originalText = submitBtn.textContent;
        submitBtn.setAttribute('data-original-text', originalText);
        submitBtn.textContent = 'Enviando...';
      }
    });
  });

})();
