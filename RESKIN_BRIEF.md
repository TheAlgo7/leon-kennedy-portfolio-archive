# Leon Kennedy Portfolio Archive — Reskin Brief

> **For the developer doing the reskin.**
> The current site is themed as Dr. Bruce Banner (Hulk / Marvel). You need to retheme it fully to **Leon Scott Kennedy** from the *Resident Evil* franchise. The page structure, CSS architecture, JavaScript, and layout must stay exactly the same. Only content, copy, colour palette, and images change.

---

## 1. Who Is Leon Scott Kennedy?

Leon Scott Kennedy is a fictional character from Capcom's **Resident Evil** survival horror series.

### Core Bio
- **Full name:** Leon Scott Kennedy
- **First appearance:** Resident Evil 2 (1998)
- **Key games:** Resident Evil 2, Resident Evil 4, Resident Evil 6, Resident Evil: Damnation (film)
- **Affiliation:** Originally Raccoon City Police Department (RPD) → Later a U.S. Government Special Agent / DSO (Division of Security Operations)
- **Employer (by RE4):** Works directly for the U.S. President, assigned to rescue the President's daughter Ashley Graham

### Personality & Tone
- Cool, composed, and sarcastic under extreme pressure
- A survivor who turns trauma into expertise
- Known for one-liners and dark humour even in life-or-death situations
- Deeply loyal, morally grounded — refuses to compromise on innocent lives
- Has seen the worst of bioterrorism and kept going anyway

### Key Story Points
- **Raccoon City (RE2):** His first day as a rookie cop. The city is overrun by zombies from the T-Virus. He escapes with Claire Redfield. This event defines his entire career.
- **RE4:** Six years after Raccoon City. Now a top-tier government agent, sent solo into rural Spain to rescue Ashley Graham from a cult (Los Illuminados) using a parasitic organism called Las Plagas.
- **RE6:** Fights multiple bioterror outbreaks across the globe. Partners with Helena Harper.

### Skills & Capabilities (for the "Abilities" section)
| Skill | Level |
|---|---|
| Combat / Tactical Firearms | Elite (100%) |
| Close-Quarters Combat (CQC) | Expert (95%) |
| Bioterrorism Countermeasures | Expert (90%) |
| Virus / Parasite Analysis | Advanced (80%) |
| Crisis Survival & Evasion | Unmeasurable |
| Government Protocol & Intel | Expert (85%) |

### Famous Quotes (can use as testimonial copy or intro text)
- *"I don't have time to explain. Just move."*
- *"It's Leon. Leon Kennedy."*
- *"Saddler, you're small-time."*
- *"I'll buy you some time. Just make sure you use it."*

---

## 2. What Needs to Change — Section by Section

Work through `index.html` top to bottom. Do not touch the HTML structure, CSS class names, JavaScript, or layout. Only swap out the **text content**, **image `src`/`alt`**, and the **colour palette** in `archive.css`.

---

### 2.1 `<head>` — Metadata

| Field | Current (Banner) | Replace With (Leon) |
|---|---|---|
| `<title>` | `Dr. Bruce Banner \| Research Archive` | `Leon S. Kennedy \| Classified Dossier` |
| `<meta name="description">` | Hulk-themed description | `Classified dossier of Leon Scott Kennedy — U.S. Government Special Agent and Raccoon City survivor. Resident Evil operative profile.` |
| `<meta name="theme-color">` | `#5ca629` (Hulk green) | `#8b0000` (deep blood red) OR `#1a1a2e` (dark navy tactical) — choose whichever fits the palette you pick |

---

### 2.2 Navigation / `<header>`

| Element | Current | Replace With |
|---|---|---|
| `.nav__logo` (text) | `B A N N E R` | `K E N N E D Y` |
| Nav link "Bio" label | `Bio` | `Dossier` |
| Nav link "Abilities" label | `Abilities` | `Loadout` |
| Nav link "Research" label | `Research` | `Operations` |
| Nav link "Missions" label | `Missions` | `Missions` *(keep as-is)* |
| Nav link "Contact" label | `Contact` | `Contact` *(keep as-is)* |

---

### 2.3 Home Section (`#home`)

| Element | Current | Replace With |
|---|---|---|
| `.home__blob-img` src | `assets/img/archive/banner-profile.png` | New Leon Kennedy image (see §4) |
| `.home__blob-img` alt | `Bruce Banner` | `Leon S. Kennedy` |
| `.home__title` | `Dr. Bruce Banner` | `Leon S. Kennedy` |
| `.home__subtitle` | `Nuclear Physicist` | `Government Special Agent` |
| `.home__description` | Gamma radiation / Rick Jones text | *"A veteran of Raccoon City and countless bioterror operations. First day on the job, the city fell. Every mission since has been a war no one else could survive."* |
| `.button` text (CTA) | `Access Files` | `Open Dossier` |
| Home social icons (3 × `uil-*`) | `uil-flask`, `uil-shield`, `uil-atom` | `uil-shield-check`, `uil-crosshair`, `uil-map-marker` (or similar tactical Unicons) |

---

### 2.4 About Section (`#about`)

| Element | Current | Replace With |
|---|---|---|
| `section__title` | `About Me` | `About Me` *(keep)* |
| `section__subtitle` | `Classified Bio` | `Agent Profile` |
| `about__img` src | `assets/img/archive/about.jpg` | New Leon image (see §4) |
| `about__img` alt | `Bruce Banner profile photo` | `Leon S. Kennedy` |
| `about__description` | Hulk / gamma radiation bio | *"Leon S. Kennedy is a U.S. Government Special Agent operating under the DSO (Division of Security Operations). A survivor of the 1998 Raccoon City incident, he has since dedicated his life to combating bioterrorism at the highest level. He doesn't flinch. He adapts."* |
| Info stat 1 | `07` / `PhDs Held` | `1998` / `Raccoon City` |
| Info stat 2 | `Infinite` / `Gamma Capacity` | `Classified` / `Active Operations` |
| Info stat 3 | `Lv. 8` / `S.H.I.E.L.D Access` | `Level 10` / `DSO Clearance` |
| Download button text | `Download Log` | `Access Report` |

---

### 2.5 Skills Section (`#skills`)

Replace all three skill group cards. Keep the exact HTML structure (accordions, progress bars, percentages). Just swap category names, icons, and skill names.

**Group 1 (currently "Nuclear Physics") → "Tactical Combat"**
- Icon: `uil-shield-check` or `uil-crosshair`
- Subtitle: `Elite Operative`
- Skills:
  - Firearms Proficiency → 100%
  - Close-Quarters Combat → 95%
  - Tactical Evasion → 90%

**Group 2 (currently "Bio-Chemistry") → "Bioterrorism Intel"**
- Icon: `uil-virus` or `uil-flask`
- Subtitle: `Field Expert`
- Skills:
  - Virus Threat Analysis → 85%
  - Parasite Countermeasures → 88%

**Group 3 (currently "Combat Capabilities") → "Field Operations"**
- Icon: `uil-map-marker` or `uil-mountains`
- Subtitle: `Raccoon City Graduate`
- Skills:
  - Crisis Survival → Unmeasurable (bar at 100%)
  - Adaptability Under Fire → Indestructible (bar at 100%)
  - Backup Plans → Variable (bar at 75%)

---

### 2.6 History / Qualification Section

#### Academic Tab (rename to match Leon's training background):

| Current | Replace With |
|---|---|
| Title: `Nuclear Physics PhD` / Caltech | Title: `Police Academy Training` / Raccoon City PD |
| Title: `Biochemistry PhD` / Culver University | Title: `Government Field Training` / DSO Programme |
| Title: `Gamma Radiation Study` / U.S. Military | Title: `Classified Briefing` / White House Clearance |

#### Operational Tab:

| Current | Replace With |
|---|---|
| `Founding Member` / The Avengers / 2012 - Present | `Rookie Officer` / Raccoon City Police Dept. / 1998 |
| `Gladiator / King` / Planet Sakaar | `Special Agent` / Office of the President / 2004 |
| `Member` / The Defenders | `DSO Operative` / Division of Security Operations / 2009 - Present |

---

### 2.7 Services / Operations Section (`#services`)

The section title `Research` → `Operations`. Subtitle `Areas of Expertise` → `Mission Specialisations`.

Replace three service cards:

**Card 1 — Currently "Gamma Research" → "Bioterror Neutralisation"**
- Icon: `uil-shield-check`
- Modal items:
  - Virus and BOW threat containment
  - Las Plagas parasite analysis

**Card 2 — Currently "Threat Assessment" → "Rescue Operations"**
- Icon: `uil-ambulance` or `uil-map-marker`
- Modal items:
  - High-value individual extraction
  - Zero-casualty infiltration protocols

**Card 3 — Currently "Bio-Medical Analysis" → "Weapons & Tactics"**
- Icon: `uil-crosshair`
- Modal items:
  - Advanced firearms and explosives handling
  - Melee & CQC in contaminated zones

---

### 2.8 Portfolio / Archives Section (`#portfolio`)

Section title `Archives` stays. Subtitle `Mission Reports` stays.

Replace the two Swiper slides:

**Slide 1 — Currently "Project: Avengers"**
- Image: Replace `portfolio1.jpg` with an RE2-themed image (or any Leon / Raccoon City image)
- Title: `Operation: Raccoon City`
- Description: *"1998. First day on the job. The T-Virus had already consumed the city. Worked alongside Claire Redfield to evacuate survivors and expose Umbrella Corporation."*

**Slide 2 — Currently "Project: Ultron"**
- Image: Replace `portfolio2.jpg` with an RE4-themed image (castle / Ashley / Spain)
- Title: `Operation: Las Plagas`
- Description: *"2004. Rural Spain. Extracted Ashley Graham from Los Illuminados and dismantled their Las Plagas parasite programme. Solo incursion. No backup."*

---

### 2.9 CTA Banner Section (`.project`)

| Element | Current | Replace With |
|---|---|---|
| `.project__title` | `Detected a Gamma Anomaly?` | `Bioterror Threat Detected?` |
| `.project__description` | Radiation/lab contact text | *"If you've encountered a viral outbreak, an unknown organism, or a compromised facility — report to the DSO immediately. Don't engage alone."* |
| Button text | `Report Incident` | `File Incident Report` |
| `.project__img` src | `assets/img/archive/project.png` | Replace with a Leon Kennedy action image (see §4) |

---

### 2.10 Testimonials Section

Section title: `Personnel Reviews` → `Mission Reviews`
Subtitle: `S.H.I.E.L.D Database` → `Classified Field Reports`

Replace three testimonial cards:

**Card 1 — Currently Tony Stark**
- Image: Replace `testimonial1.jpg` with an image of Ada Wong (RE character)
- Name: `Ada Wong`
- Role: `Double Agent`
- Quote: *"Kennedy is the only agent I've seen come out of that city standing. Predictable in the best way — he always goes back for the ones left behind."*

**Card 2 — Currently Natasha Romanoff**
- Image: Replace `testimonial2.jpg` with an image of Claire Redfield
- Name: `Claire Redfield`
- Role: `TerraSave Operative`
- Quote: *"Leon saved my life in Raccoon City without even knowing my name. Eight years later, he was still the first person I'd call."*

**Card 3 — Currently Thor**
- Image: Replace `testimonial3.jpg` with an image of Helena Harper or Ingrid Hunnigan
- Name: `Ingrid Hunnigan`
- Role: `DSO Intelligence Analyst`
- Quote: *"He ignores protocol, improvises constantly, and somehow survives impossible odds every single time. I'd take those results over a clean mission report any day."*

---

### 2.11 Contact Section

| Element | Current | Replace With |
|---|---|---|
| Section title | `Secure Contact` | `Secure Contact` *(keep)* |
| Section subtitle | `Encrypted Channel` | `DSO Encrypted Channel` |
| Contact info — Email | `banner.b@avengers.com` | `kennedy.l@dso.gov` |
| Contact info — Location | `Unknown (Mobile Lab)` | `Classified (Active Field)` |
| Form label — Name | `Agent Name` | `Agent Name` *(keep)* |
| Form label — Email | `Clearance Code` | `Clearance Code` *(keep)* |
| Form label — Message | `Briefing` | `Mission Briefing` |
| Submit button text | `Send Encryption` | `Transmit Secure` |

---

### 2.12 Footer

| Element | Current | Replace With |
|---|---|---|
| `.footer__title` | `BANNER` | `KENNEDY` |
| `.footer__subtitle` | `Nuclear Physicist` | `Special Agent, DSO` |
| Footer copyright | `© Earth-616 Archive.` | `© Leon Kennedy Dossier. Classified.` |
| Footer social icons | `uil-flask`, `uil-shield` | `uil-shield-check`, `uil-crosshair` (or RE-appropriate) |

---

## 3. Colour Palette Change (archive.css)

The current palette is **Hulk green** (`#5ca629`, `#2d6314`). Replace it with a **dark tactical / Resident Evil red** palette.

Open `assets/css/archive.css`. Search and replace these colour values:

| Current Value | Replace With | Usage |
|---|---|---|
| `#5ca629` | `#cc0000` | Primary accent (buttons, active links, highlights) |
| `#2d6314` | `#8b0000` | Darker accent (hover states, footer background) |
| Any green text highlights | Match above | Inline accent text |

**Suggested palette:**
```
--primary:       #cc0000;   /* Resident Evil signature red */
--primary-dark:  #8b0000;   /* Deep blood red for depth */
--background:    #0d0d0d;   /* Near-black, oppressive feel */
--surface:       #1a1a1a;   /* Card/panel backgrounds */
--text-primary:  #f0f0f0;   /* Off-white for readability */
--text-muted:    #888888;   /* Subtitles, captions */
```

> **Note:** If the CSS uses hardcoded hex values rather than CSS custom properties, do a global find-and-replace for `#5ca629` and `#2d6314` in the file.

---

## 4. Images — What Needs Replacing

All images live in `assets/img/archive/`. You need to source and drop in replacements for the following files (keep the same filenames so no HTML edits are needed for the `src` attributes):

| File | Current | Replace With |
|---|---|---|
| `banner-profile.png` | Bruce Banner portrait (transparent BG preferred) | **Leon Kennedy portrait** — ideally transparent/cutout PNG. Use official RE2 Remake or RE4 Remake Leon art. Search: *"Leon Kennedy render transparent"* |
| `about.jpg` | Bruce Banner photo | Any Leon Kennedy character art or render |
| `portfolio1.jpg` | Generic project screenshot | Raccoon City / RE2 Remake screenshot or Leon in RPD |
| `portfolio2.jpg` | Generic project screenshot | RE4 Remake screenshot — castle, village, or Ashley extraction |
| `project.png` | Generic project image | Leon Kennedy action shot (RE4 or RE6) |
| `testimonial1.jpg` | Tony Stark | Ada Wong |
| `testimonial2.jpg` | Natasha Romanoff | Claire Redfield |
| `testimonial3.jpg` | Thor | Ingrid Hunnigan or Helena Harper |

**Where to source images:**
- Capcom's official art / press kits
- Resident Evil Wiki: https://residentevil.fandom.com
- Deviantart / renders by fan artists (check licence)
- RE2 / RE4 Remake official trailers (screenshot frames)

> All images are 100% visual — this is a personal/fan portfolio archive, not a commercial product. Fair use applies.

---

## 5. Files To Edit

Only two files need changes:

```
leon-kennedy-portfolio-archive/
├── index.html          ← All content/text changes (see §2 above)
└── assets/
    └── css/
        └── archive.css ← Colour palette only (see §3 above)
```

**Do not touch:**
- `assets/js/archive.js` — no changes needed
- `assets/js/swiper-bundle.min.js` — leave as-is
- `assets/js/consent.js` — leave as-is
- `assets/css/swiper-bundle.min.css` — leave as-is
- `vercel.json` — leave as-is
- `.gitignore` — leave as-is

---

## 6. After Changes — Push & Deploy

The repo is already connected to GitHub and Vercel. Once edits are done:

```bash
git add .
git commit -m "feat: retheme to Leon Scott Kennedy (Resident Evil)"
git push
```

Vercel will auto-deploy from the `master` branch. The live URL is:
**https://leon-kennedy-portfolio-archive.vercel.app**

---

## 7. Summary Checklist

- [ ] `<title>` updated to Leon Kennedy
- [ ] `<meta description>` updated
- [ ] Nav logo: `B A N N E R` → `K E N N E D Y`
- [ ] Home section: name, subtitle, description, CTA button, social icons
- [ ] About section: image, description, 3 stat boxes
- [ ] Skills section: all 3 accordion groups renamed with Leon's capabilities
- [ ] Qualification section: Academic + Operational tabs rewritten
- [ ] Services section: 3 cards rethemed to Leon's operational specialisations
- [ ] Portfolio section: 2 slides rewritten (RE2 + RE4 missions)
- [ ] CTA banner: title, description, button text, image
- [ ] Testimonials: 3 cards replaced (Ada Wong, Claire Redfield, Hunnigan)
- [ ] Contact section: email, location updated
- [ ] Footer: name, subtitle, copyright updated
- [ ] `archive.css`: green palette replaced with red tactical palette
- [ ] All 8 images replaced in `assets/img/archive/`
- [ ] Git commit + push → Vercel auto-deploys
