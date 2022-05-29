# **Relazione Progetto TLN Parte 1 - Mazzei**

# Severus Python

## Introduzione
Severus Python è un Dialog System che simula un'interrogazione ispirata dalla saga di Harry Potter, nello specifico del corso di pozioni, tenuto dal professore Severus Piton.
Lo scopo del sistema è domandare allo studente, che non è altro che l'utente che interagisce con il sitema, quali sono gli ingredienti di una pozione, scelta a caso da una lista di 3 pozioni.

<br>

## Funzionamento di base
Quello che caratterizza il nostro sistema è la rappresentazione dello stato dell'umore del professore, in grado di influenzare il modo in cui
vengono generate le frasi. Nello specifico il sistema risponderà in maniera più fredda e irritata a seconda dell'umore.
All'inizio di ogni simulazione il dialog manager setterà una variabile che rappresenta il numero di tentivi a disposizione dello studente.
Il numero di tentativi si decrementerà di 1 ogni votla che lo studente sbaglierà una risposta, al termine dei tentivi il sistema terminerà la simulazione.
L'umore del professore andrà ad influenzare il numero di tentivi, andandoli a decrementare in modo da rendere l'interrogazione più difficile.

Il sistema andrà a domandare allo studente di elencare uno alla volta gli ingredienti di una pozione. 
Dovrà quindi capire ed estrarre l'ingrediente dalla frase, controllare se è corretto e comunicare allo studente (l'utente) se l'ingrediente inserito è corretto o meno.
La simulazione terminerà quando lo studente avrà detto tutti gli ingredienti della pozione, o quando avrà esaurito i tentativi.
Abbiamo

## Come estraiamo le informazioni dalla frase:
Per trovare le informazioni utili all'interno della frase, come gli ingredienti e il nome dello studente, utilizziamo il `DependecyMatcher` di spacy, grazie alle quali troviamo le relazioni di dipendenza all'interno della frasi.
Abbiamo analizzato un insieme di possibili frasi in input e abbiamo scoperto che le frasi avevano una struttura simile. 
Grazie a questa caratteristica siamo riusciti a capire la dipendenza associata agli ingredienti presenti nella frase e a creare dei pattern in grado di riconoscere gli ingredienti in varie frasi.
Abbiamo generato 11 pattern in grado di riconoscere tutti gli ingredienti presenti nelle 3 pozioni che abbiamo selezionato.


## Le frasi di input:
Abbiamo selezionato un insieme di frasi in input e abbiamo deciso di restringere il dominio del nostro sistema a queste frasi.
La parte difficile, come vedremmo dopo, riguarda proprio il dominio. Infatti abbiamo avuto molti problemi siccome gli ingredienti delle pozioni, 
che appartengono all'universo di Harry Potter, quindi al mondo fantasy, non sono parole che vengono usate tutti i giorni. Questo ha reso particolarmente difficile
l'estrazione delle informazioni dalle frasi. Per risolvere questo problema abbiamo generato dei pattern che riconoscano tutti gli ingredienti delle nostre 3 pozioni.

Le frasi su cui abbiamo lavorato sono:
- X is contained in the potion
- X are contained in the potion
- X is used in the potion
- X are used in the potion
- X is needed in the potion
- X are needed in the potion
- The potion contains X
- The potion uses X
- The potion needs X
- X
- The answer is X

Dove al posto di X ci sono i vari ingredienti della pozione.

Nella file `test.py` abbiamo definito delle funzioni che permettono di testare il corretto funzionamento del sistema.
Nello specifico nella classe `TestSentences` abbiamo testato tutte le possibili combinazioni, ottenendo, per il nostro insieme di ingredinenti e il nostro insieme di frasi,
un accuratezza del 100%. 
In pratica il nostro sistema è sempre in grado di estrarre un ingrediente da una frase se la frase ha la struttura delle frasi sopra citate e, ovviamente, l'ingrediente è presente nella nostra lista di ingredienti.

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
Andiamo a ricercare nella frase il nome utilizzando, come sempre faremo, il `DependecyMatcher` di spacy.
Il sistema di dialogo è quindi in grado di capire se il nome è presente nella frase o meno, anche se la frase contiene altre parole oltre al nome (come ad esempio **"My name is Ron Weasley"**).

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
Questo file contiene i metodi in grado di riconoscere il pattern di una frase, con lo scopo di isolare le informazioni importanti di una frase.
Se la frase soddisfa il pattern in ingresso restituisce la porzione di frase che soddisfa quel pattern.
Visto che gli ingtredienti delle pozioni hanno nomi caratterizzati da più parole ritorniamo sempre la sotto sequenza più lunga perchè altrimenti il sistema di dialogo potrebbe estrarre solamente una parte dell'ingrediente (es. *"The Crisopa"* e non *"The Crisopa Fly"*)

- `get_matched_patterns` -> Data una frase in input, un pattern e il nome del pattern restituisce la porzione di frase che rispetta il pattern. Questo metodo utilizza il `DependecyMatcher` di spacy.
Ritorna la sotto sequenza di parole più lunga trovata nella frase, e se non ha trovato nessuna parola ritorna "No Match". Questo metodo verrà richiamato più volte, testando tutti i pattern.
- `find_pattern_name` -> Utilizzata per trovare il nome dellu studente all'interno di una frase. Il meccanismo è simile a quello di prima. Il meotodo viene richiamato all'inizio della simulazione, 
quando allo studente viene cheisto il nome.
- `test_pattern` -> Questo motodo richiama il metodo `get_matched_patterns` per ogni pattern, e ritorna l'ingrediente che rispetta il pattern più lungo. Se non lo trova ritorna tutta la frase. Questo perchè se non trova un pattern la frase potrebbe contenere solamente l'ingrediente.
- `get_vote` -> Questo metodo ritorna il voto dell'interrogazione. Il voto sarà influenzato dal numero di ingredienti detti dallo studenti sulla base del totale, sul numero di errori commessi e infine, come ogni interrogazione che sis rispetti, dall'umore del professore.


## I limiti del nostro sistema:
 - **Frasi in input:** Il nostro sistema allo stato attuale è in grado di riconoscre gli ingredienti delle 3 pozioni che abbiamo selezionato.
Inolte il sistema si comporta molto bene per le frasi che abbiamo testato, se però in input viene fornita una frase che non abbamo previsto il sistema fallisce nella ricerca dell'ingrediente nella frase.
Questo perchè il `DepenecyMatcher` di spacy non riesce a capire bene la struttura delle frasi che contengono degli ingredienti come quelli delle pozioni dell'universo di Harry Potter.

 - **Frasi in output:** Il nostro sistema genera frasi in output utilizzando la libreria di `simpleNLG`. Questa libreria si è rivelata molto potente per generare frasi in maniera automatica. 
Si potrebbe però estendere il nostro sistema per generare frasi in output in modo da renderlo ancora più parametrico, andando ad estrarre gli elementi delle frasi da una lista di possibili alternative.
Noi ci siamo limitati a generare alcune frasi, che venivano selezionate in base all'umore del professore e allo stato dell'interrogazione.

 - **Audio mode:** Come abbiamo già detto sopra il nostro sistema funziona bene sul testo scritto, mentre sull'input vocale fa molta fatica. 
Questo è portato dal fatto che gli ingredienti delle pozioni non sono parole "reali" visto che appartengono ad dominio Fantasy. 
Inoltre è anche fortemente influenzato dall'ambiente

## Sviluppi futuri:



## Notes:
Use class.funcion().__doc__ to get the documentation of a function.