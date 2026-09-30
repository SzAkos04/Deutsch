---
Titel: Wörterbuch
tags:
  - Wörterbuch
---
# `=this.Titel`

```dataviewjs
const n = dv.pages('"02_Vokabeln"').where(p => p.Wortart).length;
dv.paragraph(`**Összesen ${n} szó / kifejezés** a \`03_Vokabeln\` mappában.`);
```

## Összesítés szófajok szerint

```dataview
TABLE WITHOUT ID key AS "Szófaj", length(rows) AS "Darab"
FROM "02_Vokabeln"
WHERE Wortart
FLATTEN choice(typeof(Wortart) = "array", choice(contains(Wortart, "Vonzat"), "Vonzatos ige", "Redewendung"), Wortart) AS Art
GROUP BY Art
SORT length(rows) DESC
```

## Összesítés Niveau szerint

```dataview
TABLE WITHOUT ID key AS "Niveau", length(rows) AS "Darab"
FROM "02_Vokabeln"
WHERE Wortart
GROUP BY Niveau
SORT key ASC
```

---

## Substantive

```dataview
TABLE WITHOUT ID file.link AS "Szó", Genus AS "Nem", Plural AS "Plural", Bedeutung AS "Jelentés", regexreplace(string(Quelle), "^.*– ", "") AS "Forrás"
FROM "02_Vokabeln"
WHERE Wortart = "Substantiv"
SORT lower(file.name) ASC
```

## Verben

```dataview
TABLE WITHOUT ID file.link AS "Ige", Präteritum AS "Präteritum", Hilfsverb + " " + Partizip_II AS "Perfekt", join(Verbtyp, ", ") AS "Típus", Bedeutung AS "Jelentés", regexreplace(string(Quelle), "^.*– ", "") AS "Forrás"
FROM "02_Vokabeln"
WHERE Wortart = "Verb"
SORT lower(file.name) ASC
```

## Adjektive

```dataview
TABLE WITHOUT ID file.link AS "Szó", Komparativ AS "Komparativ", Superlativ AS "Superlativ", Bedeutung AS "Jelentés", regexreplace(string(Quelle), "^.*– ", "") AS "Forrás"
FROM "02_Vokabeln"
WHERE Wortart = "Adjektiv"
SORT lower(file.name) ASC
```

## Adverben

```dataview
TABLE WITHOUT ID file.link AS "Szó", Bedeutung AS "Jelentés", regexreplace(string(Quelle), "^.*– ", "") AS "Forrás"
FROM "02_Vokabeln"
WHERE Wortart = "Adverb"
SORT lower(file.name) ASC
```

## Konjunktionen

```dataview
TABLE WITHOUT ID file.link AS "Szó", Bedeutung AS "Jelentés", regexreplace(string(Quelle), "^.*– ", "") AS "Forrás"
FROM "02_Vokabeln"
WHERE Wortart = "Konjunktion"
SORT lower(file.name) ASC
```

## Redewendungen

```dataview
TABLE WITHOUT ID file.link AS "Kifejezés", Bedeutung AS "Jelentés", regexreplace(string(Quelle), "^.*– ", "") AS "Forrás"
FROM "02_Vokabeln"
WHERE typeof(Wortart) = "array" AND contains(Wortart, "Redewendung") AND !contains(Wortart, "Vonzat")
SORT lower(file.name) ASC
```

## Vonzatos igék

```dataview
TABLE WITHOUT ID file.link AS "Szerkezet", Bedeutung AS "Jelentés"
FROM "02_Vokabeln"
WHERE typeof(Wortart) = "array" AND contains(Wortart, "Vonzat")
SORT lower(file.name) ASC
```

---

## Fachwortschatz (mérnöki/KIT-felkészülés, nem kurzus-specifikus)

```dataview
TABLE WITHOUT ID file.link AS "Szó", Wortart AS "Szófaj", Bedeutung AS "Jelentés", regexreplace(string(Quelle), "^.*Fachwortschatz: ", "") AS "Terület"
FROM "02_Vokabeln"
WHERE contains(string(Quelle), "Fachwortschatz")
SORT regexreplace(string(Quelle), "^.*Fachwortschatz: ", "") ASC, lower(file.name) ASC
```

*(Ez a szekció most még üres lesz — amint bekerülnek az első mérnöki/KIT szavak
`Fachwortschatz: <Terület>` jelöléssel a Quelle mezőjükben, itt automatikusan
megjelennek, területenként csoportosítva.)*

---

## Lektion szerint

```dataviewjs
const pages = dv.pages('"02_Vokabeln"').where(p => p.Quelle);
for (let i = 1; i <= 17; i++) {
  const re = new RegExp(`Lektion ${i}(?!\\d)`);
  const list = pages
    .where(p => re.test(String(p.Quelle)))
    .sort(p => p.file.name.toLowerCase());
  if (list.length === 0) continue;
  dv.header(3, `Lektion ${i} (${list.length})`);
  dv.table(
    ["Szó", "Szófaj", "Jelentés"],
    list.map(p => [
      p.file.link,
      Array.isArray(p.Wortart) ? p.Wortart.join(", ") : p.Wortart,
      p.Bedeutung
    ])
  );
}
```

---

## Siehe auch

- [[MOC]]
- [[Német haladó félintenzív]]
