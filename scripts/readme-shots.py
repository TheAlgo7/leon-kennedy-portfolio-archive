"""README screenshots, from the live site.

  python scripts/readme-shots.py            # against production
  BASE=http://localhost:8080 python scripts/readme-shots.py

Needs Python with Playwright and Chrome. Declines analytics in the throwaway
browser and writes docs/readme/*.png. docs/ and scripts/ are in .vercelignore.
"""
import base64, os
from pathlib import Path
from playwright.sync_api import sync_playwright

BASE = os.environ.get('BASE', 'https://leon-kennedy-portfolio-archive.vercel.app')
OUT = Path('docs/readme/src/assets')
OUT.mkdir(parents=True, exist_ok=True)
UA = 'Mozilla/5.0 (Linux; Android 16; Pixel 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0 Mobile Safari/537.36'
PREP = "localStorage.setItem('algothrim_consent', 'denied');"
SECTIONS = ['home', 'about', 'skills', 'portfolio', 'contact']

with sync_playwright() as p:
    b = p.chromium.launch(channel='chrome')

    desk = b.new_context(viewport={'width': 1440, 'height': 900}, device_scale_factor=1.5)
    desk.add_init_script(PREP)
    d = desk.new_page()
    d.goto(BASE, wait_until='networkidle'); d.wait_for_timeout(2500)
    for sid in SECTIONS:
        d.evaluate('id => document.getElementById(id).scrollIntoView({block: "start"})', sid)
        d.wait_for_timeout(1500)
        d.screenshot(path=str(OUT / f'desktop-{sid}.png'))
    d.evaluate('scrollTo(0, 0)'); d.wait_for_timeout(600)
    d.locator('#theme-button').click(); d.wait_for_timeout(1200)
    d.screenshot(path=str(OUT / 'desktop-light.png'))
    desk.close()

    mob = b.new_context(viewport={'width': 393, 'height': 852}, device_scale_factor=2, user_agent=UA, is_mobile=True, has_touch=True)
    mob.add_init_script(PREP)
    m = mob.new_page()
    m.goto(BASE, wait_until='networkidle'); m.wait_for_timeout(2500)
    m.screenshot(path=str(OUT / 'phone.png'))
    m.evaluate('document.getElementById("skills").scrollIntoView({block: "start"})'); m.wait_for_timeout(1500)
    m.screenshot(path=str(OUT / 'phone-skills.png'))
    mob.close()

    b.close()
print('written:', sorted(x.name for x in OUT.iterdir()))
