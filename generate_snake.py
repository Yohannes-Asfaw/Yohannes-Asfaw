import json
import urllib.request
from datetime import datetime

user = "Yohannes-Asfaw"
url = f"https://github-contributions-api.jogruber.de/v4/{user}?y=last"
req = urllib.request.Request(url, headers={"User-Agent": "snake-gen"})
data = json.load(urllib.request.urlopen(req, timeout=30))

weeks = {}
for c in data["contributions"]:
    dt = datetime.strptime(c["date"], "%Y-%m-%d")
    key = f"{dt.isocalendar()[0]}-W{dt.isocalendar()[1]:02d}"
    if key not in weeks:
        weeks[key] = [0] * 7
    weeks[key][dt.weekday()] = c["count"]

keys = sorted(weeks.keys())[-53:]
cols = len(keys)
cell, pad, rad = 11, 3, 2
W = pad * 2 + cols * (cell + pad)
H = pad * 2 + 7 * (cell + pad)

colors = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]


def level(n):
    if n == 0:
        return 0
    if n <= 1:
        return 1
    if n <= 3:
        return 2
    if n <= 6:
        return 3
    return 4


rects = []
points = []
for ci, k in enumerate(keys):
    for ri in range(7):
        count = weeks[k][ri]
        x = pad + ci * (cell + pad)
        y = pad + ri * (cell + pad)
        rects.append(
            f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="{rad}" fill="{colors[level(count)]}"/>'
        )
        if count > 0:
            points.append((x + cell / 2, y + cell / 2))

path_d = ""
if points:
    path_d = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in points[:150])

head = ""
tail = ""
if points:
    head = f'<circle cx="{points[0][0]:.1f}" cy="{points[0][1]:.1f}" r="5" fill="#58a6ff"/>'
    tail = f'<circle cx="{points[-1][0]:.1f}" cy="{points[-1][1]:.1f}" r="4" fill="#f85149"/>'

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <rect width="100%" height="100%" fill="#0d1117"/>
  {''.join(rects)}
  <path d="{path_d}" fill="none" stroke="#8957e5" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
  {head}
  {tail}
</svg>"""

with open(r"c:\Users\jovan\Downloads\Readmeforgithub\assets\contribution-snake.svg", "w", encoding="utf-8") as f:
    f.write(svg)

print(f"Generated snake {W}x{H} with {len(points)} points")
