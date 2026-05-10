---
Wort: <% tp.file.title %>
Wortart: Substantiv
Niveau: <% await tp.system.suggester((item) => item, ["A1", "A2", "B1", "B2", "C1", "C2"]) %>
Genus: <% await tp.system.suggester((item) => item, ["der", "die", "das"]) %>
Plural:
Bedeutung:
Quelle:
aliases:
---

# `=this.Genus` `=this.Wort`, `=this.Plural`

## Ungarisch Bedeutung: "`=this.Bedeutung`"

| Artikel                                         | Substantiv                                   | Plural                                         |
| ----------------------------------------------- | -------------------------------------------- | ---------------------------------------------- |
| <mark style="background: #ADCCFFA6;">der</mark> | `=choice(this.Genus = "der", this.Wort, "")` | `=choice(this.Genus = "der", this.Plural, "")` |
| <mark style="background: #FF5582A6;">die</mark> | `=choice(this.Genus = "die", this.Wort, "")` | `=choice(this.Genus = "die", this.Plural, "")` |
| <mark style="background: #BBFABBA6;">das</mark> | `=choice(this.Genus = "das", this.Wort, "")` | `=choice(this.Genus = "das", this.Plural, "")` |

> [!INFO]
> 
> 

---

## Siehe auch

- 

---

`=this.Bedeutung` :: `=this.Genus` `=this.Wort`, `=this.Plural`
<!--SR:!2026-05-25,15,290-->

#Lernkarten 