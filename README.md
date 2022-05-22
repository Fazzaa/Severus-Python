# **Relazione Progetto TLN Parte 1 - Mazzei**

# Severus Python

## Introduzione
Severus Python è un Dialog System che simula un'interrogazione ispirata dalla saga di Harry Potter, nello specifico del corso di pozioni, tenuto appunto dal professore Severus Piton.
Lo scopo del sistema è domandare allo studente, che non è altro che l'utente che interagisce con il sitema, quali sono gli ingredienti di una pozione, scelta a caso da una lista di 3 pozioni.

Quello che caratterizza il nostro sistema è la rappresentazione dello stato dell'umore del professore, in grado cambiare le frasi che vengono generate e rendendo più difficile l'interrogazione dello studente.
Ovviamente anche il voto finale sarà influenzato dall'umore del professore.

<br>

## Funzionamento di base
Il sistema andrà a domandare allo studente di elencare uno alla volta gli ingredienti di una pozione. 
Dovrà quindi capire ed estrarre l'ingrediente dalla frase, controllare se è corretto e comunicare all'utente se l'ingredienti inserito è corretto o no.
La simulazione terminerà quando lo studente avrà detto tutti gli ingredienti della pozione, o quando avrà esaurito i tentativi.

## Come estraiamo le informazioni dalla frase:
Per trovare le informazioni utili all'interno della frase, come gli ingredienti e il nome dello studente, utilizziamo il `DependecyMatcher` di spacy, grazie alle quali troviamo le relazioni di dipendenza all'interno della frasi.
Abbiamo analizzato un insieme di possibili frasi in input e abbiamo scoperto che le frasi avevano una struttura simile. 
Grazie a questo concetto siamo riusciti a capire la dipendeza associata agli ingredienti presenti nella frase.
Abbiamo generato 11 pattern in grado di riconoscere tutti gli ingredienti presenti nelle 3 pozioni che abbiamo selezionato.

<br>

## Come abbiamo strutturato il comportamento del dialog system:
Dovendo simulare il comportamento di un professore come Piton, noto per essere particolarmente scorbutico, le risposte del nostro sistema di dialogo sono guidate dal suo umore, caratterizzato da una variabile `mood`.
La variabile `mood` è una stringa che indica il tipo di umore del professore, 0 rappresenta uno stato di quiete, mentre lo stato 3 rappresenta uno stato di irritazione.
L'umore del professore, come spesso accade anche nel mondo reale, è generato in maniera randomica. Quando irritato sarà molto più secco con le risposte, sopratutto in caso di ettore.
Inoltre più è arrabbiato, meno chance avrà lo studente di sbagliare una risposta.

<br>

## Diamo un occhiata al codice:
<br>

### Classe Main
Nel main simuliamo il funzionamento dell'intero dialogo. 

**Modalità audio**:

Abbiamo implementato anche la possibilità di avere un dialogo verbale con il nostro Dialog System.
Per farlo abbiamo utilizzato il pacchetto `pyttsx3`, grazie alla quale siamo riusciti a riprodurre le frasi dagli speacker del computer e ad inserire le risposte tramite il microfono.

*Problematiche modalità audio:*

- Purtroppo gli ingredienti delle pozioni sono per la maggior parte parole inventate, che il sintetizzatore di google non riesce a capire e ritorna gli ingredienti scritti male.

<br>

**Inizio Interazione**:

Inizia generando un istanza della classe Frame, in cui saranno salvate tutte le informazioni riguardanti l'interazione, come i dettagli della pozione.
La pozione sarà estratta a caso tra una lista di 3 pozioni dal file *potions.txt*.
I dettagli della classe Frame li vedremo dopo.

Una volta selezionata una pozione, l'interazione avrà inizio con la richiesta del nome del partecipante.
Andiamo a ricercare un pattern
### Classe Frame
Un frame è una struttura dati che utilizziamo per salvare tutti i dati dell'interazione tra l'utente e il sistema di dialogo.
Nello specifico salviamo le seguenti variabili:

* `potions` -> La lista di pozioni
* `student_ingridients` -> La lista degli ingredienti corretti detti da uno studente
* `potion_name` -> Il nome della pozione corrente, oggetto dell'interrogazione
* `student_name` -> Il nome dello studente
* `student_potion_name` -> 
* `add_potion` -> Richiamiamo la funzione add potions che aggiunge la lista delle pozioni al frame
* `mood` -> Indica l'umore del professore

Oltre ai metodi getter e setter, abbiamo altri due metodi:

- `add_potions` -> Va a leggere il file contenente le pozioni (potions.txt) e le aggiunge alla lista di pozioni del frame
- `check_response` -> Prende in input l'ingrediente detto dall'utente e se l'ingrendiente è corretto e non è stato già detto, aggiunge l'ingrediente alla lista degli ingredienti corretti.

### Dialogmanagaer
Questo file contiene i metodi in grado di riconoscere il pattern di una frase, con lo scopo di isolare le cose importanti di una frase.
Se la frase xsoddisfa il pattern in ingresso restituisce la porzione di frase che soddisfa quel pattern.

- `get_matched_patterns` -> Data una frase in input, un pattern e il nome del pattern restituisce la porzione di frase che rispetta il pattern. Questo metodo utilizza il ***matcher*** di spacy.

## I limiti del nostro sistema:

## Sviluppi futuri:



## Notes:
Use class.funcion().__doc__ to get the documentation of a function.