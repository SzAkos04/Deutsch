---
Kurs: Német középfok félintenzív
Niveau: B2
Lehrer*in: Vitéz Adrienn
Lehrbuch:
Beginn: 2026-10-19
tags:
  - Kurs
  - MOC
---

# `=this.Kurs`

**Niveau:** `=this.Niveau`
**Lehrer*in:** `=this.Lehrer*in`
**Lehrbuch:** `=this.Lehrbuch`
**Beginn:** `=this.Beginn`

---

## 📚 Unterrichtsstunden

```dataview
TABLE Datum, Thema
FROM #Unterricht
WHERE Kurs = this.file.link
SORT Datum ASC
```

## 📝 Hausaufgaben

```dataview
TABLE Datum, Frist, Status
FROM #Hausaufgabe
WHERE Kurs = this.file.link
SORT Frist ASC
```

## 🗂️ Neue Wörter aus diesem Kurs

```dataview
LIST
FROM #Lernkarten
WHERE contains(string(Quelle), this.file.name)
SORT file.name ASC
```

---

## Siehe auch

- [[Wörterbuch]]
- [[Német haladó félintenzív]]
