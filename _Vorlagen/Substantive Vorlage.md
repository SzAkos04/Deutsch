---
Wort: <% tp.file.title %>
Wortart: Substantiv
Genus:
Plural:
Bedeutung:
Quelle:
aliases:
---

# `=this.Genus` `=this.Wort`, `=this.Plural`

## Ungarisch Bedeutung: "`=this.Bedeutung`"

| Artikel                                         | Substantiv                                                        | Plural                                                                |
| ----------------------------------------------- | ----------------------------------------------------------------- | --------------------------------------------------------------------- |
| <mark style="background: #ADCCFFA6;">der</mark> | `=choice(this.Genus = "der", "**" + this.Wort + "**", this.Wort)` | `=choice(this.Genus = "der", "**" + this.Plural + "**", this.Plural)` |
| <mark style="background: #FF5582A6;">die</mark> | `=choice(this.Genus = "die", "**" + this.Wort + "**", this.Wort)` | `=choice(this.Genus = "die", "**" + this.Plural + "**", this.Plural)` |
| <mark style="background: #BBFABBA6;">das</mark> | `=choice(this.Genus = "das", "**" + this.Wort + "**", this.Wort)` | `=choice(this.Genus = "das", "**" + this.Plural + "**", this.Plural)` |

> [!INFO]
> 

---

## Siehe auch

- 

---

`=this.Bedeutung` :: `=this.Genus` `=this.Wort`, `=this.Plural`

#Lernkarten 