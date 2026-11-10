"""
Creates the additional 32x32 binary watermark images used in the experiments.

Output folder: ./watermarks/   (values 0 / 255, 255 = white = bit 1)
    watermark_binary_2.png          second watermark (cat-head silhouette, drawn by the authors)
    watermark_binary_3_random.png   random-bit watermark   (seed 43)
    watermark_binary_4_text.png     text watermark         ("Digital image authentication 2026")
    watermark_binary_5_texture.png  texture watermark      (seed 44)

The main watermark (watermark_binary.png) is the eagle silhouette and is supplied separately.
The pipeline notebook generates the random, text and texture watermarks itself with the same
code and seeds, so these files are only needed for viewing or reuse. The second watermark file
is read by the notebook (section 7.3b).

Usage:  python create_watermarks.py
Requires: numpy, scipy, pillow
"""
from pathlib import Path
import numpy as np
from PIL import Image
from scipy.ndimage import gaussian_filter

GLOBAL_SEED = 42
OUT = Path("watermarks")
OUT.mkdir(exist_ok=True)


def save(bits, name):
    img = (np.asarray(bits, dtype=np.uint8).reshape(32, 32) * 255).astype(np.uint8)
    Image.fromarray(img, mode="L").save(OUT / name)
    print(f"saved {OUT / name}  | white pixels: {int((img == 255).sum())} of 1024")


# ---- second watermark: cat-head silhouette ('#' = black, '.' = white) ----
CAT_HEAD = [
    "................................",
    "................................",
    "................................",
    ".....##..................##.....",
    ".....###................###.....",
    ".....#####............#####.....",
    ".....######.########.######.....",
    ".....######################.....",
    ".....######################.....",
    ".....######################.....",
    ".....######################.....",
    ".....######################.....",
    ".....######################.....",
    "....#######.########.#######....",
    "....######...######...######....",
    "....#####....######....#####....",
    "....#####....######....######...",
    "...######....######....######...",
    "...#######..########..#######...",
    "....########################....",
    "....###########..###########....",
    "....########################....",
    "....########################....",
    ".....######################.....",
    "......#######.#..#########......",
    "......########.##.########......",
    ".......##################.......",
    ".........##############.........",
    "..........############..........",
    "..............####..............",
    "................................",
    "................................",
]
assert len(CAT_HEAD) == 32 and all(len(r) == 32 for r in CAT_HEAD)
cat = np.array([[0 if ch == "#" else 1 for ch in row] for row in CAT_HEAD], dtype=np.uint8)
save(cat, "watermark_binary_2.png")

# ---- random-bit watermark ----
save(np.random.default_rng(GLOBAL_SEED + 1).integers(0, 2, 1024), "watermark_binary_3_random.png")


# ---- text watermark (ASCII bits, zero padded to 1024 bits) ----
def text_to_bits(msg, n=1024):
    b = np.unpackbits(np.frombuffer(msg.encode("ascii"), dtype=np.uint8))
    assert b.size <= n, "text too long: max 128 ASCII characters"
    return np.concatenate([b, np.zeros(n - b.size, np.uint8)]).astype(np.uint8)


save(text_to_bits("Digital image authentication 2026"), "watermark_binary_4_text.png")


# ---- texture watermark (smooth noise, thresholded at the median) ----
def make_texture(seed=GLOBAL_SEED + 2, sigma=1.5):
    f = gaussian_filter(np.random.default_rng(seed).standard_normal((32, 32)), sigma=sigma, mode="wrap")
    return (f > np.median(f)).astype(np.uint8).ravel()


save(make_texture(), "watermark_binary_5_texture.png")
