---
Titel: <% tp.file.title %>
Kurs:
Datum: <% tp.date.now("YYYY-MM-DD") %>
Frist:
Status: <% await tp.system.suggester((item) => item, ["nincs elkezdve", "folyamatban", "kész"]) %>
tags:
  - Hausaufgabe
---

# `=this.Titel`

**Kurs:** `=this.Kurs` | **Határidő:** `=this.Frist` | **Státusz:** `=this.Status`

## Feladatok

- [ ] 
- [ ] 

## Megjegyzések

> [!INFO]
> 

---

## Siehe auch

- [[]]

#Hausaufgabe
