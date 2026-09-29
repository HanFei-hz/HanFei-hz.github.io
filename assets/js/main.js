'use strict';

// ---------- theme toggle ----------
(function () {
  const root = document.documentElement;
  const btn = document.getElementById('theme-toggle');
  const systemDark = () => window.matchMedia('(prefers-color-scheme: dark)').matches;
  btn.addEventListener('click', () => {
    const current = root.dataset.theme || (systemDark() ? 'dark' : 'light');
    const next = current === 'dark' ? 'light' : 'dark';
    root.dataset.theme = next;
    try { localStorage.setItem('theme', next); } catch (e) {}
  });
})();

// ---------- mobile menu ----------
(function () {
  const nav = document.getElementById('nav');
  const btn = document.getElementById('menu-toggle');
  btn.addEventListener('click', () => {
    const open = nav.classList.toggle('is-open');
    btn.setAttribute('aria-expanded', String(open));
  });
  nav.addEventListener('click', (e) => {
    if (e.target.closest('a')) {
      nav.classList.remove('is-open');
      btn.setAttribute('aria-expanded', 'false');
    }
  });
})();

// ---------- highlight current section in nav ----------
(function () {
  const links = [...document.querySelectorAll('.nav a')];
  const sections = links.map((a) => document.querySelector(a.getAttribute('href'))).filter(Boolean);
  if (!('IntersectionObserver' in window)) return;
  const io = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      links.forEach((a) => a.classList.toggle('is-current', a.getAttribute('href') === '#' + entry.target.id));
    });
  }, { rootMargin: '-40% 0px -55% 0px' });
  sections.forEach((s) => io.observe(s));
})();

// ---------- publication filter ----------
(function () {
  const chips = document.querySelectorAll('.filters .chip');
  const pubs = document.querySelectorAll('#publications .pub');
  const groups = document.querySelectorAll('#publications .pub-group');
  chips.forEach((chip) => chip.addEventListener('click', () => {
    const f = chip.dataset.filter;
    chips.forEach((c) => c.classList.toggle('is-active', c === chip));
    pubs.forEach((p) => { p.hidden = f !== 'all' && p.dataset.status !== f; });
    // Hide a group heading when every paper under it is filtered out.
    groups.forEach((g) => {
      const list = g.nextElementSibling;
      g.hidden = !list.querySelector('.pub:not([hidden])');
    });
  }));
})();

// ---------- BibTeX dialog ----------
(function () {
  const dialog = document.getElementById('bib-dialog');
  const pre = document.getElementById('bib-text');
  const copy = document.getElementById('bib-copy');
  document.querySelectorAll('[data-bib]').forEach((btn) => btn.addEventListener('click', () => {
    const tpl = document.getElementById(btn.dataset.bib);
    pre.textContent = tpl ? tpl.innerHTML.replace(/&amp;/g, '&').trim() : '';
    copy.textContent = 'Copy';
    if (dialog.showModal) dialog.showModal(); else dialog.setAttribute('open', '');
  }));
  copy.addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText(pre.textContent);
      copy.textContent = 'Copied';
    } catch (e) {
      const range = document.createRange();
      range.selectNodeContents(pre);
      const sel = window.getSelection();
      sel.removeAllRanges();
      sel.addRange(range);
      copy.textContent = 'Press Ctrl+C';
    }
  });
})();

// ---------- videos: show a placeholder until the file is uploaded ----------
(function () {
  document.querySelectorAll('.video-frame').forEach((frame) => {
    const video = frame.querySelector('video');
    const source = video && video.querySelector('source');
    if (!source) return;
    const showPlaceholder = () => {
      frame.innerHTML =
        '<div class="video-placeholder"><div>' +
        '<svg viewBox="0 0 24 24"><use href="#i-play"/></svg>' +
        'Video coming soon</div></div>';
    };
    // The error may fire before this script runs, so also check the current state.
    if (video.networkState === HTMLMediaElement.NETWORK_NO_SOURCE) return showPlaceholder();
    source.addEventListener('error', showPlaceholder);
    video.addEventListener('error', showPlaceholder);
  });
})();
