"""
Creates the binary watermark images used in the experiments.

Output folder: ./watermarks/   (values 0 / 255, 255 = white = bit 1)
    watermark_binary_cameraman.png  cameraman watermark, from watermarks/cameraman_source.png
                                    (grayscale photograph, thresholded at 127)
    watermark_binary_random.png     random-bit watermark   (800x800, 32x32 bits, seed 43)
    watermark_binary_text.png       text watermark         (800x800, 32x32 bits, "Digital image authentication 2026")

The main watermark (watermark_binary.png) is the eagle silhouette and is supplied separately.
The pipeline notebook reads watermark_binary.png and watermark_binary_cameraman.png, and generates
the text and random-bit watermarks itself with the same code and seed, so those two files are only
needed for viewing or reuse.

Usage:  python create_watermarks.py
Requires: numpy, pillow
"""
from pathlib import Path
import numpy as np
from PIL import Image

GLOBAL_SEED = 42
OUT = Path("watermarks")
OUT.mkdir(exist_ok=True)
SCALE = 25                      # each of the 32 x 32 bits becomes a 25 x 25 block -> 800 x 800 pixels


def save_bits(bits, name):
    img = (np.asarray(bits, dtype=np.uint8).reshape(32, 32) * 255).astype(np.uint8)
    big = np.kron(img, np.ones((SCALE, SCALE), dtype=np.uint8))
    Image.fromarray(big, mode="L").save(OUT / name)
    print(f"saved {OUT / name}  | {big.shape[1]}x{big.shape[0]} | white bits: {int((img == 255).sum())} of 1024")


# ---- cameraman watermark: grayscale photograph thresholded at 127 ----
photo = np.asarray(Image.open(OUT / "cameraman_source.png").convert("L"))
cameraman = ((photo > 127) * 255).astype(np.uint8)
Image.fromarray(cameraman, mode="L").save(OUT / "watermark_binary_cameraman.png")
print(f"saved {OUT / 'watermark_binary_cameraman.png'}  | {cameraman.shape[1]}x{cameraman.shape[0]} | white pixels: {int((cameraman == 255).sum())}")

# ---- random-bit watermark ----
save_bits(np.random.default_rng(GLOBAL_SEED + 1).integers(0, 2, 1024), "watermark_binary_random.png")


# ---- text watermark (ASCII bits, zero padded to 1024 bits) ----
def text_to_bits(msg, n=1024):
    b = np.unpackbits(np.frombuffer(msg.encode("ascii"), dtype=np.uint8))
    assert b.size <= n, "text too long: max 128 ASCII characters"
    return np.concatenate([b, np.zeros(n - b.size, np.uint8)]).astype(np.uint8)


save_bits(text_to_bits("Digital image authentication 2026"), "watermark_binary_text.png")
