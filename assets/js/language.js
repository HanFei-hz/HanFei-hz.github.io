'use strict';

// Load in the head so a saved language preference is resolved before rendering.
(() => {
  const preferenceKey = 'preferred-language';
  const currentLanguage = document.documentElement.lang.toLowerCase().startsWith('zh') ? 'zh' : 'en';
  const currentUrl = new URL(location.href);
  const requested = currentUrl.searchParams.get('lang');
  const validLanguage = value => value === 'en' || value === 'zh';
  const remember = language => {
    try { localStorage.setItem(preferenceKey, language); } catch (_) {}
  };
  let saved;
  try { saved = localStorage.getItem(preferenceKey); } catch (_) {}
  const preferred = validLanguage(requested) ? requested : validLanguage(saved) ? saved : currentLanguage;

  if (validLanguage(requested)) remember(requested);
  if (preferred !== currentLanguage) {
    const destination = new URL(preferred === 'zh' ? './zh.html' : './index.html', currentUrl);
    destination.search = currentUrl.search;
    destination.hash = currentUrl.hash;
    location.replace(destination.href);
    return;
  }

  function enhanceLinks() {
    const links = [...document.querySelectorAll('.language-switch [data-language]')]
      .filter(link => validLanguage(link.dataset.language));
    const syncLinks = () => {
      links.forEach(link => {
        const destination = new URL(link.getAttribute('href'), document.baseURI);
        destination.searchParams.set('lang', link.dataset.language);
        destination.hash = location.hash;
        link.href = destination.href;
        if (link.dataset.language === currentLanguage) link.setAttribute('aria-current', 'page');
        else link.removeAttribute('aria-current');
      });
    };
    links.forEach(link => link.addEventListener('click', () => {
      remember(link.dataset.language);
      syncLinks();
    }));
    window.addEventListener('hashchange', syncLinks);
    window.addEventListener('popstate', syncLinks);
    document.addEventListener('site:sectionchange', syncLinks);
    syncLinks();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', enhanceLinks, { once: true });
  else enhanceLinks();
})();
