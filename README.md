<p align="center">
  <picture>
    <source media="(max-width: 600px)" srcset="docs/readme/hero-mobile.webp">
    <img src="docs/readme/hero.webp" alt="Kennedy: a DSO field dossier. The archived portfolio on a laptop and a phone" width="100%">
  </picture>
</p>

<p align="center">
  <strong>The 2024 Algothrim portfolio system, preserved and re-themed as a DSO field dossier for Leon S. Kennedy.</strong><br>
  Every section of a personal portfolio, written in character. Vanilla HTML, CSS and JavaScript.
</p>

<p align="center">
  <a href="https://leon-kennedy-portfolio-archive.vercel.app"><img alt="Archive: Open the dossier" src="https://img.shields.io/badge/Archive-Open%20the%20dossier-b81c20?style=for-the-badge"></a>
</p>

<p align="center">
  <a href="#what-it-looks-like">What it looks like</a> ·
  <a href="#sections">Sections</a> ·
  <a href="#design">Design</a> ·
  <a href="#run-it-locally">Run it locally</a>
</p>

## What this is

Before thealgothrim.com became what it is now, it ran on this layout: a one-page portfolio with an about block, skill bars, a timeline, services, a project carousel, testimonials and a contact form. Rather than delete it, the system was kept as a standalone site and re-skinned to prove how far one structure can stretch.

The subject is Leon Scott Kennedy from *Resident Evil*. The portfolio becomes a classified file: skills are an arsenal, services are field ops, projects are case files and testimonials come from Ada Wong, Claire Redfield and Hunnigan.


## What it looks like

<picture>
  <source media="(max-width: 600px)" srcset="docs/readme/dossier-mobile.webp">
  <img src="docs/readme/dossier.webp" alt="Written in character: the About and Case Files sections on two laptops" width="100%">
</picture>

**Written in character.** Every section of a personal portfolio, told as a classified record.

<picture>
  <source media="(max-width: 600px)" srcset="docs/readme/arsenal-mobile.webp">
  <img src="docs/readme/arsenal.webp" alt="The arsenal: skills as capability bars on a laptop and a phone" width="100%">
</picture>

**The arsenal.** Skills as capability bars in folding panels, on every screen size.

<picture>
  <source media="(max-width: 600px)" srcset="docs/readme/contact-mobile.webp">
  <img src="docs/readme/contact.webp" alt="Light, and secure: the light theme and the Secure Contact section on two laptops" width="100%">
</picture>

**Light, and secure.** A light theme one tap away, and contact as an encrypted channel.

## Sections

| Section | In the dossier | What it does |
| --- | --- | --- |
| Home | Home | Name, rank and a one-line operative summary |
| About | Dossier | Case background, clearance level and stat callouts |
| Skills | Arsenal | Accordion groups with animated bars |
| Qualification | History | A tabbed academic and operational timeline |
| Services | Field Ops | Three specialisation cards with detail modals |
| Portfolio | Case Files | A Swiper carousel of mission reports |
| Testimonials | Field Reviews | Assessments from people who worked with him |
| Contact | Secure Contact | An "encrypted channel" form |


## Design

- **Near black with one red.** The page sits at `hsl(0, 6%, 8%)`; `#cc0000` marks buttons, icons and active states, and a deep maroon carries the footer and alert banner.
- **Written in character.** The "Human Cost" skill group rates Survival Instinct as unmeasurable and Normal Life Maintained at 0%; the academic record ends with "City was destroyed".
- **Quiet atmosphere.** A faint scanline overlay, a rare glitch on the name, staggered entrances and skill bars that fill on load.
- **Dark by default,** with a light mode that is remembered on the device.
- **Responsive,** with a bottom navigation sheet on phones.


## Built with

| Layer | Choice |
|---|---|
| Markup and style | Semantic HTML, CSS custom properties, Chakra Petch and Barlow |
| Carousels | [Swiper](https://swiperjs.com/), bundled locally |
| Icons | Unicons |
| Hosting | Vercel |


## Run it locally

<details>
<summary><strong>Setup and commands</strong></summary>

No build step. Serve the folder:

```bash
git clone https://github.com/TheAlgo7/leon-kennedy-portfolio-archive.git
cd leon-kennedy-portfolio-archive
python -m http.server 8080
```

Open http://localhost:8080. `python scripts/readme-shots.py` rebuilds the screenshots in this README from the live site.

The pictures on this page come from `scripts/readme-shots.py` (captures in `docs/readme/src/assets`) and `docs/readme/src/readme.js`, drawn by The Algothrim's README Kit.

</details>

## Licence

Copyright © 2026 Gaurav Kumar, [The Algothrim](https://thealgothrim.com). All rights reserved.

The code is public to read and learn from. It is not licensed for reuse. Leon S. Kennedy and *Resident Evil* belong to Capcom; this is a fan tribute and is not affiliated with them.
