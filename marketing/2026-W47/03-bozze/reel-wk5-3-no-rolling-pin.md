# reel-wk5-3-no-rolling-pin

Due varianti dello stesso reel, stesso hook, stessa caption, stesso taglio (sorgente 4,5-28,4 s, 23,9 s):

| Variante | File Instagram | Cover | TikTok |
|---|---|---|---|
| **Con volto** (serve l'ok del pizzaiolo) | `reel-wk5-3-no-rolling-pin.mp4` | `reel-wk5-3-no-rolling-pin-cover.jpg` | `tiktok/reel-wk5-3-no-rolling-pin-no-music.mp4` |
| **Solo mani** (se l'ok non arriva) | `reel-wk5-3-no-rolling-pin-hands-only.mp4` | `reel-wk5-3-no-rolling-pin-hands-only-cover.jpg` | `tiktok/reel-wk5-3-no-rolling-pin-hands-only-no-music.mp4` |

Formato: 1080x1920, H.264 + AAC, 30 fps, 23,9 s. Cover JPG 1080x1920.

- **Giorno e ora previsti**: mercoledi 18 novembre 2026, 10:00 ora di Londra (in Metricool, fuso Europe/Rome: 11:00, o correggere il fuso)
- **Hook (a schermo da 0,0 s a 5,0 s; nella variante solo mani resta per tutto il reel)**: "No rolling pin. Just hands." (giro 1 QC: tolto "Ever.", promessa assoluta non confermata; ora descrive solo cio' che si vede)
- **Stile di hook**: affermazione forte
- **Stile di montaggio**: un solo piano lungo. Nessun taglio: un unico tratto continuo della clip, dalle mani che allargano il panetto al disco pronto sul banco. Solo due scritte brevi in piu': "Lift. Stretch. Slap." (9,5-14,5 s, impasto sollevato e schiaffato) e, sul disco finito, logo + "Stretched by hand, in our trailer." (20,6 s-fine).

### Variante con volto
- Ritaglio 596x1060 della clip 720x1280 (da x 62, y 220), ingrandito a 1080x1920. Il pizzaiolo e' riconoscibile a tratti (di lato, chinato sul banco, e come riflesso nell'acciaio della cappa in alto a destra).
- **Watermark "Insta360 X4"** (sorgente x 60-202, y 188-212, fisso): eliminato dal ritaglio, che parte da y 220. Controllato su prima, meta' e fine.
- Grafica: cartellino color carta (#F3EFE6, 94%) con hook in blu notte Segoe Print Bold e "Just hands." in rosso, come i reel wk3. Testo tra y 290 e y 580: niente nei primi 250 px ne' negli ultimi 350 px.

### Variante solo mani
- Ritaglio stretto 720x720 della sola parte bassa della clip (sorgente y 560-1280: banco, mani, avambracci, impasto), ingrandito a 960x960 e messo in una cornice blu notte con nastro adesivo su fondo carta, come `reel-wk3-1-build-a-boscaiola`. La testa del pizzaiolo nella sorgente non scende mai sotto y ~520, il riflesso nella cappa resta sopra y ~480: entrambi fuori dal ritaglio, e il watermark (y 188-212) pure.
- **Controllo volti**: guardato un fotogramma al secondo (24 fotogrammi, 0-23 s) piu' un ingrandimento della fascia alta del riquadro per ogni secondo, e la sorgente a 2 fotogrammi al secondo: nessun volto ne' riflesso del volto. Si vedono torso, grembiule a righe, avambracci con il tatuaggio: se il pizzaiolo non vuole essere riconoscibile neanche dal tatuaggio, serve un'altra soluzione.
- Grafica: hook in alto a sinistra (y 262-490), logo a destra di "Just hands.", riquadro video y 520-1492, scritte secondarie sotto il riquadro (y 1500-1555, sopra il limite di 1570).
- Nota: tra 16 e 18 s la parte alta dell'impasto lanciato esce dal riquadro per un attimo.

## Caption
No rolling pin on this one, just two hands and a floured counter. A rolling pin squashes the air out; hands push it to the edge, and that's where the crust gets its puff. Lift, stretch, a slap on the counter, repeat, until there's a disc ready for the toppings.

Ever tried stretching dough by hand at home? Tell us how it went.

## Hashtag
#bedford #bedfordfood #pizzadough #handstretched #foodtrailer

## Grezzi usati
- `video 1/WhatsApp Video 2026-11-10 at 22.25.2.mp4`: 4,5-28,4 s (un solo tratto)
- Logo: `foto pizza/logo.jpg` (fondo bianco reso trasparente)
- Cover variante con volto: fotogramma della sorgente a 27,0 s (disco pronto) con l'hook
- Cover variante solo mani: fotogramma a 23,5 s del montato (disco pronto, hook e "Stretched by hand, in our trailer.")

## Audio
**Audio originale rimosso, al suo posto una traccia AAC silenziosa** (48 kHz stereo), in entrambe le varianti. L'audio della clip e' quasi tutto ronzio a bassa frequenza (cappa/ventola, circa -27 dB), con colpi brevi quando l'impasto batte sul banco; ma lo spettrogramma mostra, dentro il tratto montato, armoniche con l'intonazione che sale e scende come una voce (sorgente circa 12,4-13,3 s e 15,5-16,4 s) e un tono fermo intorno a 500 Hz con armoniche (circa 25-27,5 s), forse qualcuno che parla o canticchia. Non potendolo ascoltare, per prudenza e' stato tolto. Nessuna musica: sul PC non ci sono tracce libere da diritti.
- **Versioni TikTok `-no-music`**: identiche byte per byte alle versioni Instagram, audio compreso (tutte silenziose). Il titolare puo' ascoltare l'originale e, se non ci sono voci, chiedere di rimetterlo (il "suono dell'impasto" previsto dal programma), oppure aggiungere un suono dalla libreria commerciale di Instagram/TikTok.

## Da confermare prima della pubblicazione
- **Ok del pizzaiolo a mostrare il volto**: con l'ok si pubblica `reel-wk5-3-no-rolling-pin.mp4`; senza, `reel-wk5-3-no-rolling-pin-hands-only.mp4` (stessa caption).

## Vincoli rispettati
- Nessun orario, prezzo, offerta o affermazione fuori dal config.
