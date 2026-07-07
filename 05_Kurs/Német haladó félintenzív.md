---
Kurs: Német haladó félintenzív
Niveau: B1
Lehrerin: Vitez Adrien
Lehrbuch: "[[Menschen B1.pdf]]"
Beginn: 2026-07-06
tags:
  - Kurs
---

# `=this.Kurs`

**Niveau:** `=this.Niveau`
**Lehrerin:** `=this.Lehrerin`
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

- 
