# Fontos tudnivalók a generált Vokabeln fájlokról (v2)

607 db .md fájl készült a Lektion 1–17 szavaiból (627 sorból 20 lecke-közti
duplikátumot összevontam egyetlen fájlba). A _Vorlagen sablonjaid struktúráját
követi, és a 03_Vokabeln mappát közvetlenül bemásolhatod / összefésülheted a
saját ~/Documents/Deutsch/03_Vokabeln mappáddal.

## Amit ebben a körben javítottam a kéréseid alapján

1. **Spaced Repetition szűrés Lektion szerint**: minden fájl alján a korábbi
   sima `#Lernkarten` helyett beágyazott tag van, pl. `#Lernkarten/Lektion07`.
   Az Obsidian/Dataview a beágyazott tageket hierarchikusan kezeli, tehát a
   Kurs Vorlage meglévő `FROM #Lernkarten` dataview-ja továbbra is mindent
   megtalál — miközben az SR plugin review-indításkor most már alrendszerként
   (subdeck) fel fogja kínálni az egyes leckéket, és csak azt gyakorolhatod.
   Ha egy szó több leckében is előfordult, mindkét/mindhárom tag rajta van
   (pl. `#Lernkarten/Lektion02 #Lernkarten/Lektion03 #Lernkarten/Lektion16`).

2. **Igék magyar jelentése főnévi igenévben**: minden ige Bedeutung mezőjét
   átírtam "-ni" végű alakra (pl. "elalszik" -> "elaludni", "segít" ->
   "segíteni", "kapni, fogadni" stb.).

3. **Duplikátumok összevonva**: ha egy szó több leckében is szerepelt (pl.
   "erledigen" L2/L3/L16, "spannend" L1/L12, "erhalten" L4/L5 stb.), most egy
   fájl van belőle, a Quelle mezőben minden érintett lecke fel van sorolva,
   a különböző jelentések pedig vesszővel/pontosvesszővel összefűzve
   szerepelnek benne.

4. **Sich-es (reflexív) igék**: a "sich" mostantól a fájlnévben ÉS a Wort
   mezőben (a "normális", szótári alakban) is szerepel, nem csak a
   Präteritum/Partizip II oszlopban — pl. `sich verabschieden.md`,
   Wort: "sich verabschieden".

## Amit továbbra is ÉRDEMES átnézned (automatikus becslés)

- **Niveau**: Lektion 1–6 -> A2, 7–12 -> B1, 13–17 -> B2 (durva közelítés)
- **Verbtyp** (stark/schwach/gemischt): egyszerű heurisztikával döntöttem,
  előfordulhat téves besorolás rendhagyó igéknél
- **Adjektiv Komparativ/Superlativ**: szabályos -er/-sten képzéssel, csak
  néhány kivétel (groß, hoch, nah, gut, viel) van külön kezelve — az
  umlautos rendhagyó alakokat (pl. jung->jünger) nem ismeri fel automatikusan
- **"der/die" kettős nemű szavak** (Auszubildende, Angehörige, Beamte,
  Jugendliche, Lockige, Schüchterne, Schlauste): alapból "der"-t állítottam
  be, az Info dobozban jelezve
- A Substantiv/Verb/Adjektiv/Adverb/Konjunktion/Redewendung besorolás néhány
  határesetben (pl. "reich sein an +Dat", "gute Besserung") saját döntésem —
  ha máshogy szeretnéd kategorizálni, könnyen áthelyezhető
