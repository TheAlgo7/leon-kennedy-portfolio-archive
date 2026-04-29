<div align="center">

  <img src="https://img.shields.io/badge/Leon%20Kennedy-🔰-5ca629?style=for-the-badge&labelColor=111111" alt="Leon Kennedy Portfolio Archive" />

  # Leon Kennedy — Portfolio Archive

  **The 2024 portfolio archive — a character-driven showcase preserving the original design system before the next evolution.**

  <p align="center">
    <a href="https://leon-kennedy-portfolio-archive.vercel.app">
      <img src="https://img.shields.io/badge/Live%20Site-leon--kennedy--portfolio--archive.vercel.app-5ca629?style=flat-square&logo=vercel&logoColor=white&labelColor=111111" alt="Live Site" />
    </a>
    <img src="https://img.shields.io/badge/Stack-Vanilla%20HTML%2FCSS%2FJS-5ca629?style=flat-square&labelColor=111111" alt="Vanilla Stack" />
    <img src="https://img.shields.io/badge/Year-2024%20Archive-5ca629?style=flat-square&labelColor=111111" alt="2024 Archive" />
    <img src="https://img.shields.io/badge/Built%20by-The%20Algothrim-5ca629?style=flat-square&labelColor=111111" alt="Built by The Algothrim" />
  </p>

</div>

---

## ⚡ Overview

This is the **2024 portfolio archive** — the design that came before the current Algothrim system. Rather than deleting it, it was preserved here as a standalone site: a time capsule of the skills, layout patterns, and design decisions that shaped what came after.

The site was originally themed around Dr. Bruce Banner and is slated to be rethemed to **Leon Scott Kennedy** (Resident Evil) in a future update. The structure, CSS, and interaction patterns remain intact and ready for the reskin.

Built with zero framework overhead — pure Vanilla HTML, CSS, and JavaScript with Swiper.js for the portfolio carousel.

---

## ✨ Features

- **📋 Full portfolio layout** — Home, Bio, Abilities (Skills), History (Qualification), Research (Services), Archives (Portfolio), Testimonials, and Contact sections.
- **🎯 Accordion skill bars** — Expandable skill categories with animated progress bars.
- **🗓️ Qualification timeline** — Tabbed Academic / Operational history timeline.
- **🪟 Services modals** — Click-to-expand research area cards with modal popups.
- **🎠 Portfolio carousel** — Swiper.js slider for mission/project showcases.
- **🌙 Dark/Light toggle** — Theme switcher built into the nav.
- **📱 Fully responsive** — Mobile-first layout with hamburger nav.
- **♿ Accessible** — Semantic HTML5, ARIA labels, skip-to-content link.

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| **Markup** | Semantic HTML5 |
| **Styling** | Vanilla CSS with CSS custom properties |
| **Slider** | [Swiper.js](https://swiperjs.com/) — portfolio + testimonial carousels |
| **Icons** | [Unicons 4.0.8](https://iconscout.com/unicons) (CDN) |
| **Hosting** | [Vercel](https://vercel.com/) — static deployment |

---

## 🚀 Getting Started

No build step. Just serve the files.

```bash
# Clone the repo
git clone https://github.com/TheAlgo7/leon-kennedy-portfolio-archive.git
cd leon-kennedy-portfolio-archive

# Option 1 — Open directly
start index.html

# Option 2 — Local dev server
npx serve .
# or
python -m http.server 8080
```

---

## 📂 Project Structure

```text
leon-kennedy-portfolio-archive/
├── index.html
├── assets/
│   ├── css/
│   │   ├── archive.css
│   │   └── swiper-bundle.min.css
│   ├── js/
│   │   ├── archive.js
│   │   ├── swiper-bundle.min.js
│   │   └── consent.js
│   └── img/
│       └── archive/
│           ├── favicon.svg
│           ├── banner-profile.png
│           ├── about.jpg
│           ├── portfolio1.jpg
│           ├── portfolio2.jpg
│           ├── project.png
│           └── testimonial1-3.jpg
├── .gitignore
├── vercel.json
└── README.md
```

---

## 🎨 Design Language

- **Green-accented dark mode.** The gamma-green palette (`#5ca629`) defines the colour identity — bold and distinct.
- **Structured narrative.** Every section tells a story: bio → abilities → history → work → contact.
- **Character-driven.** The site was designed to show personality through content framing, not just layout.
- **Reskin-ready.** The HTML structure and CSS are intentionally theme-agnostic — the character layer sits on top and can be swapped independently.

> **Note:** This archive is currently styled as Dr. Bruce Banner (Hulk). A full reskin to **Leon Scott Kennedy** (Resident Evil 2 / RE4) is planned as a future update.

---

<div align="center">
  Designed &amp; developed by <b><a href="https://github.com/TheAlgo7">The Algothrim</a></b>.
</div>
