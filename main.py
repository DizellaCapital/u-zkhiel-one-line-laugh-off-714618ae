"""One-Line Laugh-Off — make.fun entry.

A grandmother's voicemail from 2019 still plays on the old Nokia,
telling the narrator to water the plant. The plant has been dead
for four years, and the narrator waters the empty pot anyway —
because it is the only thing they have never disappointed.

The program writes that one line to MAKEFUN_OUTPUT_DIR/entry.txt
(fallback /output/entry.txt), validates the 1-200 character gate,
keeps the text to plain ASCII so bytes equal characters (the
tie-break favours fewer bytes), and verifies the write by reading
it back. Stdlib only.
"""

import os

LINE = "At 6:47 a.m., Grandma's voicemail from 2019 played on the old Nokia, 'water the plant, love,' so I watered the empty pot again; dead four years, and still the only thing I've never disappointed."


def main():
    if not (1 <= len(LINE) <= 200):
        raise ValueError(f"line must be 1-200 characters, got {len(LINE)}")
    if len(LINE.encode("utf-8")) > 200:
        raise ValueError("line must fit 200 bytes (tie-break favours fewer bytes)")
    if "\n" in LINE or LINE.strip() != LINE:
        raise ValueError("line must be a single line with no surrounding whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    assert back == LINE, "read-back mismatch"
    byte_len = len(LINE.encode("utf-8"))
    print(f"wrote {len(LINE)} chars ({byte_len} bytes) to {path}")


if __name__ == "__main__":
    main()
