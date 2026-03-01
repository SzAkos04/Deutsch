> [!Hehehe]
> - [[#Adjektive|Adjektive]]
> - [[#Adverben|Adverben]]
> - [[#Konjunktionen|Konjunktionen]]
> - 


```dataview
TABLE WITHOUT ID
	(choice(Genus, Genus + " ", "") + file.link + choice(Plural, ", " + Plural, "")) AS "Wort",
	Bedeutung,
	Quelle
FROM "03_Vokabeln"
WHERE Bedeutung != null
SORT file.name ASC
```

---

## Adjektive

```dataview
TABLE WITHOUT ID
	(choice(Genus, Genus + " ", "") + file.link + choice(Plural, ", " + Plural, "")) AS "Wort",
	Bedeutung,
	Quelle
FROM "03_Vokabeln/Adjektive"
WHERE Bedeutung != null
SORT file.name ASC
```

---

## Adverben

```dataview
TABLE WITHOUT ID
	(choice(Genus, Genus + " ", "") + file.link + choice(Plural, ", " + Plural, "")) AS "Wort",
	Bedeutung,
	Quelle
FROM "03_Vokabeln/Adverben"
WHERE Bedeutung != null
SORT file.name ASC
```

---

## Konjunktionen

```dataview
TABLE WITHOUT ID
	(choice(Genus, Genus + " ", "") + file.link + choice(Plural, ", " + Plural, "")) AS "Wort",
	Bedeutung,
	Quelle
FROM "03_Vokabeln/Konjunktionen"
WHERE Bedeutung != null
SORT file.name ASC
```

---

## Pronomen

```dataview
TABLE WITHOUT ID
	(choice(Genus, Genus + " ", "") + file.link + choice(Plural, ", " + Plural, "")) AS "Wort",
	Bedeutung,
	Quelle
FROM "03_Vokabeln/Pronomen"
WHERE Bedeutung != null
SORT file.name ASC
```

---

## Substantive

```dataview
TABLE WITHOUT ID
	(choice(Genus, Genus + " ", "") + file.link + choice(Plural, ", " + Plural, "")) AS "Wort",
	Bedeutung,
	Quelle
FROM "03_Vokabeln/Substantive"
WHERE Bedeutung != null
SORT file.name ASC
```

---

## Verben

```dataview
TABLE WITHOUT ID
	(choice(Genus, Genus + " ", "") + file.link + choice(Plural, ", " + Plural, "")) AS "Wort",
	Bedeutung,
	Quelle
FROM "03_Vokabeln/Verben"
WHERE Bedeutung != null
SORT file.name ASC
```