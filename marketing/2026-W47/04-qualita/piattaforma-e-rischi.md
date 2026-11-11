# Controllo qualita' 2026-W47 - dimensione 5: piattaforma e rischi

Controllore: `quality-checker` (piattaforma e rischi), 11/11/2026. Nessun contenuto modificato.
Materiale di lavoro (fogli provini a 1 fotogramma al secondo, spettrogrammi, ritagli): `C:\Users\Utente\AppData\Local\Temp\claude\df28836391b3a17e\53d3c6e3-5ef0-4402-9367-8dd499965d92\scratchpad\qc-rischi\`

## Come ho controllato
- **Audio**: `volumedetect` su tutti i 13 MP4 e sulle 6 versioni `tiktok/*-no-music.mp4`.
- **R4 inside-the-trailer** (`reel-wk5-5-inside-the-trailer.mp4`): `showspectrumpic` dell'intero montato, di ogni segmento montato (0-5,5 / 5,5-8,5 / 8,5-12,5 / 12,5-14,5 s) e del grezzo completo `video 1/WhatsApp Video 2026-11-10 at 21.17.0 6.mp4`.
- **Immagine**: foglio provini a 1 fotogramma al secondo di ogni reel e story, piu' le 13 JPG (6 cover e 7 story); ritagli a piena risoluzione dove c'erano bottiglie, cartelli e il forno.
- **Testi**: caption, hashtag e testi in sovrimpressione di tutte le schede `.md`, cercando anche i nomi dei concorrenti del config (Peddling Pizza, Dough Boy, Sud Italia, Italian Touch by Ivano) e parole come best, number one, authentic, cheapest.

## Risultati audio misurati
| File | mean / max | Esito |
|---|---|---|
| Tutti i reel e le story tranne R4, versioni TikTok comprese | -91,0 / -91,0 dB | silenzio digitale vero: nessuna musica, nessuna voce |
| `reel-wk5-5-inside-the-trailer.mp4` e la sua versione `-no-music` | -16,5 / -1,5 dB | audio originale presente (vedi R4) |

Nota tecnica, non di rischio: la scheda di R4 dice che `tiktok/reel-wk5-5-inside-the-trailer-no-music.mp4` e' una "copia del file", ma l'md5 e' diverso da quello della versione Instagram (049442e1.. contro 578b446c..). I livelli audio sono identici. Va segnalato alla dimensione tecnica.

## Regola hashtag usata
Instagram dal dicembre 2025 accetta **al massimo 5 hashtag** per post o reel (gli altri non vengono pubblicati, oppure il post da' errore). Su TikTok tengo per prudenza lo stesso tetto di 5 (non ho verificato il limite attuale di TikTok). Lunghezza delle caption: tutte tra circa 130 e 310 caratteri, molto sotto i 2.200 di Instagram e i 4.000 di TikTok, quindi vanno bene.

## Verdetti

| Contenuto | Verdetto | Cosa, dove, come correggere |
|---|---|---|
| **R1** `reel-wk5-1-dough-duty` (+ cover, + tiktok) | **NON PASSA** | **Hashtag**: 8 nella scheda (riga `## Hashtag`), oltre il tetto di 5 di Instagram. *Correzione*: tenerne 5, per esempio `#bedford #bedfordfood #foodtrailer #pizzadough #tasteitalian`. Il resto passa: audio a -91 dB (silenzio vero, quindi niente musica con diritti); niente volti (solo mani e avambracci, 0-10 s); sullo sfondo in alto (y 0-250, per tutto il reel) ci sono flaconi di detersivo e un cartello di sicurezza blu, ma nessun marchio leggibile; nessuna targa, nessun telefono; nessuna affermazione da dimostrare. |
| **R2** `reel-wk5-3-no-rolling-pin` (variante **con volto**, + cover, + tiktok) | **NON PASSA (condizionato)** | **Volto del pizzaiolo** riconoscibile di lato nei secondi 1-9 e 15-23, frontale con gli occhiali nei secondi 17-21, e nella cover. **Serve l'ok esplicito del pizzaiolo** (punto 1 di "Da confermare" del programma): senza l'ok non si pubblica questa variante, si usa quella solo mani. **Hashtag**: 7, oltre il tetto di 5. *Correzione*: `#bedford #bedfordfood #pizzadough #handstretched #foodtrailer`. Il resto passa: audio a -91 dB; il watermark Insta360 non si vede; le bottiglie sullo sfondo (spremibottiglie dell'olio, barattoli) non hanno marchi leggibili; nessun cliente. "No rolling pin. Ever." e "not now, not ever" sono una promessa sul metodo di lavoro: il titolare deve confermarla (basso rischio). |
| **R2** `reel-wk5-3-no-rolling-pin-hands-only` (+ cover, + tiktok) | **NON PASSA** (solo per gli hashtag) | Volto: non visibile in nessuno dei 24 fotogrammi al secondo (0-23 s), ne' nella cover. Si vedono il tatuaggio sull'avambraccio e il grembiule a righe: basso rischio, ma il pizzaiolo va avvisato. Audio a -91 dB. **Hashtag**: 7 (stessa scheda di R2). *Correzione*: come sopra, 5 hashtag. Corretti gli hashtag, questa e' la variante sicura. |
| **R3** `reel-wk5-4-rocket-on-pizza` (+ cover, + tiktok) | **NON PASSA** | **Hashtag**: 10, il doppio del tetto. **`#woodfiredpizza`** dichiara la cottura a legna, ma ne' il config ne' il girato lo dimostrano: nel forno di R4 si vede solo una fiamma sul fondo, e un forno di quel tipo puo' andare a gas. *Correzione*: togliere `#woodfiredpizza` a meno che il titolare non confermi la legna, e scendere a 5 hashtag, per esempio `#bedford #bedfordfood #pizzabedford #parmaham #foodtrailer`. Il resto passa: audio a -91 dB; guanti blu e scatola bianca senza marchi altrui; niente volti; caption di circa 230 caratteri. |
| **R4** `reel-wk5-5-inside-the-trailer` (+ cover, + tiktok) | **NON PASSA** | **1. Audio "ripulito" non confermato**: nello spettrogramma del montato ci sono pile di armoniche con l'intonazione che cambia e una durata da sillaba (fondamentale circa 160-200 Hz, armoniche fino a circa 1,6 kHz): **reel 6,4-7,1 s** (grezzo circa 10,1-10,8 s, nel segmento "A QUICK TURN") e **reel 12,8-13,0 s** (grezzo circa 30,2-30,4 s, nel segmento finale rallentato). Lo stesso schema c'e' nei tratti del grezzo che l'editor indica come voci (12,3-16 s, 18,5-20,5 s). L'editor lo aveva visto solo come "traccia debolissima verso 11,7-12,2". Con la normalizzazione a -16 LUFS questi suoni arrivano a circa -24/-30 dBFS, quindi si sentono. Giudizio: **probabile voce, comunque non verificato**. Musica: nessuna (non ci sono linee tonali stabili, solo rumore del forno e colpi della pala). *Correzione*: mettere silenzio o rumore di fondo del forno nei tratti 6,3-7,2 s e 12,7-13,1 s del reel, oppure usare una traccia silenziosa per tutto il reel, oppure far ascoltare il reel al titolare prima di pubblicare. Vale anche per la versione `-no-music`. **2. Hashtag**: 10. *Correzione*: `#bedford #bedfordfood #behindthescenes #pizzaoven #foodtrailer`. **Marchio GOZNEY**: nei 15 fotogrammi del forno (0-13 s) e nei ritagli a piena risoluzione a 2, 4, 10 e 13,6 s non si legge nessuna scritta GOZNEY. Il fregio dentro la bocca del forno (in alto a destra, per esempio a 10 s) non si riesce a leggere. La forma del forno resta riconoscibile, ma mostrare la propria attrezzatura non e' un problema: va bene. Bottiglie sullo sfondo (0-5 s, in alto a destra: una bottiglia verde, un olio): etichette non leggibili, va bene. Niente volti, nessuna targa, nessun telefono. Nella caption "Most people only ever see the box" e "Fired in the trailer, by hand" vanno bene. |
| **R5** `reel-wk5-6-three-ingredients` (+ cover, + tiktok) | **NON PASSA** (solo per gli hashtag) | **Hashtag**: 7. *Correzione*: `#margherita #pizzabedford #bedford #bedfordfood #tasteitalian`. Il resto passa: audio a -91 dB; "FIVE THINGS ON OUR MARGHERITA" corrisponde a quello che si vede (pomodoro, grana, basilico, mozzarella, olio: 2-9 s); nessun marchio sulla bottiglia dell'olio (non si vede nell'inquadratura); niente volti. |
| **S1** `story-wk5-1-mon-no-tomato-sauce` (mp4 + jpg) | **PASSA** | Audio a -91 dB. Foto della pizza nella scatola bianca, senza marchi altrui. Nessun hashtag (va bene per una story). Il sondaggio si aggiunge in app. |
| **S2** `story-wk5-2-tue-closed-today` (mp4 + jpg) | **PASSA** | Audio a -91 dB. Panetti nel contenitore, nessun marchio. Nessun orario. |
| **S3** `story-wk5-3-wed-this-or-that` (mp4 + jpg) | **PASSA** | Audio a -91 dB. Scatole kraft senza stampe di altri. Nessun riferimento ai concorrenti. |
| **S4** `story-wk5-4-thu-porcini-season` (mp4 + jpg) | **PASSA** | Audio a -91 dB. Hashtag facoltativi: 3. Usata `porcini.jpg`, non il vecchio `porcini.mp4` con lo scontrino: nessun prezzo visibile. |
| **S5** `story-wk5-5-fri-veggie-in-the-group` (mp4 + jpg) | **PASSA** | Audio a -91 dB. Hashtag: 2. "Tag them" in una story con lo sticker Mention e' una chiamata all'azione normale (basso rischio di essere trattata come esca per l'interazione). |
| **S6** `story-wk5-6-sat-pizza-duty` (mp4 + jpg) | **PASSA** | Audio a -91 dB. "England v All Blacks" cita le squadre solo come fatto del giorno: non ci sono loghi della RFU o degli All Blacks, ne' grafiche ufficiali, quindi va bene. *Consiglio*: non aggiungere in app sticker, GIF o hashtag ufficiali della partita, e non far pensare a una sponsorizzazione. Orario della partita (14:10) da ricontrollare il giorno prima: e' una questione di fatti, non di rischio di piattaforma. Tavolata senza persone. |
| **S7** `story-wk5-7-sun-stir-up-sunday` (mp4 + jpg) | **PASSA** | Audio a -91 dB: la traccia PCM del `.MOV` non e' stata usata. Si vedono per un attimo un cucchiaio e una mano (0-2 s), ma nessun volto. Hashtag: 2. |

## Controlli trasversali
- **Concorrenti**: non compaiono in nessuna caption, scritta o hashtag (cercati per nome).
- **Clienti riconoscibili**: nessuno in nessun contenuto. L'unica persona e' il pizzaiolo (R2).
- **Targhe e numeri di telefono**: nessuno leggibile nei fotogrammi controllati, ne' nelle cover o nelle JPG.
- **Musica con diritti**: nessuna, in nessun file (11 reel e story su 12 sono in silenzio digitale; R4 ha solo l'audio originale). Se il titolare aggiunge musica in app, deve usare la libreria commerciale (Instagram "Audio" per gli account business, TikTok "Commercial Music Library"): niente brani di tendenza non commerciali.
- **Affermazioni da dimostrare**: `#woodfiredpizza` (R3) e' l'unica. "No rolling pin. Ever." (R2) va bene se il titolare la conferma.

## Cosa serve prima di pubblicare
1. Hashtag a 5 o meno in tutti e 5 i reel (R1, R2 in entrambe le varianti, R3, R4, R5).
2. R4: sistemare o far ascoltare i tratti 6,3-7,2 s e 12,7-13,1 s (probabili voci), anche nella versione TikTok.
3. R3: togliere `#woodfiredpizza`, salvo conferma della cottura a legna.
4. R2: ok del pizzaiolo per la variante con volto. Senza l'ok si pubblica la variante solo mani.

---

## Giro 2 (11/11/2026, solo i 5 reel e le loro versioni TikTok)

Come ho controllato:
- `volumedetect` sui 6 MP4 Instagram e sui 6 `tiktok/*-no-music.mp4`;
- md5 di ogni versione Instagram confrontato con la sua versione TikTok;
- foglio provini a 1 fotogramma al secondo dei reel rifatti o modificati (R2 in entrambe le varianti, R3, R4, R5) e delle 5 cover nuove;
- nuove schede `.md`: caption e hashtag.

Fogli provini in `C:\Users\Utente\AppData\Local\Temp\claude\36832352b5379ea2\53d3c6e3-5ef0-4402-9367-8dd499965d92\scratchpad\qc-rischi-g2\`.

Audio: tutti e 12 i file a **-91,0 / -91,0 dB**, cioe' silenzio digitale vero. Ogni versione `-no-music` ha lo stesso md5 della versione Instagram: sono copie identiche.

| Contenuto | Verdetto | Motivo |
|---|---|---|
| **R1** `reel-wk5-1-dough-duty` (+ tiktok) | **PASSA** | Hashtag ora 5 (`#bedford #bedfordfood #foodtrailer #pizzadough #tasteitalian`). Video invariato rispetto al giro 1 (stesso md5): muto, niente volti, nessun marchio leggibile. |
| **R2** `reel-wk5-3-no-rolling-pin`, variante **con volto** (+ cover, + tiktok) | **PASSA solo con l'ok del pizzaiolo** | Hashtag ora 5. Hook "No rolling pin. Just hands." descrive solo quello che si vede: va bene. Caption "on this one" al posto di "not now, not ever": va bene. Audio muto. **Condizione che resta**: il volto si riconosce nei secondi 1-9 e 15-23 (di fronte nei secondi 19-20) e nella cover. Senza l'ok esplicito del pizzaiolo non si pubblica: si usa la variante solo mani. |
| **R2** `reel-wk5-3-no-rolling-pin-hands-only` (+ cover, + tiktok) | **PASSA** | Hashtag ora 5, audio muto. Nessun volto ne' riflesso nei 24 fotogrammi (0-23 s) e nella cover. Si vedono solo avambracci con il tatuaggio e il grembiule: il pizzaiolo va avvisato, rischio basso. |
| **R3** `reel-wk5-4-rocket-on-pizza` (+ cover, + tiktok) | **PASSA** | `#woodfiredpizza` tolto, hashtag ora 5. Audio muto. Nuova chiusura con logo (24,5-27 s) e logo sulla cover: nessun marchio di altri. Guanti blu e scatola bianca senza stampe. Caption con invito a emoji: va bene. |
| **R4** `reel-wk5-5-inside-the-trailer` (rifatto, 10,0 s, + cover, + tiktok) | **PASSA** | **Audio muto per tutto il reel, misurato: -91,0 dB mean e max**, quindi non ci sono piu' le probabili voci del giro 1. La versione TikTok ora ha lo stesso md5 (copia identica). Hashtag 5. Forno nei secondi 0-6: nessuna scritta GOZNEY leggibile; bottiglie sullo sfondo con etichette illeggibili. Niente volti. Hook e caption senza affermazioni da dimostrare (niente tempo di cottura). |
| **R5** `reel-wk5-6-one-last-thing` (11,8 s, + cover, + tiktok) | **PASSA** | Audio muto (-91 dB). Hashtag 5 (`#margherita #pizzabedford #bedford #bedfordfood #tasteitalian`). Hook "ONE LAST THING: OLIVE OIL" corrisponde al girato (filo d'olio, 0-2,8 s) e al menu. La bottiglia dell'olio non e' inquadrata, quindi nessun marchio. Niente volti. I vecchi file `three-ingredients` non ci sono piu' in `03-bozze/` ne' in `tiktok/`. |

**Esito giro 2**: tutti e 5 i reel passano. Resta una sola condizione: l'ok del pizzaiolo per pubblicare la variante di R2 con il volto; in alternativa si pubblica la variante solo mani, che passa senza condizioni.
