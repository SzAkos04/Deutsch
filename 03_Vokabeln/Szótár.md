```dataview
TABLE Bedeutung AS "Jelentés", Wortart AS "Szófaj", Quelle AS "Forrás"
FROM "03_Vokabeln/Lieder"
WHERE Wortart != null
SORT file.name ASC
```
