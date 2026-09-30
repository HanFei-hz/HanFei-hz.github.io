'use strict';

// Theme preference is applied in the document head before first paint.
(() => {
  const button = document.getElementById('theme-toggle');
  const sync = () => {
    const dark = document.documentElement.dataset.theme === 'dark';
    button.setAttribute('aria-label', dark ? 'Switch to light theme' : 'Switch to dark theme');
  };
  button.addEventListener('click', () => {
    const theme = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
    document.documentElement.dataset.theme = theme;
    try { localStorage.setItem('theme', theme); } catch (_) {}
    sync();
  });
  sync();
})();

// Progressive enhancement: without JS all sections remain readable.
(() => {
  const panels = [...document.querySelectorAll('.panel')];
  const nav = document.querySelector('.tab-nav');
  const tabs = [...nav.querySelectorAll('.tab-link')];
  const main = document.getElementById('main-content');
  const titles = new Map(tabs.map(tab => [tab.getAttribute('aria-controls'), tab.textContent]));
  nav.setAttribute('role', 'tablist');
  tabs.forEach(tab => tab.setAttribute('role', 'tab'));
  panels.forEach(panel => panel.setAttribute('role', 'tabpanel'));

  function resolve(hash) {
    let id;
    try { id = decodeURIComponent(hash.slice(1)); } catch (_) { id = ''; }
    const target = document.getElementById(id);
    const panel = target?.closest('.panel') || panels[0];
    return { panel, target: target?.closest('.panel') ? target : panel };
  }

  function activate(hash, { scroll = false, focus = false } = {}) {
    const { panel, target } = resolve(hash);
    panels.forEach(item => {
      item.hidden = item !== panel;
      if (item.hidden) item.querySelectorAll('video').forEach(video => video.pause());
    });
    tabs.forEach(tab => {
      const selected = tab.getAttribute('aria-controls') === panel.id;
      tab.setAttribute('aria-selected', String(selected));
      tab.tabIndex = selected ? 0 : -1;
      if (selected) {
        const left = tab.offsetLeft - nav.offsetLeft;
        if (left < nav.scrollLeft || left + tab.offsetWidth > nav.scrollLeft + nav.clientWidth) {
          nav.scrollTo({ left: left - 12, behavior: 'instant' });
        }
      }
    });
    document.title = `${titles.get(panel.id)} · Fei Han`;
    if (focus) panel.focus({ preventScroll: true });
    if (scroll) requestAnimationFrame(() => {
      if (target !== panel) target.scrollIntoView({ block: 'start', behavior: 'instant' });
      else window.scrollTo({ top: Math.max(0, main.getBoundingClientRect().top + window.scrollY - 20), behavior: 'instant' });
    });
  }

  function navigate(hash, options) {
    if (location.hash !== hash) history.pushState(null, '', hash);
    activate(hash, options);
  }

  document.addEventListener('click', event => {
    const link = event.target.closest('a[href^="#"]');
    if (!link || event.defaultPrevented || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    const hash = link.getAttribute('href');
    const { target } = resolve(hash);
    if (!target) return;
    event.preventDefault();
    navigate(hash, { scroll: true, focus: !link.matches('.tab-link') });
  });

  nav.addEventListener('keydown', event => {
    const current = tabs.indexOf(document.activeElement);
    if (current < 0) return;
    let next;
    if (event.key === 'ArrowRight') next = (current + 1) % tabs.length;
    else if (event.key === 'ArrowLeft') next = (current - 1 + tabs.length) % tabs.length;
    else if (event.key === 'Home') next = 0;
    else if (event.key === 'End') next = tabs.length - 1;
    else if (event.key === ' ') { event.preventDefault(); tabs[current].click(); return; }
    else return;
    event.preventDefault();
    tabs[next].focus({ preventScroll: true });
    navigate(tabs[next].getAttribute('href'), { scroll: false });
  });
  window.addEventListener('popstate', () => activate(location.hash, { scroll: true }));
  window.addEventListener('hashchange', () => activate(location.hash, { scroll: true }));
  activate(location.hash, { scroll: !!location.hash });
  document.documentElement.classList.add('tabs-ready');
})();

(() => {
  const button = document.getElementById('contact-toggle');
  const details = document.getElementById('profile-details');
  button.addEventListener('click', () => {
    const open = details.classList.toggle('is-open');
    button.setAttribute('aria-expanded', String(open));
  });
})();

// ---------- publication filter ----------
(function () {
  const chips = document.querySelectorAll('.filters .chip');
  const pubs = document.querySelectorAll('#publications .pub');
  const groups = document.querySelectorAll('#publications .pub-group');
  chips.forEach(chip => chip.setAttribute('aria-pressed', String(chip.classList.contains('is-active'))));
  chips.forEach((chip) => chip.addEventListener('click', () => {
    const f = chip.dataset.filter;
    chips.forEach((c) => { c.classList.toggle('is-active', c === chip); c.setAttribute('aria-pressed', String(c === chip)); });
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
