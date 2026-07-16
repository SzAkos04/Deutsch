---
tags: [MOC, Grammatik]
---
# 📚 Grammatik MOC — Német haladó félintenzív (B1)

## ⚠️ Gyenge pontok — ide gyakorolj elsőnek
```dataview
LIST
FROM #Grammatik
WHERE Schwäche = true
SORT Thema ASC
```

## 📖 Összes téma kategória szerint
```dataview
TABLE Kategorie, Niveau
FROM #Grammatik
WHERE Kategorie != null
SORT Kategorie ASC, Thema ASC
```

## 📝 Feladatok, amik még hátravannak
```dataview
TASK
FROM #Grammatik OR #Übung
WHERE !completed
```

## 🔗 Kapcsolódás az Unterricht-jegyzetekhez
Ha egy órai jegyzetből ([[2026-07-16]] típusú fájlokból) egy adott témára hivatkozol, mindig az atomi Grammatik-jegyzetre linkelj (pl. `[[Konjunktionen (Wortstellung)]]`), ne a régi `nemet_halado_segedlet#Header` formára — így a link akkor is stabil marad, ha a téma-jegyzet szerkezete változik.

## 🃏 Kártyák / SR
- [[Verbtabellen]] — Präteritum / Perfekt / Konjunktiv II ige alakok

## 🧪 Tesztek
- [[Wiederholungstests]]

---
### Teljes témalista
- [[Nominalisierte Adjektive]]
- [[Präteritum]]
- [[Perfekt]]
- [[Plusquamperfekt]]
- [[Temporale Konjunktionen - während-solange]]
- [[Temporale Konjunktionen - bis]]
- [[Temporale Konjunktionen - als-wenn]]
- [[Temporale Konjunktionen - bevor-ehe]]
- [[Konjunktionen (Wortstellung)]]
- [[Vorgangspassiv]]
- [[Zu + Infinitiv (Grundlagen)]]
- [[Adjektivdeklination]]
- [[Konjunktiv II]]
- [[Relativsatz]]
- [[Partizipien]]
- [[Zu + Infinitiv Konstruktionen]]
- [[Genitivus Partitivus]]
- [[Präpositionen mit Genitiv]]
- [[Wiederholungstests]]
- [[Verbtabellen]]
