"""README screenshots and hero banner, from the live site.

  python scripts/readme-shots.py            # against production
  BASE=http://localhost:8080 python scripts/readme-shots.py

Needs Python with Playwright and Chrome. Declines analytics in the throwaway
browser and writes docs/readme/*.png. docs/ and scripts/ are in .vercelignore.
"""
import base64, os
from pathlib import Path
from playwright.sync_api import sync_playwright

BASE = os.environ.get('BASE', 'https://leon-kennedy-portfolio-archive.vercel.app')
OUT = Path('docs/readme')
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

    # Hero: the name, the line, the dossier on a laptop and a phone.
    img = lambda n: 'data:image/png;base64,' + base64.b64encode((OUT / n).read_bytes()).decode()
    hero = f'''<html><head>
<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500&family=Chakra+Petch:wght@600;700&display=block" rel="stylesheet">
<style>
body {{ margin: 0; width: 1600px; height: 820px; background: #0B0B0B; font-family: Barlow; color: #F1EDED; overflow: hidden; position: relative; }}
.scan {{ position: absolute; inset: 0; background: repeating-linear-gradient(to bottom, rgba(255,255,255,0.018) 0 1px, transparent 1px 4px); }}
.glow {{ position: absolute; right: -200px; top: -240px; width: 1100px; height: 1100px; border-radius: 50%;
  background: radial-gradient(closest-side, rgba(204,0,0,0.18), rgba(204,0,0,0)); }}
.copy {{ position: absolute; left: 100px; top: 200px; width: 520px; }}
.wm {{ font-family: 'Chakra Petch'; font-weight: 700; font-size: 30px; letter-spacing: 0.32em; }}
h1 {{ margin: 44px 0 0; font-family: 'Chakra Petch'; font-size: 64px; line-height: 1.05; font-weight: 700; }}
h1 em {{ font-style: normal; color: #E01B1B; }}
p {{ margin: 28px 0 0; font-size: 22px; line-height: 1.55; color: #A8A0A0; max-width: 32ch; }}
.laptop {{ position: absolute; left: 640px; top: 110px; width: 860px; border-radius: 10px; overflow: hidden;
  border: 1px solid rgba(255,255,255,0.10); box-shadow: 0 50px 110px -40px rgba(0,0,0,0.95); background: #000; }}
.laptop img {{ display: block; width: 100%; }}
.phone {{ position: absolute; left: 1300px; top: 250px; width: 250px; border-radius: 32px; overflow: hidden;
  border: 1px solid rgba(255,255,255,0.12); box-shadow: 0 40px 90px -30px rgba(0,0,0,0.95); background: #000; }}
.phone img {{ display: block; width: 100%; }}
</style></head><body><div class="scan"></div><div class="glow"></div>
<div class="copy"><div class="wm">KENNEDY</div>
<h1>A portfolio, filed as a <em>classified dossier.</em></h1>
<p>The 2024 Algothrim portfolio system, preserved and re-themed for Leon S. Kennedy.</p></div>
<div class="laptop"><img src="{img('desktop-home.png')}"></div>
<div class="phone"><img src="{img('phone.png')}"></div>
</body></html>'''
    pg = b.new_page(viewport={'width': 1600, 'height': 820})
    pg.set_content(hero, wait_until='networkidle')
    pg.evaluate('document.fonts.ready')
    pg.wait_for_timeout(800)
    pg.screenshot(path=str(OUT / 'hero.png'))
    b.close()
print('written:', sorted(x.name for x in OUT.iterdir()))
