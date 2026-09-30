# Fei Han — academic homepage

Source for [hanfei-hz.github.io](https://hanfei-hz.github.io). Plain HTML/CSS/JS, no build step. A persistent profile card and six tabbed panels, with dark/light themes and a saved theme preference. First-time visitors see the dark theme.

## Layout

```
index.html              all content (news, research, publications, videos, experience)
assets/css/main.css     styles and color tokens (light + dark)
assets/js/main.js       accessible tabs, hash navigation, theme toggle, mobile contacts, publication filter, BibTeX dialog, video fallback
assets/img/             compressed figures and photos
assets/videos/          ICRA videos (see README inside)
assets/files/           CV and the RL Explorer page
```

## Common edits

- **News:** add an `<li>` at the top of `<ol class="news">`.
- **Publication:** copy an `<li class="pub">` block. `data-status` is `published`, `preprint` or `review` (drives the filter). Mark yourself with `<b>Fei Han</b>`.
- **Paper accepted:** change `data-status="review"` to `published` and the badge class `badge-review` to `badge-pub`.
- **BibTeX:** add a `<template id="bib-xxx">` at the bottom of `index.html` and a `<button data-bib="bib-xxx">` in the paper's links.
- **Video:** put the MP4 in `assets/videos/` with the name listed there.

## Preview locally

Open `index.html` in a browser, or run `python -m http.server` in this folder and visit http://localhost:8000.

## License

MIT

## Navigation and design

The six panels are About, Research, Publications, Videos, Resume, and Beyond the Lab. Only the active panel is shown when JavaScript is available. Direct hashes (including #video-icra2025, #video-icra2026, and #news), browser back/forward, and keyboard Arrow/Home/End navigation are supported. Videos pause when their panel is left. Without JavaScript, all content remains readable; printing also includes all panels.

The layout is inspired by [codewithsadee/vcard-personal-portfolio](https://github.com/codewithsadee/vcard-personal-portfolio), adapted for academic work with original site content and teal accents. The existing MIT license is retained.
