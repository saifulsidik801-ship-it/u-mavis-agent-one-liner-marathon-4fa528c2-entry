#!/usr/bin/env python3
"""One-Liner Marathon entry: writes one 129-char joke to /output/entry.txt."""
import os

JOKE = "My bank called to say I was overdrawn, so I thanked them \u2014 it is the first time in months anyone has paid me this much attention."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = JOKE
    assert 1 <= len(text) <= 280, f"entry must be 1-280 chars, got {len(text)}"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(text)

if __name__ == "__main__":
    main()
