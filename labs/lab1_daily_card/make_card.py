"""Lab 1: draw one generative card per day. The same date always gives the same card.

    python labs/lab1_daily_card/make_card.py                 # today (UTC)
    python labs/lab1_daily_card/make_card.py --date 2026-11-10

It writes cards/<date>.png and cards/latest.png, and rewrites the block between
<!-- CARD:START --> and <!-- CARD:END --> in README.md so the repo front page shows today's card.
"""
from __future__ import annotations

import argparse
import hashlib
import io
import random
import re
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

WIDTH, HEIGHT = 600, 800
START, END = "<!-- CARD:START -->", "<!-- CARD:END -->"

# TODO (design): add your own palette, or change SHAPE_COUNT, to make the cards yours.
PALETTES = [
    ["#16192E", "#E4572E", "#2A9D8F", "#F2C14E"],
    ["#0B132B", "#1C2541", "#5BC0BE", "#FFD166"],
    ["#2B2D42", "#EF476F", "#06D6A0", "#FFD166"],
    ["#1B1B3A", "#693668", "#A74482", "#F84AA7"],
    ["#222831", "#00ADB5", "#EEEEEE", "#FF5722"],
]
SHAPE_COUNT = 9

_DAY = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def seed_for(day: str) -> int:
    return int(hashlib.sha256(day.encode()).hexdigest()[:8], 16)


def _rgb(color: str) -> tuple[int, int, int]:
    c = color.lstrip("#")
    return int(c[0:2], 16), int(c[2:4], 16), int(c[4:6], 16)


def _font(size: int):
    for path in ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", "DejaVuSans-Bold.ttf"):
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default(size=size)


def render(day: str) -> bytes:
    """Return the PNG bytes of the card for `day` (format YYYY-MM-DD)."""
    if not _DAY.match(day):
        raise ValueError("date must look like 2026-11-10")
    rng = random.Random(seed_for(day))
    palette = [_rgb(c) for c in rng.choice(PALETTES)]
    top, bottom, accents = palette[0], palette[1], palette[2:]

    base = Image.new("RGB", (WIDTH, HEIGHT))
    px = ImageDraw.Draw(base)
    for y in range(HEIGHT):
        t = y / (HEIGHT - 1)
        px.line([(0, y), (WIDTH, y)], fill=tuple(int(top[i] * (1 - t) + bottom[i] * t) for i in range(3)))

    layer = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    for _ in range(SHAPE_COUNT):
        color = rng.choice(accents)
        alpha = rng.randint(90, 190)
        x, y = rng.randint(0, WIDTH), rng.randint(0, int(HEIGHT * 0.75))
        size = rng.randint(60, 230)
        if rng.random() < 0.5:
            draw.ellipse([x - size, y - size, x + size, y + size], fill=(*color, alpha))
        else:
            draw.rounded_rectangle([x - size, y - size // 2, x + size, y + size // 2], radius=size // 4, fill=(*color, alpha))
    layer = layer.filter(ImageFilter.GaussianBlur(3))
    image = Image.alpha_composite(base.convert("RGBA"), layer)

    text = ImageDraw.Draw(image)
    text.text((36, HEIGHT - 96), day, font=_font(46), fill=(255, 255, 255, 255))
    text.text((38, HEIGHT - 44), "card of the day", font=_font(20), fill=(235, 235, 235, 220))

    out = io.BytesIO()
    image.convert("RGB").save(out, format="PNG")
    return out.getvalue()


def update_readme(readme: Path, day: str, image_path: str) -> bool:
    """Replace the block between the markers. Returns True if the file changed."""
    if not readme.exists():
        return False
    text = readme.read_text(encoding="utf-8")
    if START not in text or END not in text or text.index(START) > text.index(END):
        print(f"note: markers not found in {readme}; skipped")
        return False
    block = f"{START}\n![Card of {day}]({image_path}?v={day})\n\n_Card of {day} (UTC)_\n{END}"
    new = text[: text.index(START)] + block + text[text.index(END) + len(END):]
    if new == text:
        return False
    readme.write_text(new, encoding="utf-8")
    return True


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=datetime.now(timezone.utc).strftime("%Y-%m-%d"))
    parser.add_argument("--out", default="cards")
    parser.add_argument("--readme", default="README.md")
    args = parser.parse_args(argv)
    png = render(args.date)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / f"{args.date}.png").write_bytes(png)
    (out / "latest.png").write_bytes(png)
    changed = update_readme(Path(args.readme), args.date, f"{args.out}/latest.png")
    print(f"wrote {out}/{args.date}.png ({len(png)} bytes); readme changed: {changed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
