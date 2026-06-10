#!/usr/bin/env python3
"""Assemble MAAE2300 course notes from fragments into a single HTML file."""
import os, glob

REPO = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(REPO, "MAAE2300-notes.html")

CHAPTER_ORDER = [
    "ch1-lec1", "ch1-lec2", "ch1-lec3", "ch1-lec4", "ch1-prob",
    "ch2-notes", "ch2-prob",
    "ch3-notes", "ch3-prob",
    "ch4-notes", "ch4-prob",
    "ch5-notes", "ch5-prob",
    "ch6-notes", "ch6-prob",
    "formulas", "m1prep", "m2prep", "final",
    "lab1", "lab2", "lab3",
    "summary", "progress",
]

def build():
    head = open(os.path.join(REPO, "shell-head.html"), encoding="utf-8").read()
    foot = open(os.path.join(REPO, "shell-foot.html"), encoding="utf-8").read()
    fragments = []
    for name in CHAPTER_ORDER:
        path = os.path.join(REPO, "chapters", f"{name}.html")
        if os.path.exists(path):
            fragments.append(open(path, encoding="utf-8").read())
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(head + "\n")
        f.write('<main class="content-area">\n')
        for frag in fragments:
            f.write(frag + "\n")
        f.write("</main>\n")
        f.write(foot)
    print(f"Built {OUT} ({len(fragments)} fragments)")

if __name__ == "__main__":
    build()
