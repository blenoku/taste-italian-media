---
name: marketing-settimana
description: Mod marketing di Taste Italian. Giro settimanale completo - 5 agenti analizzano la concorrenza, 3 creano il programma, 5 montano i contenuti con hook tutti diversi, 5 controllano la qualita', i finiti vanno in finiti/ e si pubblica solo dopo la conferma del titolare. Usalo per "marketing della settimana", "prepara i contenuti", "/marketing-settimana".
---

# Mod marketing - giro settimanale

Tu sei l'orchestratore. Gli agenti fanno il lavoro, tu assegni, unisci e controlli.
Argomento opzionale: la settimana (es. `2026-W47`). Senza argomento: la prossima settimana, da lunedi a domenica.
Rispondi al titolare in italiano. I contenuti sono in inglese.

Cartella di lavoro: `marketing/<settimana>/` con `01-concorrenza/`, `02-programma/`, `03-bozze/`, `04-qualita/`.
Cartella dei finiti: `finiti/<settimana>/`.

## Fase 0 - Preparazione
1. Leggi `marketing/config.md`.
2. Verifica le due cartelle sorgente (`per claude`, `video 1`). Se un percorso manca o e' vuoto, chiedi al titolare e fermati qui: senza girato non si monta.
3. Scrivi `marketing/<settimana>/inventario.md`: ogni file grezzo con durata, risoluzione e una riga su cosa si vede (guarda i fotogrammi). Segna quelli gia' usati in settimane precedenti.

## Fase 1 - Concorrenza (5 agenti `competitor-scout`, in parallelo)
Uno per concorrente - Peddling Pizza, Dough Boy Pizza, Sud Italia, Italian Touch by Ivano - piu' uno per "tendenze e sintesi".
Output: `01-concorrenza/<nome>.md`. Poi tu scrivi `01-concorrenza/sintesi.md` (una pagina: cosa fanno, cosa manca, 5 opportunita') e salvi nel config i profili trovati.

## Fase 2 - Programma (3 agenti `weekly-planner`, in parallelo)
Angolazioni: prodotto, comunita', tendenze. Output: `02-programma/proposta-<angolazione>.md`.
Chiedi a Metricool gli orari migliori (`getBestTimeToPostByNetwork`) e uniscili tu in `02-programma/programma.md`: un solo calendario, scegliendo il meglio delle tre proposte, senza due contenuti sullo stesso girato o sullo stesso tema.
Nel programma assegna a OGNI contenuto uno stile di hook e uno stile di montaggio (elenchi in `content-editor`), distribuiti in modo che contenuti vicini nel calendario non abbiano mai lo stesso.

## Fase 3 - Montaggio (5 agenti `content-editor`, in parallelo)
Dividi il programma in 5 lotti senza girati in comune. A ogni agente: il suo lotto, i file grezzi, gli stili assegnati.
Output in `03-bozze/`. Poi raccogli tutti gli hook in `03-bozze/hooks-settimana.md` (`settimana | file | hook`) ed esegui
`python3 marketing/tools/check_hooks.py marketing/<settimana>/03-bozze/hooks-settimana.md marketing/hooks-registry.md`.
Se segnala qualcosa, rimanda quei contenuti all'editor prima della fase 4.

## Fase 4 - Qualita' (5 agenti `quality-checker`, in parallelo)
Uno per dimensione: tecnica, hook e testo, unicita', brand e fatti, piattaforma e rischi.
Output: `04-qualita/<dimensione>.md`. Un contenuto e' approvato solo con 5 PASSA su 5.
I bocciati tornano all'editor con le note, poi si ricontrollano solo sulle dimensioni fallite. Massimo 2 giri: quello che non passa resta fuori e lo dici al titolare.

## Fase 5 - Consegna
1. Copia in `finiti/<settimana>/` solo i contenuti approvati (video, cover, `-no-music` in `tiktok/`, schede `.md`).
2. Scrivi `finiti/<settimana>/RIEPILOGO.md`: tabella giorno | ora | file | formato | hook | caption, piu' l'elenco di cio' che e' rimasto fuori e perche'.
3. Fai commit e push sul ramo di lavoro.
4. Mostra il riepilogo al titolare e **fermati**. Chiedi: pubblico tutto, solo alcuni, o cambio qualcosa?

## Fase 6 - Pubblicazione (SOLO dopo conferma esplicita)
Non programmare e non pubblicare nulla finche' il titolare non risponde si' in questa conversazione. Una conferma vale per i contenuti nominati e per questa settimana, non per le successive.
- Instagram: `createScheduledPost` di Metricool, con giorno e ora del programma (fuso del brand). Il file deve avere un URL pubblico: usa il link raw di GitHub dopo il push.
- TikTok: non collegato. Indica al titolare i file in `finiti/<settimana>/tiktok/` da caricare a mano.
- Dopo la programmazione: rileggi i post con `getScheduledPosts`, conferma al titolare cosa e' in calendario e aggiungi gli hook approvati a `marketing/hooks-registry.md`.

## Regole fisse
- Niente inventato: orari, prezzi, offerte e dati sui concorrenti vengono dal config o da una fonte citata.
- Ogni hook e' unico: nella settimana e rispetto al registro.
- Se una fase fallisce o un agente non consegna, dillo nel riepilogo con il motivo. Non sostituire il risultato mancante con uno tuo senza dirlo.
