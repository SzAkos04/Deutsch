```dataview
TABLE (choice(Genus, Genus + " ", "") + file.name + choice(Plural, ", " + Plural, "")) AS "Wort", Bedeutung, Quelle
FROM "03_Vokabeln"
WHERE Bedeutung != null
SORT file.name ASC
```
