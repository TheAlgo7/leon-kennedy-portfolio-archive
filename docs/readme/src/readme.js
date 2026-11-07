// The Leon Kennedy archive's README pictures, drawn by the README Kit (Work\Playbooks\README Kit\render.py).
// Every wide picture has a "-mobile" twin that the README swaps in on screens up to 600 px.
// The screens come from scripts/readme-shots.py: the live site, desktop at 1080x675 and 2x,
// phones at 393x852 and 2x.
const RED = '#e3262a', INK = '#f2eded';
const FIELD = (at, glow = '#3a0d0e') => `radial-gradient(820px 640px at ${at}, ${glow} 0%, rgba(22,19,19,0) 70%), #161313`;
const P = (src, x, y, w, rot = 0, z = 24) => ({ type: 'phone', src, x, y, w, rot, z, glow: RED, bar: true, barBg: '#161313', barColor: '#f2eded' });
const L = (src, x, y, w, z = 20) => ({ type: 'laptop', src, x, y, w, z });
const wideLine = { width: 20, color: RED, points: [[-40, 712], [400, 690], [800, 730], [1640, 650]] };
const tallLine = (y) => ({ width: 26, color: RED, points: [[-40, y], [400, y - 40], [800, y + 10], [1120, y - 50]] });
const panel = (head, sub, items, glow) => ({
  w: 1600, h: 760, bg: FIELD('76% 54%', glow), color: INK, accent: RED,
  head: { x: 76, y: 180, size: 150, max: 530, lines: head }, sub: { x: 80, width: 500, size: 27, text: sub }, line: wideLine, items,
});
const tall = (head, sub, items, glow) => ({
  w: 1080, h: 1360, bg: FIELD('56% 74%', glow), color: INK, accent: RED,
  head: { x: 64, y: 80, size: 180, max: 950, lines: head }, sub: { x: 70, width: 930, size: 36, text: sub }, line: tallLine(1320), items,
});

window.README = {
  name: 'Kennedy', icon: 'icon.png',
  layouts: {
    hero: {
      w: 1600, h: 820, bg: FIELD('74% 54%'), color: INK, accent: RED,
      brand: { x: 80, y: 74, size: 30 },
      head: { x: 76, y: 236, size: 150, max: 600, lines: ['DSO field', 'dossier'] },
      sub: { x: 80, width: 500, size: 27, gap: 34, text: 'The 2024 Algothrim portfolio system, preserved and re-themed for Leon S. Kennedy.' },
      line: { width: 20, color: RED, points: [[-40, 770], [300, 724], [640, 708], [900, 772], [1200, 714], [1640, 752]] },
      items: [L('desktop-home.png', 720, 110, 700), P('phone.png', 1260, 220, 250, 5)],
    },
    'hero-mobile': {
      w: 1080, h: 1350, bg: FIELD('56% 76%'), color: INK, accent: RED,
      brand: { x: 70, y: 70, size: 38 },
      head: { x: 64, y: 196, size: 200, max: 950, lines: ['DSO field', 'dossier'] },
      sub: { x: 70, width: 930, size: 38, text: 'The 2024 Algothrim portfolio system, re-themed for Leon S. Kennedy.' },
      line: { width: 26, color: RED, points: [[-40, 1300], [300, 1250], [600, 1296], [1120, 1222]] },
      items: [L('desktop-home.png', 110, 760, 720), P('phone.png', 770, 740, 240, 5)],
    },
    dossier: panel(['Written', 'in character'], 'Every section of a portfolio, from the about page to the case files, told as a classified record.', [
      L('desktop-about.png', 700, 70, 640), L('desktop-portfolio.png', 930, 320, 560, 22),
    ]),
    'dossier-mobile': tall(['Written', 'in character'], 'Every section of a portfolio, told as a classified record.', [
      L('desktop-about.png', 90, 600, 700), L('desktop-portfolio.png', 330, 860, 640, 22),
    ]),
    arsenal: panel(['The', 'arsenal'], 'Skills as capability bars in folding panels, on the laptop and the phone alike.', [
      L('desktop-skills.png', 700, 110, 680), P('phone-skills.png', 1270, 200, 240, 5),
    ], '#2a0b0c'),
    'arsenal-mobile': tall(['The', 'arsenal'], 'Skills as capability bars in folding panels, on the laptop and the phone.', [
      L('desktop-skills.png', 110, 640, 720), P('phone-skills.png', 770, 640, 240, 5),
    ], '#2a0b0c'),
    contact: panel(['Light,', 'and secure'], 'A light theme one tap away, and a contact page written as an encrypted channel.', [
      L('desktop-light.png', 700, 70, 640), L('desktop-contact.png', 930, 320, 560, 22),
    ]),
    'contact-mobile': tall(['Light,', 'and secure'], 'A light theme one tap away, and contact as an encrypted channel.', [
      L('desktop-light.png', 90, 600, 700), L('desktop-contact.png', 330, 860, 640, 22),
    ]),
  },
};
