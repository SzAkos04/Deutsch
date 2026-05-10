---
Wort: <% tp.file.title %>
Wortart: Verb
Verbtyp:
  - <% await tp.system.suggester((item) => item, ["stark", "schwach", "gemischt", "modal"]) %>
  - <% await tp.system.suggester((item) => item, ["trennbar", "untrennbar"]) %>
Niveau: <% await tp.system.suggester((item) => item, ["A1", "A2", "B1", "B2", "C1", "C2"]) %>
Bedeutung:
Präteritum:
Partizip_II:
Hilfsverb:
  - <% await tp.system.suggester((item) => item, ["hat", "ist"]) %>
Quelle:
aliases:
---

# `=this.Wort`

## Ungarisch Bedeutung: "`=this.Bedeutung`"

| Infinitiv        | Präteritum             | Partizip II                               |
| ---------------- | ---------------------- | ----------------------------------------- |
| **`=this.Wort`** | **`=this.Präteritum`** | `=this.Hilfsverb` **`=this.Partizip_II`** |

| Personalpronomen | Verb                                         |
| ---------------- | -------------------------------------------- |
| ich              | **<% tp.file.title.replace(/en$/, "e") %>**  |
| du               | **<% tp.file.title.replace(/en$/, "st") %>** |
| er / sie / es    | **<% tp.file.title.replace(/en$/, "t") %>**  |
| wir              | **<% tp.file.title %>**                      |
| ihr              | **<% tp.file.title.replace(/en$/, "t") %>**  |
| sie / Sie        | **<% tp.file.title %>**                      |

> [!INFO]
> 
> **Verbtyp:** `=this.Verbtyp`

---

## Siehe auch

- 

---

`=this.Bedeutung` :: `=this.Wort`, `=this.Präteritum`, `=this.Hilfsverb` `=this.Partizip_II`
<!--SR:!2026-05-25,15,290-->

#Lernkarten 