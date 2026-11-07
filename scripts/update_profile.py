"""Render an honest portfolio dashboard using only public GitHub repository data.

No dependencies. Run --offline to render the checked-in snapshot. Without that
flag, the GitHub REST API refreshes public metadata before rendering both themes.
The optional GITHUB_TOKEN is used only in the request Authorization header.
"""
import argparse
from collections import Counter
from datetime import date, datetime, timezone
from html import escape
import json
import os
from pathlib import Path
import urllib.request
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
OWNER = "BharathLingaReddy-Palem"
PALETTE = ["#C9F488", "#9ABBF7", "#CCB6F6", "#F0BF92", "#79CEBE", "#EB9FBB"]

def public_repositories():
    repos = []
    page = 1
    while True:
        request = urllib.request.Request(
            f"https://api.github.com/users/{OWNER}/repos?type=owner&per_page=100&page={page}",
            headers={"Accept": "application/vnd.github+json", "User-Agent": f"{OWNER}-profile"},
        )
        token = os.getenv("GITHUB_TOKEN")
        if token:
            request.add_header("Authorization", f"Bearer {token}")
        with urllib.request.urlopen(request, timeout=30) as response:
            batch = json.load(response)
        if not isinstance(batch, list):
            raise ValueError("GitHub did not return a repository list")
        for repo in batch:
            if repo.get("private") or repo.get("fork") or repo["name"].casefold() == OWNER.casefold():
                continue
            repos.append({key: repo.get(key) for key in (
                "name", "language", "created_at", "pushed_at", "html_url", "fork", "archived"
            )})
        if len(batch) < 100:
            break
        page += 1
    if not repos:
        raise ValueError("Empty public data: retaining the existing charts")
    repos.sort(key=lambda item: (item["created_at"], item["name"]))
    return {"updated_at": datetime.now(timezone.utc).date().isoformat(), "repositories": repos}

def dashboard(snapshot, light=False):
    repos = snapshot["repositories"]
    count = len(repos)
    languages = Counter(repo["language"] or "Unclassified" for repo in repos)
    ranked = sorted(languages.items(), key=lambda item: (-item[1], item[0]))
    bg, panel, line, text, muted = (
        ("#F5F7F0", "#FFFFFF", "#D6DDCC", "#182419", "#5A6957") if light else
        ("#111912", "#18211A", "#354333", "#F0F2E7", "#AFBCA6")
    )
    colors = ["#568221", "#3664A7", "#7952B0", "#A36632", "#258575", "#AD507D"] if light else PALETTE
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="1440" height="590" viewBox="0 0 1440 590" role="img" aria-labelledby="title desc"><title id="title">Bharath’s public portfolio dashboard</title><desc id="desc">{count} public project repositories. Primary languages: {escape(str(dict(ranked)))}. Repository creation timeline. Updated {snapshot["updated_at"]}.</desc><rect width="1440" height="590" rx="16" fill="{bg}"/>']
    def label(x, y, value, size=15, color=None, weight=400, anchor="start"):
        parts.append(f'<text x="{x}" y="{y}" fill="{color or text}" font-family="Arial,Helvetica,sans-serif" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}">{escape(str(value))}</text>')
    label(36, 44, "PORTFOLIO / SIGNAL", 15, muted, 700)
    label(1404, 44, "PUBLIC GITHUB DATA · " + snapshot["updated_at"], 12, muted, anchor="end")
    metrics = [(str(count).zfill(2), "PUBLIC PROJECTS"), (str(len(languages)).zfill(2), "PRIMARY LANGUAGES"), ("04", "FEATURED SYSTEMS"), ("2027", "GRADUATING CLASS")]
    for i, (value, title) in enumerate(metrics):
        x = 36 + 351 * i
        parts.append(f'<rect x="{x}" y="71" width="315" height="108" rx="9" fill="{panel}" stroke="{line}"/>')
        label(x + 22, 127, value, 42, text, 700)
        label(x + 22, 154, title, 11, muted, 700)
    label(36, 223, "01 / LANGUAGE LANDSCAPE", 14, muted, 700)
    label(745, 223, "02 / BUILDING HISTORY", 14, muted, 700)
    label(36, 251, "Repositories by primary language", 13, muted)
    label(745, 251, "Cumulative public project repositories", 13, muted)
    parts.append(f'<path d="M710 213V544" stroke="{line}"/>')
    for i, (language, value) in enumerate(ranked):
        y = 292 + i * 48
        color = colors[i % len(colors)]
        label(36, y + 5, language, 15, text)
        parts.append(f'<rect x="230" y="{y - 9}" width="330" height="13" rx="6" fill="{line}"/><rect x="230" y="{y - 9}" width="{330 * value / count:.2f}" height="13" rx="6" fill="{color}"/>')
        label(657, y + 5, f"{value} / {round(value * 100 / count)}%", 13, muted, anchor="end")
    start = min(date.fromisoformat(r["created_at"][:10]) for r in repos).replace(day=1)
    end = date.fromisoformat(snapshot["updated_at"]).replace(day=1)
    months = []
    cursor = start
    while cursor <= end:
        months.append(cursor)
        cursor = date(cursor.year + (cursor.month == 12), cursor.month % 12 + 1, 1)
    x0, x1, y0, y1 = 771, 1398, 492, 285
    for tick in sorted({0, count // 2, count}):
        y = y0 - (y0 - y1) * tick / max(count, 1)
        parts.append(f'<path d="M{x0} {y}H{x1}" stroke="{line}" stroke-dasharray="3 5"/>')
        label(x0 - 14, y + 4, tick, 11, muted, anchor="end")
    points = []
    totals = []
    for i, month in enumerate(months):
        total = sum(r["created_at"][:7] <= month.isoformat()[:7] for r in repos)
        totals.append(total)
        x = x0 + i * (x1 - x0) / max(len(months) - 1, 1)
        y = y0 - (y0 - y1) * total / max(count, 1)
        points.append((x, y))
    path = "M" + "L".join(f"{x:.1f},{y:.1f}" for x, y in points)
    area = path + f"L{x1},{y0}L{x0},{y0}Z"
    parts.append(f'<path d="{area}" fill="{colors[0]}" opacity=".1"/><path d="{path}" fill="none" stroke="{colors[0]}" stroke-width="3" stroke-linejoin="round"/>')
    for i, (x, y) in enumerate(points):
        if i == 0 or i == len(points) - 1 or totals[i] != totals[i - 1]:
            parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="{colors[0]}"/>')
    indices = sorted({0, len(months) // 2, len(months) - 1})
    for i in indices:
        x = x0 + i * (x1 - x0) / max(len(months) - 1, 1)
        label(x, 521, months[i].strftime("%b %Y"), 12, muted, anchor="middle")
    label(36, 567, "SOURCE: GITHUB REST API / PUBLIC, ORIGINAL REPOSITORIES / NO SKILL SCORES", 10, muted)
    parts.append('</svg>')
    svg = "\n".join(parts)
    ET.fromstring(svg)
    return svg

def buttons():
    for name, title, width, accent in [("linkedin", "LinkedIn ↗", 174, "#D9FF8A"), ("x", "X / @bharath3702 ↗", 244, "#B9CFFF"), ("github", "Explore the code ↗", 226, "#E2CEFF")]:
        svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="48" viewBox="0 0 {width} 48"><rect x=".5" y=".5" width="{width-1}" height="47" rx="7" fill="#172018" stroke="#42513E"/><circle cx="20" cy="24" r="3" fill="{accent}"/><text x="34" y="29" fill="{accent}" font-family="Arial,Helvetica,sans-serif" font-size="14" font-weight="600">{escape(title)}</text></svg>'
        (ROOT / "assets" / f"{name}.svg").write_text(svg, encoding="utf-8")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    data_path = ROOT / "data" / "repositories.json"
    snapshot = json.loads(data_path.read_text(encoding="utf-8")) if args.offline else public_repositories()
    dark, light = dashboard(snapshot), dashboard(snapshot, True)
    (ROOT / "assets").mkdir(exist_ok=True)
    (ROOT / "data").mkdir(exist_ok=True)
    (ROOT / "assets" / "portfolio-signal.svg").write_text(dark, encoding="utf-8")
    (ROOT / "assets" / "portfolio-signal-light.svg").write_text(light, encoding="utf-8")
    data_path.write_text(json.dumps(snapshot, indent=2) + "\n", encoding="utf-8")
    buttons()
    print(f'Rendered both themes from {len(snapshot["repositories"])} public projects; updated {snapshot["updated_at"]}.')

if __name__ == "__main__":
    main()
