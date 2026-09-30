#!/usr/bin/env python3
"""
Hozzáadja a "- [[Német haladó félintenzív]]" sort minden .md jegyzet
"## Siehe auch" szekciójához, HA még nincs ott (a link neve alapján
ellenőrzi, tehát kétszer lefuttatva sem duplikál semmit).

Csak a "## Siehe auch" szekciót módosítja — az SR-sort
(<!--SR:...-->), a frontmattert és minden mást érintetlenül hagy.

Használat:
    python3 add_kurs_link.py /eleresi/ut/a/03_Vokabeln
    (vagy akár a teljes Deutsch vault gyökerét megadva, mert
    rekurzívan bejárja az almappákat is)

Ha nem adsz meg útvonalat, az aktuális mappát (".") használja.
"""

import sys
import re
from pathlib import Path

LINK_TEXT = "[[Német haladó félintenzív]]"
HEADING = "## Siehe auch"

# a heading utáni első üres sort keressük, és oda szúrjuk be a linket
# egy új listaelemként — a heading utáni MEGLÉVŐ tartalmat nem bántjuk
HEADING_RE = re.compile(re.escape(HEADING) + r"\n+")


def process_file(path: Path) -> str:
    text = path.read_text(encoding="utf-8")

    m = HEADING_RE.search(text)
    if not m:
        return "skip (nincs 'Siehe auch' szekció)"

    insert_at = m.end()

    # csak a "Siehe auch" szekción belül nézzük, hogy megvan-e már a link
    # (a Quelle frontmatter mezőben ez a link amúgy is szerepel minden
    # fájlban, azt nem szabad összekeverni ezzel a body-szintű linkkel)
    section_end = text.find("\n---", insert_at)
    if section_end == -1:
        section_end = len(text)
    section = text[insert_at:section_end]

    if LINK_TEXT in section:
        return "skip (már megvan)"

    rest = text[insert_at:]
    # ha az eredeti sablon üres helyőrző bullet-je ("- " egyedül a sorban)
    # következik, azt kicseréljük a linkre, nem hagyunk utána üres sort
    empty_bullet_re = re.compile(r"^- ?\n")
    if empty_bullet_re.match(rest):
        rest = empty_bullet_re.sub(f"- {LINK_TEXT}\n", rest, count=1)
    else:
        rest = f"- {LINK_TEXT}\n" + rest

    new_text = text[:insert_at] + rest

    path.write_text(new_text, encoding="utf-8")
    return "updated"


def main():
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    if not root.exists():
        print(f"Nem található: {root}")
        sys.exit(1)

    md_files = list(root.rglob("*.md"))
    if not md_files:
        print(f"Nincs .md fájl itt: {root}")
        sys.exit(0)

    skip_no_section = "skip (nincs 'Siehe auch' szekció)"
    counts = {"updated": 0, "skip (már megvan)": 0, skip_no_section: 0}
    problems = []

    for fp in md_files:
        try:
            result = process_file(fp)
            counts[result] = counts.get(result, 0) + 1
        except Exception as e:
            problems.append((fp, str(e)))

    print(f"Átnézett fájlok: {len(md_files)}")
    print(f"  Frissítve:               {counts['updated']}")
    print(f"  Kihagyva (már megvolt):  {counts['skip (már megvan)']}")
    print(f"  Kihagyva (nincs szekció): {counts[skip_no_section]}")
    if problems:
        print(f"\nHibák ({len(problems)} fájl):")
        for fp, err in problems:
            print(f"  {fp}: {err}")


if __name__ == "__main__":
    main()
