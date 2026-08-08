"""Regenerate the scattered-square background layer.

Run from the site root:   python3 tools/make_background.py
Then re-render:           quarto render

Change SEED for a different arrangement, or edit `palette` for other colours.
"""
import random

SEED = 1975          # change this number to re-roll the layout
N_SQUARES = 54       # how many squares
W, H = 1600, 1150

palette = ["#F3C2D1", "#F5B9A2", "#F6E1A0", "#BCDCC6", "#B2D2ED",
           "#CDC5E7", "#A2C8C9", "#EED2A0", "#E9A9B8", "#9FC3E4"]

random.seed(SEED)

def centre_weight(x):
    """Thin the squares out behind the middle column, where the text sits."""
    return 0.30 if 0.26 < x / W < 0.74 else 1.0

rects, placed, tries = [], [], 0
while len(rects) < N_SQUARES and tries < 6000:
    tries += 1
    s = random.choice([18, 22, 26, 30, 34, 40, 46, 54, 62, 74])
    x = random.uniform(-20, W - s + 20)
    y = random.uniform(-20, H - s + 20)
    if random.random() > centre_weight(x):
        continue
    if any(abs(x - px) < (s + ps) * 0.75 and abs(y - py) < (s + ps) * 0.75
           for px, py, ps in placed):
        continue
    placed.append((x, y, s))
    c = random.choice(palette)
    op = round(random.uniform(0.42, 0.78) * 0.82, 2)
    if random.random() < 0.22:
        rects.append(f'<rect x="{x:.0f}" y="{y:.0f}" width="{s}" height="{s}" '
                     f'fill="none" stroke="{c}" stroke-width="2.5" opacity="{op}"/>')
    else:
        rects.append(f'<rect x="{x:.0f}" y="{y:.0f}" width="{s}" height="{s}" '
                     f'fill="{c}" opacity="{op}"/>')

svg = (f'<div class="bg-squares" aria-hidden="true">\n'
       f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" '
       f'preserveAspectRatio="xMidYMid slice">\n' + "\n".join(rects) +
       '\n</svg>\n</div>\n')

with open("_background.html", "w") as f:
    f.write(svg)
print(f"{len(rects)} squares written to _background.html")
