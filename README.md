# Dataseksjonens-innedag

Dette repoet inneholder data i .csv format og python scripts som henter dataen. Dataen som ligger i [data mappen](data/) er et forslag til hva som kan visualiseres, dere står fritt til å bruke annen data. 
Hvis dere ønsker annen data fra SSB sitt API eller NAV sine sider, kan dere ta utgangspunkt i python-scriptene som ligger i repoet. 

Repoet inneholder også eksempler på hvordan  visualisere dataen i plotly eller MagicMirror.

## Data
Dataen som ligger i [data mappen](data/) er offentlig data hentet fra SSB sitt API og NAV sine sider.

- [nav_sykemeldte_alle_diagnoser.csv](data/nav_sykemeldte_alle_diagnoser.csv): Totalt nye sykmeldte per uke, tidserie. Les mer [her](https://www.nav.no/no/nav-og-samfunn/statistikk/sykefravar-statistikk/nye-sykmeldte-per-uke).
- [nav_sykemeldte_korona.csv](data/nav_sykemeldte_korona.csv): Antall nye korona relaterte sykmeldte per uke, tidserie. Les mer [her](https://www.nav.no/no/nav-og-samfunn/statistikk/sykefravar-statistikk/nye-sykmeldte-per-uke).
- [ssb_ledige_stillinger.csv](data/ssb_ledige_stillinger.csv): Sesongjustert antall ledige stillinger i det norske arbeidsmarkedet. Ler mer [her](https://www.ssb.no/statbank/table/11587).
- [ssb_sykefravaer.csv](data/ssb_sykefravaer.csv): Sykefraværsprosent, ikke-sesongjustert. Les mer [her](https://www.ssb.no/statbank/table/12439).
- [ssb_fattigdomsproblemer.csv](data/ssb_fattigdomsproblemer.csv): Fattigdomsproblemer, levekårsundersøkelsen. Les mer [her](https://www.ssb.no/statbank/table/12078).


## Python-scripts
Om dere vil bruke annen data fra SSB eller NAV, så kan dere ta utgangspunkt i scriptene som ligger i repoaet for å hente dataen.

> **NB!** 
> 
> Hvis dere ønsker å bruke scriptene for å hente annen data, så trenger dere å erstatte verdiene til variablene **URL** og **QUERY**.
> 
> Scriptene burde også kjøres fra root mappen.

## Visualisere dataen

### MagicMirror

### Python og plotly
