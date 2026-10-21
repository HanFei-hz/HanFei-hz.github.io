# Fei Han — academic homepage

Source for [hanfei-hz.github.io](https://hanfei-hz.github.io), with an [English page](https://hanfei-hz.github.io/?lang=en) and a [Chinese page](https://hanfei-hz.github.io/zh.html?lang=zh). Static HTML/CSS/JS with six tabbed panels, dark/light themes, and saved language and theme preferences. First-time visitors to the root see English in the dark theme.

## Layout

```
index.html / zh.html    generated English and Chinese content
scripts/build_content.py shared bilingual content and standard-library Python builder
content/shared.html     SVG icons and BibTeX templates
assets/css/main.css     styles and color tokens (light + dark)
assets/js/main.js       accessible tabs, hash navigation, theme toggle, mobile contacts, publication filter, BibTeX dialog, video fallback
assets/js/language.js   language preference, explicit language URLs and hash preservation
assets/img/             compressed figures and photos
assets/videos/          ICRA videos (see README inside)
assets/files/           CV and the RL Explorer page
```

## Common edits

- Edit the bilingual strings in `scripts/build_content.py`, then run `python scripts/build_content.py`. Commit both generated pages; hosting does not run a build.
- **Publications:** edit the `PAPERS` list. Status is `published`, `accepted` or `review`; accepted papers share the published/accepted filter. Keep summaries focused on the work, without performance metrics.
- **BibTeX:** edit `content/shared.html` and refer to the template ID in the paper entry. The REEF BibTeX cites the public arXiv version; its visible manuscript status is Nature Mechanical Engineering, under review.
- **Research periods:** use confirmed personal participation periods, not publication years or fund execution dates. RoboMaster participation was September 2016–2019; captain in the 2017–2018 academic year, advisor for the 2019 season.
- **Doctoral training:** Westlake University–Zhejiang University joint PhD training. The doctoral research laboratory is Westlake's [i4FSI Lab](https://i4fsi.lab.westlake.edu.cn/).
- **Visiting collaboration:** the Penn State visit in [Baxi Chong's LiBR Lab](https://sites.psu.edu/libr/) is April–October 2026. The multilegged-swimming project continues with researchers from Harvard, CMU and other institutions; the manuscript is in preparation and is not counted among submitted or accepted papers.
- **CVs:** replace `assets/files/cv-{industry,academic}-{en,zh}.pdf`. All four are two-page PDFs with labeled email and website links, a homepage QR code, and separately labeled QR codes with visible URLs for the doctoral laboratory and visiting research group. `CV-Fei.pdf` remains as an alias to the English academic version for older links.
- **Video:** put the MP4 in `assets/videos/` with the name listed there.

## Preview locally

Open `index.html` in a browser, or run `python -m http.server` in this folder and visit http://localhost:8000.

## License

MIT

## Private traffic analytics

Cloudflare Web Analytics is installed once on each language page, using the same hostname token (original installation October 19, 2026). View reports by signing in to your Cloudflare account, opening **Web Analytics**, and selecting **hanfei-hz.github.io**. No visitor counter or reports are displayed on the public homepage. Access to the reports is controlled by your Cloudflare account permissions.

The beacon token in the HTML is a public site identifier, not an account API key. Keep account credentials out of this repository. Statistics begin after installation and may take a few minutes to appear. Cloudflare's default SPA tracking remains enabled for the site's tab navigation; page views and visits are different metrics.

Setup documentation: https://developers.cloudflare.com/web-analytics/get-started/

## Navigation and design

The six panels are About, Research, Publications, Videos, Resume, and Community, with corresponding Chinese labels. Only the active panel is shown when JavaScript is available. Direct hashes (including #video-icra2025, #video-icra2026, and #news), browser back/forward, and keyboard Arrow/Home/End navigation are supported. Videos pause when their panel is left. Language switching retains the active section and remembers the visitor's choice; `?lang=en` and `?lang=zh` explicitly override the saved preference. Without JavaScript, language links still work and all sections remain readable; printing also includes all panels.

## October 2026 content refresh

Confirmed research dates and roles were reconciled with the owner's current CVs. Three images were extracted from the owner's 2023 doctoral-application slides: RoboMaster robots and team (slide 6), the soft gripper (slide 7), and data-glove control experiments (slide 8). The public files preserve their visual content with web compression. Competition honors were transcribed from certificates, without publishing certificate scans or application identifiers. Earlier research proposals in those slides are not presented as completed results.

Campus activities are based on the owner's descriptions: laboratory-hosted IROS 2025 visits, school science outreach, conference volunteering, undergraduate exchanges, choir participation and exercise. The IROS visits are not presented as organization of the conference itself.

The layout is inspired by [codewithsadee/vcard-personal-portfolio](https://github.com/codewithsadee/vcard-personal-portfolio), adapted for academic work with original site content and teal accents. The existing MIT license is retained.
