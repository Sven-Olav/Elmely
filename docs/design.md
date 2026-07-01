# Elmely Energy Monitor

## Design Manual

**Document version:** 1.0  
**Project version:** 0.1.0  
**Last updated:** 2026-07-01

---

# Design Philosophy

Elmely Energy Monitor shall have a modern, clean and professional appearance inspired by:

- Windows 11
- Microsoft Power BI
- TradingView
- Microsoft PowerToys

The application should always prioritize clarity over information density.

---

# Design Principles

...
```text
docs/design.md
```

med følgende innhold.

---

# Elmely Energy Monitor – Design Manual

**Version:** 1.0
**Last updated:** 2026-07-01

---

# Designfilosofi

Elmely Energy Monitor skal ha et moderne, rolig og profesjonelt uttrykk inspirert av:

* Windows 11
* Microsoft Power BI
* TradingView
* Microsoft PowerToys

Programmet skal føles raskt, ryddig og behagelig å bruke over lengre tid.

---

# Designprinsipper

## 1. Informasjon først

Det viktigste skal alltid være synlig uten scrolling.

Brukeren skal kunne se:

* Spotpris
* Totalpris
* Valutakurs
* Vær
* Billigste timer

på ett skjermbilde.

---

## 2. Rolige farger

Vi bruker ikke sterke signalfarger.

Grønn og rød brukes kun for å vise prisnivå.

Resten av programmet skal være nøytralt.

---

## 3. Luft

God avstand mellom elementer.

Minimum:

* 12 px mellom små elementer
* 20 px mellom seksjoner
* 30 px rundt hovedinnhold

---

## 4. Kort

Informasjon vises som kort.

Eksempel:

```
┌────────────────────┐
│ Spotpris           │
│                    │
│ 0,81 DKK           │
└────────────────────┘
```

Alle kort har samme høyde.

---

# Typografi

## Font

**Segoe UI Variable**

Hvis den ikke finnes:

```
Segoe UI
```

Deretter:

```
Arial
```

---

## Størrelser

| Element            | Størrelse |
| ------------------ | --------- |
| Programtittel      | 28 px     |
| Seksjonsoverskrift | 20 px     |
| Korttittel         | 13 px     |
| Tall               | 22 px     |
| Brødtekst          | 11 px     |

---

# Farger

## Primær

```
#1976D2
```

Blå.

---

## Sekundær

```
#26A69A
```

Turkis.

---

## Bakgrunn

Lys:

```
#F5F6F8
```

Mørk:

```
#202124
```

---

## Kort

Lys:

```
#FFFFFF
```

Mørk:

```
#2A2A2A
```

---

## Tekst

Lys:

```
#222222
```

Mørk:

```
#E8E8E8
```

---

# Prisfarger

| Nivå     | Farge |
| -------- | ----- |
| Billigst | 🟢    |
| Lav      | 🟢    |
| Normal   | 🟡    |
| Høy      | 🟠    |
| Dyrest   | 🔴    |

Disse beregnes automatisk ut fra døgnets prisfordeling.

---

# Hjørner

Alle kort:

```
12 px radius
```

Dialoger:

```
16 px radius
```

---

# Skygger

Diskrete.

Ingen kraftige skygger.

---

# Ikoner

Material Symbols.

Ingen blanding av ikonsett.

---

# Navigasjon

Venstremeny.

```
🏠 Oversikt

⚡ Priser

🌤 Vær

📊 Analyse

📅 Historikk

📄 Eksport

⚙ Innstillinger

ℹ Om
```

---

# Statuslinje

Nederst.

Eksempel:

```
Nord Pool ✓

Weather ✓

Exchange ✓

Database ✓

Oppdatert 13:01
```

---

# Grafer

Bruk:

PyQtGraph

Alltid:

* Zoom
* Panorering
* Tooltip

---

# Elmely Price Timeline

Dette er programmets signatur.

24 fargede felter.

```
🟢🟢🟢🟢🟡🟡🟠🟠🔴🔴🔴🟠🟢🟢🟢
```

Hold musepekeren over en time:

```
03–04

Spot

0,41 DKK

Total

1,18 DKK

1,91 NOK

16°C

4 m/s

★★★★★

Billigste time
```

---

# Vinduer

Startstørrelse:

```
1400 × 900
```

Minimum:

```
1200 × 800
```

---

# Splash Screen

Vises ved oppstart.

Maks:

2 sekunder.

---

# Tema

Lys og mørk modus.

Automatisk etter Windows-innstilling.

---

## Jeg har ett forslag til som jeg tror vil gi programmet en tydelig identitet

Jeg synes vi skal ha en liten **"Elmely-blå"** som går igjen overalt.

Ikke mye – bare akkurat nok til at programmet får sitt eget uttrykk.

For eksempel:

* aktivt menypunkt
* lenker
* knapper
* markører i grafer
* fokuserte felter

Jeg foreslår fargen:

```text
#1976D2
```

Den er rolig, moderne og passer godt sammen med både lyst og mørkt tema.

---

### Én siste designregel

Jeg vil gjerne legge til en regel som vi skal følge gjennom hele prosjektet:

> **Hvis en ny funksjon gjør skjermbildet mer rotete, skal vi heller lage en ny visning enn å presse mer informasjon inn på samme side.**

Jeg tror det er en av grunnene til at profesjonelle programmer føles så oversiktlige. Det er en regel jeg ønsker at **Elmely Energy Monitor** skal leve etter fra første versjon. Jeg har stor tro på at det vil gi oss et program som er både kraftig og behagelig å bruke.
