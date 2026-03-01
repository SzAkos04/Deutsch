> [!LINKS] Wortarten
> - [[#Adjektive|Adjektive]]
> - [[#Adverben|Adverben]]
> - [[#Konjunktionen|Konjunktionen]]
> - [[#Pronomen|Pronomen]]
> - [[#Substantive|Substantive]]
> - [[#Verben|Verben]]


> [!STATS] Wortschatz-Statistik
> - **Substantive:** `$=dv.pages('"03_Vokabeln/Substantive"').length` Stk.
> - **Verben:** `$=dv.pages('"03_Vokabeln/Verben"').length` Stk.
> - **Adjektive:** `$=dv.pages('"03_Vokabeln/Adjektive"').length` Stk.
> - **Insgesamt:** `$=dv.pages('"03_Vokabeln"').length` Vokabeln


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
	file.link AS "Adjektiv",
	Bedeutung AS "Bedeutung",
	Quelle AS "Quelle"
FROM "03_Vokabeln/Adjektive"
WHERE Bedeutung != null
SORT file.name ASC
```

---

## Adverben

```dataview
TABLE WITHOUT ID
	file.link AS "Adverb",
	Bedeutung AS "Bedeutung",
	Quelle AS "Quelle"
FROM "03_Vokabeln/Adverben"
WHERE Bedeutung != null
SORT file.name ASC
```

---

## Konjunktionen

```dataview
TABLE WITHOUT ID
	file.link AS "Konjunktion",
	Bedeutung AS "Bedeutung",
	Quelle AS "Quelle"
FROM "03_Vokabeln/Konjunktionen"
WHERE Bedeutung != null
SORT file.name ASC
```

---

## Pronomen

```dataview
TABLE WITHOUT ID
	file.link AS "Pronomen",
	Bedeutung AS "Bedeutung",
	Quelle AS "Quelle"
FROM "03_Vokabeln/Pronomen"
WHERE Bedeutung != null
SORT file.name ASC
```

---

## Substantive

```dataview
TABLE WITHOUT ID
	(Genus + " " + file.link + choice(Plural, ", " + Plural, "")) AS "Substantiv",
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
	file.link AS "Verb",
	Bedeutung AS "Bedeutung",
	Quelle AS "Quelle"
FROM "03_Vokabeln/Verben"
WHERE Bedeutung != null
SORT file.name ASC
```