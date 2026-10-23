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
- **Publications:** edit the `PAPERS` list. Status is `published`, `accepted` or `review`; accepted papers share the published/accepted filter. Keep summaries focused on the work, without performance metrics. Fei is first author of both From Gaits to Routes (ICRA 2027, under review) and HydroWrench (ICLR 2027, under review).
- **BibTeX:** edit `content/shared.html` and refer to the template ID in the paper entry. The REEF BibTeX cites the public arXiv version; its visible manuscript status is Nature Mechanical Engineering, under review.
- **Research periods:** use confirmed personal participation periods, not publication years or fund execution dates. RoboMaster participation was September 2016–2019; captain in the 2017–2018 academic year.
- **Master's advisor:** Xingang Zhao (赵新刚), confirmed by the owner. List the advisor name in the education entry; omit administrative positions. Official profile: https://people.ucas.edu.cn/~xzhao.
- **Doctoral training:** Westlake University–Zhejiang University joint PhD training. The doctoral research laboratory is Westlake's [i4FSI Lab](https://i4fsi.lab.westlake.edu.cn/).
- **Visiting collaboration:** the Penn State visit in [Baxi Chong's LiBR Lab](https://sites.psu.edu/libr/) is April–October 2026. Fei leads the multilegged-swimming research, including reduced-order dynamics modeling, numerical simulation and experimental design. The project continues with researchers from Harvard, CMU and other institutions; the manuscript is in preparation and is not counted among submitted or accepted papers.
- **CVs:** replace `assets/files/cv-{industry,academic}-{en,zh}.pdf`. All four are two-page PDFs with labeled email and website links, a homepage QR code, and separately labeled QR codes with visible URLs for the doctoral laboratory and visiting research group. In-text publication references in the academic CV use superscript numbers; inline bold labels introduce their text with a colon. `CV-Fei.pdf` remains as an alias to the English academic version for older links. The October 23 CVs include official Westlake and Zhejiang university emblems and restrained bold emphasis for publication venues and key personal roles. Conference and journal names use black (#000000) bold text. Only the two Chinese CVs include the owner's place of origin; omit it from both English CVs.
- **CV layout authority:** preserve the owner's manually edited Word versions as the current layout authority. Apply factual corrections to those versions and derive replacement PDFs from them; do not overwrite them by rerunning an older CV generator.
- **Chinese academic CV:** the current owner-edited version places Nature Mechanical Engineering (under review), the accepted/published ICRA papers, and the ICRA 2027 and ICLR 2027 submissions together on page 1, with submission statuses explicit. ICRA entries include a Chinese description of its standing, based on the [official IEEE RAS flagship-conference description](https://2026.ieee-icra.org/about/). Per the owner's latest preference, the CV has no portrait; the turn-page reminder is in the lower right, and the homepage QR caption points readers to detailed research information and demonstration videos. Its publication numbering differs from the English academic CV and must be checked independently.
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

## Research facts and verification boundaries

- **Doctoral research directions:** since December 2023, modeling and control of bioinspired aquatic actuators have proceeded alongside quadrupedal swimming control and safe learning. Keep these linked directions distinct when describing experimental objects and validation.
- **REEF / SHOAL / V-STAR:** REEF is the learning framework, SHOAL is the force-measurement platform, and V-STAR is the learning pipeline. The research covers webbed paddles, flapping fins and tail fins through imitation learning, surrogate-model-based offline optimization and online hardware fine-tuning. Use participation wording for Fei's contributions to the shared framework, platform and actuator research.
- **HydroWrench:** a dataset and benchmark for offline reconstruction of six-axis interface loads from motion commands. Do not describe it as a pure hydrodynamic-force model or an online-control method.
- **Learn to Swim (ICRA 2025):** the LSTM learns webbed-leg hydrodynamics from force measurements. Combined with measured body drag, the component models support whole-robot dynamics, gait optimization, and hardware tests of straight swimming and turning. This work does not establish closed-loop route tracking.
- **Swimming Under Constraints (ICRA 2026):** safe reinforcement learning occurs on a physical single-leg towing platform. A recorded cycle of learned joint trajectories transfers to the quadruped with diagonal-phase coordination for free-swimming validation. Do not describe this as whole-robot online policy training or sim-to-real transfer.
- **From Gaits to Routes (ICRA 2027, under review):** component-level experiments ground the hydrodynamic simulator; behavior planning, skill distillation and closed-loop route-following evaluation occur in simulation. Physical route-following deployment is future work.
- **Storm petrel:** early simulation research, spanning the research-assistant period and the beginning of the PhD. Fei contributed to air-water modeling, deep reinforcement learning parameter tuning and simulation analysis of pattering and sea-anchoring. Do not claim primary ownership of the model, original algorithm implementation, or physical-robot validation.
- **Attribution:** distinguish paper-level collective results from personal responsibilities. Author order alone does not establish ownership of every modeling, implementation and experiment task.
