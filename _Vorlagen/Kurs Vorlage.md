---
Kurs: <% tp.file.title %>
Niveau: <% await tp.system.suggester((item) => item, ["A1", "A2", "B1", "B2", "C1", "C2"]) %>
Lehrer*in:
Lehrbuch:
Beginn: <% tp.date.now("YYYY-MM-DD") %>
tags:
  - Kurs
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

- 
