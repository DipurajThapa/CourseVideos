"""Screen design for the chapter videos: "Soft Studio".

A calm, professional look for beginners: a pale sky-to-cream gradient, frosted
white cards with soft shadows, navy text, one sky accent and a warm sand accent.
Coral is used only for errors and amber only for timers. Headings are bold
geometric capitals (Poppins), body text is Inter, code is JetBrains Mono on a
deep navy card. Layouts vary like a slide deck: a heading column with a card on
the right, centred hero cards, card grids and full-bleed title screens.

Every screen is drawn at 1920x1080. The renderer calls `render_state()` once per
distinct picture. Fonts are vendored in tools/video/fonts (open licences).
"""
from __future__ import annotations

import re
from functools import lru_cache
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont, features as _pil_features

# Code must look exactly as the learner types it. JetBrains Mono draws ligatures by default
# (">=" as one arrow-like glyph, "==" as a long bar, "!=" as a crossed sign), which would hide the
# characters a beginner has to type. Turn ligatures off for every piece of text the theme draws.
_NO_LIGATURES = ["-liga", "-calt", "-dlig"] if _pil_features.check("raqm") else None
if _NO_LIGATURES and not getattr(ImageDraw.ImageDraw, "_cq_no_ligatures", False):
    def _wrap(method):
        def inner(self, *args, **kwargs):
            kwargs.setdefault("features", _NO_LIGATURES)
            return method(self, *args, **kwargs)
        return inner
    for _name in ("text", "textlength", "textbbox"):
        setattr(ImageDraw.ImageDraw, _name, _wrap(getattr(ImageDraw.ImageDraw, _name)))
    ImageDraw.ImageDraw._cq_no_ligatures = True

W, H = 1920, 1080
FONTS = Path(__file__).resolve().parent / "video" / "fonts"
X0, X1 = 110, W - 110            # page margins
FOOT_Y = 1000                    # footer line

C = {
    "navy": "#15294A", "ink": "#1E2F4D", "muted": "#61708A", "faint": "#9AA7BA",
    "sky": "#5FAED8", "sky_deep": "#2F7FB0", "sky_soft": "#DCEEF8", "sky_tile": "#9FD0E8",
    "sand": "#F2D3A9", "sand_soft": "#FBEBD5", "cream": "#FBF4E8",
    "coral": "#D9634B", "coral_soft": "#FBE3DD", "mint": "#3E9C7E", "mint_soft": "#DDF2EA",
    "amber": "#F0A12E", "white": "#FFFFFF",
    "code_bg": "#14223A", "code_fg": "#E3E8F0", "code_hl": "#22385C", "gutter": "#5D6B85",
    "pill_bg": "#E4F0F8", "pill_fg": "#245F8A",
}

FONT_FILES = {
    "head": "Poppins-Bold.ttf", "headsb": "Poppins-Medium.ttf",
    "sans": "Inter-Regular.otf", "medium": "Inter-Medium.otf", "bold": "Inter-SemiBold.otf",
    "heavy": "Inter-Bold.otf", "mono": "jetbrains-mono-latin-400-normal.woff",
    "monob": "jetbrains-mono-latin-700-normal.woff", "sym": "DejaVuSans-Bold.ttf",
}
REQUIRED_FONTS = sorted(set(FONT_FILES.values()))


@lru_cache(maxsize=None)
def font(kind: str, size: int):
    return ImageFont.truetype(str(FONTS / FONT_FILES[kind]), int(size))


# ---------------------------------------------------------------- backgrounds and cards

def _gradient(c0: str, c1: str, c2: str | None = None) -> Image.Image:
    """Diagonal gradient from top-left c0 to bottom-right c1 (through c2 in the middle if given)."""
    import numpy as np
    def rgb(h):
        h = h.lstrip("#")
        return np.array([int(h[i:i + 2], 16) for i in (0, 2, 4)], dtype=np.float32)
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    t = (xx / W * 0.65 + yy / H * 0.35)
    t = np.clip(t, 0, 1)[..., None]
    if c2:
        a, m, b = rgb(c0), rgb(c2), rgb(c1)
        out = np.where(t < 0.5, a + (m - a) * (t / 0.5), m + (b - m) * ((t - 0.5) / 0.5))
    else:
        a, b = rgb(c0), rgb(c1)
        out = a + (b - a) * t
    return Image.fromarray(out.astype("uint8"), "RGB").convert("RGBA")


@lru_cache(maxsize=None)
def background(kind: str) -> Image.Image:
    if kind == "breather":
        return _gradient("#CFE7F5", "#F8EEDF", "#E6F2F6")
    if kind == "pause":
        return _gradient("#BFDDF0", "#F5E6D2", "#D7EAF4")
    return _gradient("#E2F0F9", "#FBF3E6", "#F3F6F6")


@lru_cache(maxsize=256)
def _shadow(w: int, h: int, radius: int, strength: int) -> Image.Image:
    pad = 40
    layer = Image.new("RGBA", (w + pad * 2, h + pad * 2), (0, 0, 0, 0))
    ImageDraw.Draw(layer).rounded_rectangle([pad, pad, pad + w, pad + h], radius=radius,
                                            fill=(21, 41, 74, strength))
    return layer.filter(ImageFilter.GaussianBlur(18))


def card(img: Image.Image, box, radius: int = 28, fill=(255, 255, 255, 200), outline=(255, 255, 255, 230),
         shadow: int = 38, width: int = 2) -> None:
    """A frosted card with a soft shadow, composited onto `img`."""
    x0, y0, x1, y1 = (int(v) for v in box)
    w, h = x1 - x0, y1 - y0
    if shadow:
        sh = _shadow(w, h, radius, shadow)
        img.alpha_composite(sh, (x0 - 40, y0 - 40 + 14))
    layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    ImageDraw.Draw(layer).rounded_rectangle([0, 0, w - 1, h - 1], radius=radius, fill=fill, outline=outline,
                                            width=width)
    img.alpha_composite(layer, (x0, y0))


def hexa(colour: str, alpha: int = 255) -> tuple:
    c = colour.lstrip("#")
    return tuple(int(c[i:i + 2], 16) for i in (0, 2, 4)) + (alpha,)


def mix(colour: str, towards: str, k: float) -> str:
    a, b = hexa(colour)[:3], hexa(towards)[:3]
    return "#%02x%02x%02x" % tuple(int(a[i] + (b[i] - a[i]) * k) for i in range(3))


# ---------------------------------------------------------------- text

RICH = re.compile(r"(`[^`]+`|\*\*[^*]+\*\*)")


def rich_runs(text: str) -> list[tuple[str, str]]:
    runs = []
    for part in RICH.split(text):
        if not part:
            continue
        if part.startswith("`"):
            runs.append(("code", part[1:-1]))
        elif part.startswith("**"):
            runs.append(("bold", part[2:-2]))
        else:
            runs.append(("text", part))
    return runs


def _fonts(size: int, base: str):
    bold = {"sans": "bold", "medium": "heavy", "bold": "heavy", "head": "head", "headsb": "head"}[base]
    return {"text": font(base, size), "bold": font(bold, size), "code": font("mono", int(size * 0.9))}


def layout_rich(text: str, size: int, width: int, base: str = "sans", upper: bool = False):
    """Lines of (kind, word, width). Code runs keep their case; text runs may be upper-cased."""
    fonts = _fonts(size, base)
    lines, line, used = [], [], 0.0
    for kind, chunk in rich_runs(text):
        if upper and kind != "code":
            chunk = chunk.upper()
        tokens = [chunk] if kind == "code" and len(chunk) <= 24 else re.findall(r"\S+|\s+", chunk)
        for word in tokens:
            if word.isspace():
                if line:
                    gap = fonts["code" if kind == "code" else "text"].getlength(" ")
                    line.append(("codespace" if kind == "code" else "space", " ", gap))
                    used += gap
                continue
            pad = 18 if kind == "code" and not (line and line[-1][0] == "codespace") else 0
            wlen = fonts[kind].getlength(word) + pad
            if line and used + wlen > width and not re.fullmatch(r"[.,:;!?)]+", word):
                while line and line[-1][0] in ("space", "codespace"):
                    used -= line.pop()[2]
                lines.append(line)
                line, used = [], 0.0
                if kind == "code":
                    wlen = fonts[kind].getlength(word) + 18
            line.append((kind, word, wlen))
            used += wlen
    if line:
        lines.append(line)
    return lines


def draw_rich(d, x: int, y: int, text: str, size: int, width: int, color: str = C["ink"], base: str = "sans",
              upper: bool = False, gap: float = 1.42, align: str = "left") -> int:
    fonts = _fonts(size, base)
    for line in layout_rich(text, size, width, base, upper):
        groups: list[list] = []
        for kind, word, wlen in line:
            is_code = kind in ("code", "codespace")
            if groups and groups[-1][0] == is_code and (is_code or kind == groups[-1][1]):
                groups[-1][2] += word
                groups[-1][3] += wlen
            else:
                groups.append([is_code, kind, word, wlen])
        total = sum(g[3] for g in groups)
        cx = x + (width - total) / 2 if align == "center" else x
        for is_code, kind, word, wlen in groups:
            if is_code:
                word = word.strip()
                wlen = fonts["code"].getlength(word) + 18
                d.rounded_rectangle([cx, y + size * 0.02, cx + wlen, y + size * 1.24], radius=8, fill=C["pill_bg"])
                d.text((cx + 9, y + size * 0.14), word, font=fonts["code"], fill=C["pill_fg"])
            elif kind != "space":
                d.text((cx, y), word, font=fonts[kind], fill=color)
            cx += wlen
        y += int(size * gap)
    return y


def rich_height(text: str, size: int, width: int, base: str = "sans", upper: bool = False, gap: float = 1.42) -> int:
    return len(layout_rich(text, size, width, base, upper)) * int(size * gap)


def tracked(d, xy, text: str, fnt, fill, spacing: float = 3.0, anchor_center: bool = False) -> float:
    """Letter-spaced small caps labels (kickers, footer)."""
    total = sum(fnt.getlength(ch) + spacing for ch in text) - spacing
    x, y = xy
    if anchor_center:
        x -= total / 2
    for ch in text:
        d.text((x, y), ch, font=fnt, fill=fill)
        x += fnt.getlength(ch) + spacing
    return total


def kicker(d, x: int, y: int, text: str, colour: str = C["sky_deep"]) -> int:
    tracked(d, (x, y), text.upper(), font("bold", 22), colour, 3.2)
    return y + 40


def heading_block(fr: "Frame", x: int, y: int, width: int, title: str, label: str = "",
                  size: int = 58, min_size: int = 34, max_lines: int = 3) -> int:
    """Kicker, bold capital title, and a short accent bar. Returns the y below it."""
    if label:
        y = kicker(fr.d, x, y, label)
    while size > min_size and len(layout_rich(title, size, width, "head", True)) > max_lines:
        size -= 2
    y = draw_rich(fr.d, x, y, title, size, width, C["navy"], base="head", upper=True, gap=1.16)
    fr.d.rounded_rectangle([x, y + 14, x + 76, y + 21], radius=4, fill=C["sky"])
    return y + 54


# ---------------------------------------------------------------- frame and chrome

class Frame:
    def __init__(self, ctx: dict, section: str, kind: str = "base"):
        self.img = background(kind).copy()
        self.d = ImageDraw.Draw(self.img)
        self.ctx = ctx
        self.section = section

    def chrome(self, progress: float) -> None:
        d = self.d
        d.line([X0, FOOT_Y, X1 - 70, FOOT_Y], fill="#C8D3E0", width=2)
        d.line([X0, FOOT_Y, X0 + int((X1 - 70 - X0) * progress), FOOT_Y], fill=C["sky"], width=4)
        tracked(d, (X0, FOOT_Y + 22), self.ctx["brand"].upper(), font("bold", 19), C["muted"], 2.6)
        tracked(d, (W / 2, FOOT_Y + 22), self.section.upper(), font("medium", 19), C["faint"], 2.6, True)
        d.rounded_rectangle([X1 - 52, FOOT_Y - 26, X1, FOOT_Y + 26], radius=10, fill=C["sky_tile"])
        d.text((X1 - 26, FOOT_Y), f"{int(self.ctx['number']):02d}", font=font("head", 22), fill=C["white"],
               anchor="mm")

    def rgb(self) -> Image.Image:
        return self.img.convert("RGB")


def settle(top: int, bottom: int, content_h: int, bias: float = 0.42) -> int:
    return top + max(0, int((bottom - top - content_h) * bias))


# ---------------------------------------------------------------- shared helpers from the renderer

def token_colours(path: Path, source: str):
    from pygments import lex
    from pygments.lexers import get_lexer_for_filename
    from pygments.styles import get_style_by_name
    style = get_style_by_name("one-dark")
    lines: list[list[tuple[str, str]]] = [[]]
    for ttype, value in lex(source, get_lexer_for_filename(path.name)):
        spec = style.style_for_token(ttype)
        colour = f"#{spec['color']}" if spec.get("color") else C["code_fg"]
        for i, piece in enumerate(value.split("\n")):
            if i:
                lines.append([])
            if piece:
                lines[-1].append((piece, colour))
    while lines and not lines[-1]:
        lines.pop()
    return lines


def wrap_plain(text: str, chars: int) -> list[str]:
    out = []
    for raw in text.split("\n"):
        while len(raw) > chars:
            cut = raw.rfind(" ", 0, chars)
            cut = cut if cut > chars // 2 else chars
            out.append(raw[:cut])
            raw = "  " + raw[cut:].lstrip()
        out.append(raw)
    return out


_TRACES: dict[str, list[str]] = {}


def real_traceback(chapter: Path, rel: str, needle: str) -> list[str]:
    """Standard output before the error plus the full error report, as a learner sees it.

    The last line must contain the verified `.expected_error` text; otherwise only that line is shown.
    """
    key = f"{chapter}/{rel}"
    if key not in _TRACES:
        import verify_chapter as vc
        chains = vc.toolchains(chapter.parent.name)
        lines = [needle]
        if chains:
            _, out, err = vc.run_file(chapter / rel, chains[0])
            errs = [x.rstrip() for x in err.rstrip().splitlines() if x.strip()]
            if errs and needle in errs[-1]:
                errs = [re.sub(r'File "[^"]*[/\\]([^/\\"]+)"', r'File "\1"', x) for x in errs]
                # A quoted path inside a message (such as Python 3.13's "consider renaming" hint) would show
                # the temporary run folder; keep only the file name, as the File lines do.
                errs = [re.sub(r"'(?:[^'\s]*[/\\])([^/\\']+\.py)'", r"'\1'", x) for x in errs]
                # An ImportError names the module's file in brackets, with the same temporary folder.
                errs = [re.sub(r"\((?:[^()\s]*[/\\])([^/\\()]+\.py)\)", r"(\1)", x) for x in errs]
                lines = [x for x in out.rstrip().splitlines()] + errs
        _TRACES[key] = lines
    return _TRACES[key]


def side_panel_lines(chapter: Path, rel: str) -> list[str]:
    stem = (chapter / rel).with_suffix("")
    out = []
    if stem.with_suffix(".expected").exists():
        out += stem.with_suffix(".expected").read_text(encoding="utf-8").split("\n")
    if stem.with_suffix(".expected_error").exists():
        out += real_traceback(chapter, rel, stem.with_suffix(".expected_error").read_text(encoding="utf-8").strip())
    return out


# ---------------------------------------------------------------- timer and questions

def timer(fr: "Frame", cx: int, cy: int, ask: dict, scale: float = 1.0) -> None:
    """Digital 00:10 countdown in a navy pill, with a sky bar that drains smoothly."""
    d = fr.d
    value, total = ask["value"], ask["total"]
    share = ask.get("fraction", value / total)
    w, h = int(300 * scale), int(116 * scale)
    warn = value <= 3
    card(fr.img, [cx - w // 2, cy - h // 2, cx + w // 2, cy + h // 2], radius=int(30 * scale),
         fill=hexa(C["navy"]), outline=hexa(C["amber"] if warn else C["navy"]), shadow=60, width=4 if warn else 1)
    colour = C["amber"] if warn else C["white"]
    d.text((cx, cy - int(8 * scale)), f"00:{value:02d}", font=font("monob", int(66 * scale)), fill=colour, anchor="mm")
    bw = w - int(64 * scale)
    bx, by = cx - bw // 2, cy + h // 2 - int(22 * scale)
    d.rounded_rectangle([bx, by, bx + bw, by + int(8 * scale)], radius=4, fill="#2A3D60")
    if share > 0:
        d.rounded_rectangle([bx, by, bx + max(8, int(bw * share)), by + int(8 * scale)], radius=4,
                            fill=C["amber"] if warn else C["sky"])


def your_turn_chip(d, x: int, y: int, done: bool) -> None:
    label = "TIME'S UP" if done else "YOUR TURN"
    f = font("bold", 22)
    w = tracked(d, (-1000, -1000), label, f, C["white"], 3) + 44
    d.rounded_rectangle([x, y, x + w, y + 44], radius=22, fill=C["sand"] if done else C["sky"])
    tracked(d, (x + 22, y + 9), label, f, C["navy"] if done else C["white"], 3)


def ask_card(fr: "Frame", box, ask: dict) -> None:
    x0, y0, x1, y1 = box
    card(fr.img, box, radius=30, fill=(255, 255, 255, 235))
    your_turn_chip(fr.d, x0 + 40, y0 + 40, ask["value"] == 0)
    width = x1 - x0 - 80
    size = 46
    room = (y1 - y0) - 330
    while size > 28 and rich_height(ask["question"], size, width, "headsb") > room:
        size -= 2
    qh = rich_height(ask["question"], size, width, "headsb")
    y = y0 + 110 + max(0, (room - qh) // 2)
    draw_rich(fr.d, x0 + 40, y, ask["question"], size, width, C["navy"], base="headsb", gap=1.3)
    if ask["value"]:
        fr.d.text(((x0 + x1) // 2, y1 - 186), "Pause the video if you need more time.", font=font("sans", 23),
                  fill=C["muted"], anchor="mm")
    timer(fr, (x0 + x1) // 2, y1 - 92, ask, 0.95)


def ask_strip(fr: "Frame", ask: dict, y0: int = 760) -> None:
    """A wide question card at the bottom, for screens whose content must stay visible."""
    box = [X0, y0, X1, FOOT_Y - 36]
    compact = FOOT_Y - 36 - y0 < 200
    card(fr.img, box, radius=28, fill=(255, 255, 255, 240))
    if compact:
        your_turn_chip(fr.d, X0 + 32, y0 + (box[3] - y0 - 44) // 2, ask["value"] == 0)
        draw_rich(fr.d, X0 + 250, y0 + (box[3] - y0) // 2 - 40, ask["question"], 32, X1 - X0 - 640, C["navy"],
                  base="headsb", gap=1.25)
        timer(fr, X1 - 170, (y0 + box[3]) // 2, ask, 0.8)
        return
    your_turn_chip(fr.d, X0 + 36, y0 + 30, ask["value"] == 0)
    draw_rich(fr.d, X0 + 36, y0 + 92, ask["question"], 38, X1 - X0 - 470, C["navy"], base="headsb", gap=1.25)
    timer(fr, X1 - 200, (y0 + FOOT_Y - 40) // 2, ask, 0.95)


# ---------------------------------------------------------------- code and output

def _mute(colour: str, bg: str = C["code_bg"], k: float = 0.5) -> str:
    return mix(colour, bg, k)


def draw_code(fr: "Frame", chapter: Path, v: dict, ask: dict | None) -> None:
    d = fr.d
    top = 96
    if v.get("heading"):
        top = heading_block(fr, X0, 84, X1 - X0, v["heading"], v.get("label", ""), size=44, min_size=30,
                            max_lines=2) - 14
    if v.get("note"):
        top = draw_rich(d, X0, top - 6, v["note"], 28, X1 - X0, C["muted"]) + 6
    src = chapter / v["file"]
    all_lines = token_colours(src, src.read_text(encoding="utf-8").rstrip("\n"))
    visible = int(v.get("lines") or len(all_lines))
    # `code_lines` shows an excerpt of a long file, keeping the real line numbers.
    only = v.get("code_lines")
    numbered = [(n, ln) for n, ln in enumerate(all_lines, start=1) if not only or n in only]
    lines = [ln for _, ln in numbered]
    side = side_panel_lines(chapter, v["file"])
    side_chars = max([28] + [len(x) for x in side])
    side_w = int(min(820, max(620, side_chars * 26 * 0.6 + 110)))
    strip = v.get("_ask_layout") == "strip"
    bottom = 720 if strip else FOOT_Y - 44
    split = X1 - side_w - 34
    code_box = [X0, top, split, bottom]
    out_box = [split + 34, top, X1, bottom]
    # code card
    card(fr.img, code_box, radius=26, fill=hexa(C["code_bg"]), outline=hexa(C["code_bg"]), shadow=70)
    for i, colour in enumerate(("#E26D5A", "#F0B54A", "#5DBB8A")):
        d.ellipse([code_box[0] + 30 + i * 26, code_box[1] + 26, code_box[0] + 44 + i * 26, code_box[1] + 40], fill=colour)
    d.text((code_box[0] + 120, code_box[1] + 21), Path(v["file"]).name, font=font("medium", 21), fill="#8D9AB3")
    max_chars = max((sum(len(p) for p, _ in ln) for ln in lines), default=1) + 6
    avail_h = code_box[3] - code_box[1] - 100
    avail_w = code_box[2] - code_box[0] - 70
    size = 34
    while size > 18 and (len(lines) * size * 1.5 > avail_h or max_chars * size * 0.6 > avail_w):
        size -= 1
    mono = font("mono", size)
    y = code_box[1] + 80
    hl = set(v.get("highlight", []))
    for n, line in numbered:
        if n > visible:
            break
        lit = n in hl
        if lit:
            d.rounded_rectangle([code_box[0] + 12, y - 6, code_box[2] - 12, y + size * 1.32], radius=8, fill=C["code_hl"])
            d.rounded_rectangle([code_box[0] + 12, y - 6, code_box[0] + 19, y + size * 1.32], radius=3, fill=C["sky"])
            d.text((code_box[2] - 30, y + size * 0.62), "◀", font=font("sym", int(size * 0.7)), fill=C["sky"],
                   anchor="rm")
        dim = bool(hl) and not lit
        d.text((code_box[0] + 34, y), f"{n:>2}", font=mono, fill=C["sky"] if lit else C["gutter"])
        x = code_box[0] + 34 + size * 0.6 * 4
        for piece, colour in line:
            d.text((x, y), piece, font=mono, fill=_mute(colour) if dim else colour)
            x += mono.getlength(piece)
        if n == visible and visible < len(all_lines):
            d.rounded_rectangle([x + 4, y + 2, x + 4 + size * 0.5, y + size * 1.2], radius=2, fill=C["sky"])
        y += int(size * 1.5)
    if ask and not strip:
        ask_card(fr, out_box, ask)
        return
    if strip and ask:
        ask_strip(fr, ask, bottom + 30)
    draw_output(fr, chapter, v, out_box)


def draw_output(fr: "Frame", chapter: Path, v: dict, box) -> None:
    d = fr.d
    is_error = bool(v.get("error"))
    card(fr.img, box, radius=26, fill=(255, 255, 255, 228))
    label = "ERROR" if is_error else "OUTPUT"
    tracked(d, (box[0] + 36, box[1] + 30), label, font("bold", 21), C["coral"] if is_error else C["mint"], 3.2)
    focus = set(v.get("out_highlight", []))
    if is_error:
        lines = real_traceback(chapter, v["file"], (chapter / v["error"]).read_text(encoding="utf-8").strip())
        focus = {k if k > 0 else len(lines) + 1 + k for k in focus}
        keys = {f"line {n}" for n in v.get("err_highlight", [])}
        body = [(ln, C["coral"] if i == len(lines) - 1 else C["ink"],
                 any(f"{k}," in ln or ln.rstrip().endswith(k) for k in keys) or (i + 1) in focus)
                for i, ln in enumerate(lines)]
    elif v.get("output"):
        text = (chapter / v["output"]).read_text(encoding="utf-8").rstrip("\n").split("\n")
        body = [(ln, C["ink"], i + 1 in focus) for i, ln in enumerate(text[: int(v.get("out_lines") or len(text))])]
    else:
        msg = v.get("hidden_text", "Predict the output, then run it.")
        d.text(((box[0] + box[2]) // 2, (box[1] + box[3]) // 2 - 50), "?", font=font("head", 120),
               fill=mix(C["sky"], C["white"], 0.45), anchor="mm")
        draw_rich(d, box[0] + 40, (box[1] + box[3]) // 2 + 40, msg, 30, box[2] - box[0] - 80, C["muted"],
                  align="center")
        return
    width = box[2] - box[0] - 110
    osize = 32
    floor = 25 if is_error else 16
    while True:
        chars = max(10, int(width / (osize * 0.6)))
        rows = [(seg, col, lit) for ln, col, lit in body for seg in (wrap_plain(ln, chars) if is_error else [ln])]
        longest = max((len(r[0]) for r in rows), default=1)
        if (len(rows) * osize * 1.55 <= box[3] - box[1] - 100 and (is_error or longest <= chars)) or osize <= floor:
            break
        osize -= 1
    mono = font("mono", osize)
    any_lit = any(lit for _, _, lit in rows)
    y = box[1] + 84
    for ln, col, lit in rows:
        if lit:
            d.rounded_rectangle([box[0] + 14, y - 6, box[2] - 14, y + osize * 1.34], radius=8, fill=C["sky_soft"])
            d.rounded_rectangle([box[0] + 14, y - 6, box[0] + 21, y + osize * 1.34], radius=3, fill=C["sky"])
            d.text((box[2] - 30, y + osize * 0.62), "◀", font=font("sym", int(osize * 0.7)), fill=C["sky_deep"],
                   anchor="rm")
        shade = col if (lit or not any_lit) else mix(col, C["white"], 0.55)
        d.text((box[0] + 38, y), ln, font=mono, fill=shade)
        y += int(osize * 1.55)


# ---------------------------------------------------------------- slide layouts

LEFT_W = 600                     # heading column width in two-column layouts


def two_column(fr: "Frame", v: dict, default_label: str = "") -> tuple[list[int], int]:
    """Heading column on the left; returns the card box on the right."""
    heading_block(fr, X0, 150, LEFT_W - 40, v.get("heading", ""), v.get("label", default_label), size=54)
    return [X0 + LEFT_W, 110, X1, FOOT_Y - 60], 0


def left_ask(fr: "Frame", ask: dict, top: int = 380) -> None:
    """On two-column screens the question sits in the heading column, so the content never moves."""
    ask_card(fr, [X0, top, X0 + LEFT_W - 50, FOOT_Y - 50], ask)


def draw_bullets(fr: "Frame", v: dict, ask: dict | None) -> None:
    heading_block(fr, X0, 150, LEFT_W - 40, v.get("heading", ""), v.get("label", ""), size=54,
                  max_lines=2 if ask else 3)
    items = v["items"]
    reveal = v.get("reveal", len(items))
    focus = v.get("focus", reveal - 1 if reveal < len(items) else None)
    bx0, bx1, area_top, area_bottom = X0 + LEFT_W, X1, 100, FOOT_Y - 60
    inner = bx1 - bx0 - 150
    size = 40
    while size > 28 and sum(rich_height(i, size, inner) + 38 for i in items) + 90 > area_bottom - area_top:
        size -= 2
    total = sum(rich_height(i, size, inner) + 38 for i in items) + 90
    by0 = settle(area_top, area_bottom, total, 0.45)
    card(fr.img, [bx0, by0, bx1, by0 + total], radius=30)
    y = by0 + 52
    for i, item in enumerate(items):
        h = rich_height(item, size, inner)
        if i < reveal:
            lit = focus == i
            if lit:
                fr.d.rounded_rectangle([bx0 + 26, y - 14, bx1 - 26, y + h + 4], radius=16, fill=C["sand_soft"])
            num_fill = C["sky"] if (lit or focus is None) else mix(C["sky"], C["white"], 0.5)
            fr.d.ellipse([bx0 + 46, y + 2, bx0 + 90, y + 46], fill=num_fill)
            fr.d.text((bx0 + 68, y + 24), str(i + 1), font=font("head", 22), fill=C["white"], anchor="mm")
            colour = C["ink"] if (lit or focus is None) else C["muted"]
            draw_rich(fr.d, bx0 + 116, y, item, size, inner, colour)
        y += h + 38
    if ask:
        left_ask(fr, ask)


def draw_table(fr: "Frame", v: dict, ask: dict | None) -> None:
    d = fr.d
    top = heading_block(fr, X0, 96, X1 - X0, v.get("heading", ""), v.get("label", ""), size=50, max_lines=1)
    cols, rows = v.get("columns", []), v["rows"]
    reserve = v.get("_ask_layout") == "strip"
    bottom = 790 if reserve else FOOT_Y - 60
    plain = lambda s: re.sub(r"[`*]", "", str(s))  # noqa: E731
    weights = [min(40, max(len(plain(c)), *(len(plain(r[i])) for r in rows))) + 8 for i, c in enumerate(cols)]
    tw = X1 - X0
    widths = [int((tw - 80) * w / sum(weights)) for w in weights]
    size = 36
    while size > 26:
        heights = [max(rich_height(str(c), size, widths[i] - 40, "bold" if r == 0 else "sans") for i, c in
                       enumerate(row)) + (38 if size > 30 else 30) for r, row in enumerate([cols] + rows)]
        if sum(heights) + 60 <= bottom - top:
            break
        size -= 2
    total = sum(heights) + 40
    y0 = settle(top, bottom, total, 0.35)
    card(fr.img, [X0, y0, X1, y0 + total], radius=28)
    y = y0 + 20
    focus = v.get("focus_row")
    for r, row in enumerate([cols] + rows):
        h = heights[r]
        lit = focus is not None and r == focus + 1
        if lit:
            d.rounded_rectangle([X0 + 16, y + 2, X1 - 16, y + h - 2], radius=14, fill=C["sand_soft"])
            d.rounded_rectangle([X0 + 16, y + 2, X0 + 23, y + h - 2], radius=3, fill=C["amber"])
        x = X0 + 40
        for i, cell in enumerate(row):
            if r == 0:
                tracked(d, (x, y + 22), plain(cell).upper(), font("bold", 20), C["sky_deep"], 2.6)
            else:
                dim = focus is not None and not lit
                draw_rich(d, x, y + 19, str(cell), size, widths[i] - 40, C["muted"] if dim else C["ink"])
            x += widths[i]
        if r < len(rows):
            d.line([X0 + 40, y + h, X1 - 40, y + h], fill="#E1E7EE", width=2)
        y += h
    if ask:
        ask_strip(fr, ask, 820)


def draw_text(fr: "Frame", v: dict, ask: dict | None) -> None:
    d = fr.d
    top = heading_block(fr, X0, 96, X1 - X0, v.get("heading", ""), v.get("label", ""), size=50, max_lines=1)
    body = v.get("body", [])
    body = [body] if isinstance(body, str) else body
    y = top
    for para in body:
        y = draw_rich(d, X0, y, para, 36, X1 - X0, C["ink"]) + 14
    if v.get("pre"):
        lines = v["pre"].split("\n")
        size = 34
        while size > 18 and (len(lines) * size * 1.45 + 90 > FOOT_Y - 70 - y or
                             max(len(x) for x in lines) * size * 0.6 > X1 - X0 - 160):
            size -= 1
        bw = max(len(x) for x in lines) * size * 0.6 + 140
        bh = len(lines) * size * 1.45 + 80
        bx = (W - bw) / 2
        by = settle(y + 10, FOOT_Y - 60, bh, 0.35)
        lit = v.get("focus") == "pre"
        card(fr.img, [bx, by, bx + bw, by + bh], radius=28,
             fill=hexa(C["sand_soft"], 240) if lit else (255, 255, 255, 215),
             outline=hexa(C["amber"]) if lit else (255, 255, 255, 230), width=4 if lit else 2)
        yy = by + 40
        for line in lines:
            d.text((bx + 70, yy), line, font=font("mono", size), fill=C["navy"])
            yy += int(size * 1.45)
    if ask:
        ask_strip(fr, ask)


def draw_prompt(fr: "Frame", v: dict, ask: dict | None) -> None:
    d = fr.d
    box, _ = two_column(fr, v, "AI prompt card")
    if v.get("label"):
        f = font("bold", 24)
        w = f.getlength(v["label"].upper()) + 3 * len(v["label"]) + 48
        d.rounded_rectangle([X0, 560, X0 + w, 608], radius=24, fill=C["sky"])
        tracked(d, (X0 + 24, 571), v["label"].upper(), f, C["white"], 3)
    text = v["prompt"]
    focus = v.get("focus")
    parts = re.split(r"(?<=[.!?])\s+", text)
    inner = box[2] - box[0] - 150
    card(fr.img, box, radius=30)
    d.text((box[0] + 44, box[1] + 18), "“", font=font("head", 120), fill=C["sky_tile"])
    y = box[1] + 120
    for i, part in enumerate(parts):
        lit = focus == i
        h = rich_height(part, 34, inner)
        if lit:
            d.rounded_rectangle([box[0] + 70, y - 10, box[2] - 40, y + h + 2], radius=14, fill=C["sand_soft"])
        draw_rich(d, box[0] + 96, y, part, 34, inner, C["ink"] if (lit or focus is None or focus == "check")
                  else C["muted"])
        y += h + 14
    if v.get("check"):
        y = max(y + 20, box[3] - 190)
        lit = focus == "check"
        d.rounded_rectangle([box[0] + 40, y, box[2] - 40, box[3] - 40], radius=20,
                            fill=C["mint_soft"] if lit else "#EEF2F6")
        tracked(d, (box[0] + 74, y + 22), "CHECK IT", font("bold", 20), C["mint"], 3)
        draw_rich(d, box[0] + 74, y + 56, v["check"], 30, box[2] - box[0] - 150, C["ink"] if lit else C["muted"])
    if ask:
        left_ask(fr, ask, 640)


def draw_title(fr: "Frame", v: dict) -> None:
    d = fr.d
    # left: text block; right: a large chapter tile card
    kicker(d, X0, 250, v.get("kicker", ""))
    size = 76
    width = 980
    while size > 48 and len(layout_rich(v.get("title", ""), size, width, "head", True)) > 3:
        size -= 2
    y = draw_rich(d, X0, 296, v.get("title", ""), size, width, C["navy"], base="head", upper=True, gap=1.1)
    d.rounded_rectangle([X0, y + 20, X0 + 96, y + 28], radius=4, fill=C["sky"])
    y += 70
    if v.get("subtitle"):
        y = draw_rich(d, X0, y, v["subtitle"], 34, width, C["muted"]) + 20
    if v.get("badge"):
        f = font("bold", 26)
        w = f.getlength(v["badge"]) + 60
        card(fr.img, [X0, y + 10, X0 + w, y + 76], radius=33, fill=(255, 255, 255, 230), shadow=26)
        d.text((X0 + 30, y + 43), v["badge"], font=f, fill=C["sky_deep"], anchor="lm")
    bx0, by0, bx1, by1 = 1260, 210, X1, 830
    card(fr.img, [bx0, by0, bx1, by1], radius=40, fill=(255, 255, 255, 170))
    number = f"{int(v.get('tile', fr.ctx['number'])):02d}"
    d.text(((bx0 + bx1) // 2, (by0 + by1) // 2 - 30), number, font=font("head", 260), fill=C["sky_tile"], anchor="mm")
    tracked(d, ((bx0 + bx1) / 2, by1 - 110), fr.ctx["language"].upper(), font("bold", 26), C["sky_deep"], 6, True)


def draw_pause(fr: "Frame", v: dict, ask: dict | None) -> None:
    d = fr.d
    question = ask["question"] if ask else v["question"]
    bw, bh = 1300, 620
    bx, by = (W - bw) // 2, 150
    card(fr.img, [bx, by, bx + bw, by + bh], radius=40, fill=(255, 255, 255, 225))
    tracked(d, (W / 2, by + 60), "PAUSE AND THINK", font("bold", 24), C["sky_deep"], 4, True)
    size = 56
    while size > 34 and rich_height(question, size, bw - 200, "headsb") > 280:
        size -= 2
    qh = rich_height(question, size, bw - 200, "headsb")
    y = by + 120 + max(0, (300 - qh) // 2)
    draw_rich(d, bx + 100, y, question, size, bw - 200, C["navy"], base="headsb", gap=1.25, align="center")
    if v.get("hint"):
        draw_rich(d, bx + 100, by + 440, f"Hint: {v['hint']}", 30, bw - 200, C["muted"], align="center")
    if ask:
        timer(fr, W // 2, by + bh - 70, ask, 1.05)


def draw_quiz(fr: "Frame", v: dict, ask: dict | None) -> None:
    d = fr.d
    kicker(d, X0, 150, "Quick check")
    draw_rich(d, X0, 196, v["question"], 42, LEFT_W + 60, C["navy"], base="headsb", gap=1.28)
    if ask:
        timer(fr, X0 + 170, 740, ask, 1.0)
    revealed = v.get("revealed")
    opts = v["options"]
    gx0, gx1, gy0 = X0 + LEFT_W + 120, X1, 130
    cols = 2 if len(opts) == 4 else 1
    cw = (gx1 - gx0 - (24 if cols == 2 else 0)) // cols
    ch = 200 if cols == 2 else 170
    for i, opt in enumerate(opts):
        r, c = divmod(i, cols)
        x, y = gx0 + c * (cw + 24), gy0 + r * (ch + 26)
        right = revealed and i == v["answer"]
        wrong = revealed and i != v["answer"]
        card(fr.img, [x, y, x + cw, y + ch], radius=26,
             fill=hexa(C["mint_soft"], 245) if right else ((255, 255, 255, 150) if wrong else (255, 255, 255, 225)),
             outline=hexa(C["mint"]) if right else (255, 255, 255, 230), width=4 if right else 2,
             shadow=20 if wrong else 38)
        bubble = C["mint"] if right else (C["faint"] if wrong else C["sky"])
        d.ellipse([x + 30, y + 30, x + 84, y + 84], fill=bubble)
        d.text((x + 57, y + 57), "ABCD"[i], font=font("head", 28), fill=C["white"], anchor="mm")
        draw_rich(d, x + 30, y + 104, opt, 32 if cols == 2 else 34, cw - 60, C["muted"] if wrong else C["ink"],
                  base="medium")
        if right:
            d.text((x + cw - 50, y + 57), "✔", font=font("sym", 44), fill=C["mint"], anchor="mm")
    if revealed and v.get("explain"):
        rows = (len(opts) + cols - 1) // cols
        y = gy0 + rows * (ch + 26) + 10
        draw_rich(d, gx0, y, "**Why:** " + v["explain"], 30, gx1 - gx0, C["ink"])


def draw_breather(fr: "Frame", v: dict, section: str) -> None:
    d = fr.d
    tracked(d, (W / 2, 140), v.get("label", "BREATHER").upper(), font("bold", 24), C["sky_deep"], 5, True)
    title = v.get("title", "Take a breath")
    d.text((W // 2, 220), title.upper(), font=font("head", 72), fill=C["navy"], anchor="mm")
    d.text((W // 2, 300), "Here is what you know so far.", font=font("sans", 32), fill=C["muted"], anchor="mm")
    items = v["items"]
    n = len(items)
    gap = 34
    cw = (X1 - X0 - gap * (n - 1)) // n
    for i, item in enumerate(items):
        x = X0 + i * (cw + gap)
        card(fr.img, [x, 380, x + cw, 660], radius=30, fill=(255, 255, 255, 215))
        d.ellipse([x + 36, 416, x + 92, 472], fill=C["sky"])
        d.text((x + 64, 444), "✔", font=font("sym", 28), fill=C["white"], anchor="mm")
        draw_rich(d, x + 36, 500, item, 32, cw - 72, C["ink"], base="medium")
    # progress track of the chapter sections
    sections = fr.ctx["sections"]
    done = sections.index(section) if section in sections else -1
    tx0, tx1, ty = X0 + 40, X1 - 40, 800
    d.line([tx0, ty, tx1, ty], fill="#C8D3E0", width=4)
    step = (tx1 - tx0) / (len(sections) - 1)
    d.line([tx0, ty, tx0 + step * max(done, 0), ty], fill=C["sky"], width=6)
    for i, name in enumerate(sections):
        cx = tx0 + i * step
        reached = i <= done
        r = 16 if i == done else 11
        d.ellipse([cx - r, ty - r, cx + r, ty + r], fill=C["sky"] if reached else C["white"],
                  outline=C["sky"] if reached else "#B5C2D2", width=3)
        if i == done or i in (0, len(sections) - 1):
            d.text((cx, ty + 44), name, font=font("bold" if i == done else "sans", 24),
                   fill=C["navy"] if i == done else C["muted"], anchor="mm")
    tracked(d, (W / 2, 900), "YOU ARE HERE", font("bold", 18), C["faint"], 4, True)


def draw_end(fr: "Frame", v: dict) -> None:
    draw_title(fr, v)


AI_STAGES = ["Plan", "Write", "Generate", "Test", "Debug", "Improve"]   # the order the story uses them


def _code_block_lines(chapter: Path, rel: str, only: list[int] | None = None):
    """Numbered code lines; `only` keeps the listed line numbers (an excerpt with its real numbers)."""
    src = chapter / rel
    lines = list(enumerate(token_colours(src, src.read_text(encoding="utf-8").rstrip("\n")), start=1))
    return [(n, ln) for n, ln in lines if not only or n in only]


def _message_height(chapter: Path, m: dict, width: int, size: int) -> int:
    h = 44
    if m.get("text"):
        h += sum(rich_height(par, size, width) for par in m["text"].split("\n"))
    if m.get("code"):
        h += len(_code_block_lines(chapter, m["code"], m.get("code_lines"))) * int(size * 1.35) + 44
    if m.get("error"):
        lines = chat_error_lines(chapter, m)
        h += len(wrap_lines(lines, int(width / (size * 0.85 * 0.6)))) * int(size * 1.3) + 40
    if m.get("output"):
        h += len((chapter / m["output"]).read_text(encoding="utf-8").rstrip("\n").split("\n")) * int(size * 1.35) + 40
    if m["role"] == "ai":
        h += 40
    return h


def chat_error_lines(chapter: Path, m: dict) -> list[str]:
    """The error report a learner pastes: from the Traceback line on (the program's own output is left out)."""
    lines = real_traceback(chapter, m["file"], (chapter / m["error"]).read_text(encoding="utf-8").strip())
    for i, ln in enumerate(lines):
        if ln.startswith("Traceback") or ln.lstrip().startswith("File "):
            return lines[i:]
    return lines


def wrap_lines(lines: list[str], chars: int) -> list[str]:
    return [seg for ln in lines for seg in wrap_plain(ln, chars)]


def draw_message(fr: "Frame", chapter: Path, m: dict, x0: int, y: int, x1: int, size: int, lit: bool) -> int:
    d = fr.d
    ai = m["role"] == "ai"
    full = x1 - x0
    bw = int(full * (0.86 if ai else 0.78))
    bx0 = x0 + 64 if ai else x1 - bw
    width = bw - 64
    h = _message_height(chapter, m, width, size)
    fill = (255, 255, 255, 250) if ai else hexa(C["sky_soft"], 250)
    outline = hexa(C["amber"]) if lit else ((226, 233, 241, 255) if ai else hexa(C["sky_soft"]))
    card(fr.img, [bx0, y, bx0 + bw, y + h], radius=24, fill=fill, outline=outline, shadow=22, width=3 if lit else 2)
    if ai:
        d.ellipse([x0, y + 4, x0 + 48, y + 52], fill=C["navy"])
        d.text((x0 + 24, y + 28), "AI", font=font("head", 18), fill=C["white"], anchor="mm")
    else:
        tracked(d, (bx0 + 32, y - 30), "YOU", font("bold", 17), C["sky_deep"], 2.5)
    yy = y + 22
    if m.get("text"):
        for par in m["text"].split("\n"):
            yy = draw_rich(d, bx0 + 32, yy, par, size, width, C["ink"])
    if m.get("code"):
        lines = _code_block_lines(chapter, m["code"], m.get("code_lines"))
        longest = max((sum(len(p) for p, _ in ln) for _, ln in lines), default=1) + 5
        csize = min(size * 0.9, (width - 40) / (longest * 0.6))
        bh = len(lines) * int(size * 1.35) + 30
        d.rounded_rectangle([bx0 + 32, yy + 8, bx0 + 32 + width, yy + 8 + bh], radius=12, fill=C["code_bg"])
        ty = yy + 22
        mono = font("mono", int(csize))
        for n, line in lines:
            d.text((bx0 + 50, ty), f"{n:>2}", font=mono, fill=C["gutter"])
            x = bx0 + 50 + mono.getlength("00  ")
            for piece, colour in line:
                d.text((x, ty), piece, font=mono, fill=colour)
                x += mono.getlength(piece)
            ty += int(size * 1.35)
        yy += bh + 14
    if m.get("error"):
        lines = chat_error_lines(chapter, m)
        chars = int(width / (size * 0.85 * 0.6))
        rows = [(seg, i == len(lines) - 1) for i, ln in enumerate(lines) for seg in wrap_plain(ln, chars)]
        bh = len(rows) * int(size * 1.3) + 28
        d.rounded_rectangle([bx0 + 32, yy + 6, bx0 + 32 + width, yy + 6 + bh], radius=12, fill="#FFFFFF")
        ty = yy + 18
        for r, last in rows:
            d.text((bx0 + 50, ty), r, font=font("mono", int(size * 0.85)), fill=C["coral"] if last else C["muted"])
            ty += int(size * 1.3)
        yy += bh + 12
    if m.get("output"):
        out = (chapter / m["output"]).read_text(encoding="utf-8").rstrip("\n").split("\n")
        bh = len(out) * int(size * 1.35) + 28
        d.rounded_rectangle([bx0 + 32, yy + 6, bx0 + 32 + width, yy + 6 + bh], radius=12, fill="#FFFFFF",
                            outline=hexa(C["mint"]), width=2)
        ty = yy + 20
        for ln in out:
            d.text((bx0 + 52, ty), ln, font=font("mono", int(size * 0.9)), fill=C["ink"])
            ty += int(size * 1.35)
        yy += bh + 12
    if ai:
        d.text((bx0 + 32, y + h - 38), "Example answer. Real AI answers vary.", font=font("medium", 22), fill=C["muted"])
    return y + h + 46


def draw_chat(fr: "Frame", chapter: Path, v: dict, ask: dict | None) -> None:
    d = fr.d
    stage = v.get("stage")
    label = f"Work with AI  \u00b7  stage {stage} of 6" if stage else v.get("label", "Work with AI")
    y = heading_block(fr, X0, 140, LEFT_W - 40, v.get("heading", ""), label, size=52, max_lines=3)
    if ask:
        left_ask(fr, ask, max(420, y))
    elif stage:
        for i, name in enumerate(AI_STAGES, start=1):
            cur, done = i == stage, i < stage
            fill = C["sky"] if cur else (C["sky_soft"] if done else C["white"])
            d.rounded_rectangle([X0, y, X0 + 300, y + 54], radius=27, fill=fill,
                                outline=C["sky"] if (cur or done) else "#D5DEE8", width=2)
            d.text((X0 + 26, y + 27), f"{i}", font=font("head", 22), fill=C["white"] if cur else C["sky_deep"],
                   anchor="lm")
            d.text((X0 + 62, y + 27), name, font=font("bold" if cur else "medium", 26),
                   fill=C["white"] if cur else (C["ink"] if done else C["muted"]), anchor="lm")
            if done:
                d.text((X0 + 270, y + 27), "\u2714", font=font("sym", 20), fill=C["sky_deep"], anchor="mm")
            y += 66
    box = [X0 + LEFT_W, 96, X1, FOOT_Y - 50]
    card(fr.img, box, radius=32, fill=(255, 255, 255, 150), shadow=18)
    msgs = v["messages"][: v.get("reveal", len(v["messages"]))]
    focus = v.get("focus")
    x0, x1 = box[0] + 36, box[2] - 36
    avail = box[3] - box[1] - 70
    size = 30
    first = 0
    def total(sz, start):
        return sum(_message_height(chapter, m, int((x1 - x0) * (0.86 if m["role"] == "ai" else 0.78)) - 64, sz) + 46
                   for m in msgs[start:])
    while size > 21 and total(size, 0) > avail:
        size -= 1
    while first < len(msgs) - 1 and total(size, first) > avail:
        first += 1                     # older messages scroll off the top, like a real chat
    y = box[1] + 52
    for i in range(first, len(msgs)):
        y = draw_message(fr, chapter, msgs[i], x0, y, x1, size, focus == i)


# ---------------------------------------------------------------- entry point

def render_state(ctx: dict, chapter: Path, section: str, v: dict, ask: dict | None, progress: float) -> Image.Image:
    kind = v["type"]
    bg = {"breather": "breather", "pause": "pause"}.get(kind, "base")
    fr = Frame(ctx, section, bg)
    if kind == "code":
        draw_code(fr, chapter, v, ask)
    elif kind == "pause":
        draw_pause(fr, v, ask)
    elif kind == "quiz":
        draw_quiz(fr, v, ask)
    elif kind == "breather":
        draw_breather(fr, v, section)
    elif kind == "table":
        draw_table(fr, v, ask)
    elif kind == "bullets":
        draw_bullets(fr, v, ask)
    elif kind == "text":
        draw_text(fr, v, ask)
    elif kind == "prompt":
        draw_prompt(fr, v, ask)
    elif kind == "chat":
        draw_chat(fr, chapter, v, ask)
    elif kind in ("title", "end"):
        draw_title(fr, v)
    fr.chrome(progress)
    return fr.rgb()
