# Relazione TLN - Mazzei

### Severus Python

## Introduzione
Severus Python è un Dialog System che simula un'interrogazione del corso di pozioni.
Il dialogo che abbiamo cercato di riprodurre si basa
## Diamo un occhiata al codice:

### Classe Frame
Un frame è una struttura dati che utilizziamo per salvare tutti i dati dell'interazione tra l'utente e il sistema di dialogo.
Nello specifico salviamo le seguenti variabili:

* **potions** -> La lista di pozioni
* **student_ingredients** -> La lista degli ingredienti corretti detti da uno studente
* **potion_name** -> Il nome della pozione corrente, oggetto dell'interrogazione
* **student_name** -> Il nome dello studente
* **student_potion_name** -> 
* **add_potions** -> Richiamiamo la funzione add potions che aggiunge la lista delle pozioni al frame
* **mood** -> Indica l'umore del professore

Oltre ai metodi getter e setter, abbiamo altri due metodi:

- **add_potions** -> Va a leggere il file contenente le pozioni (potions.txt) e le aggiunge alla lista di pozioni del frame
- **check_response** -> Prende in input l'ingrediente detto dall'utente e se l'ingrendiente è corretto e non è stato già detto, aggiunge l'ingrediente alla lista degli ingredienti corretti.


## Notes:
Use class.funcion().__doc__ to get the documentation of a function.