''' 

Abbiamo già coperto i concetti fondamentali. Tuttavia, ci sono alcuni altri argomenti da valutare e
degli stessi argomenti trattati, approfondire qualche dettaglio.

**differenza tra `f""` (f-string) e `.format()`**.



### ** `.format()`**
'''
laMiaParola4 = "torino {1}, grandezza {0}"
print(laMiaParola4.format(320.000, 45))

'''
Qui usiamo **il metodo `.format()`**, che sostituisce i segnaposto `{}` con i valori dati.

------------

### ** `f-string` (formatted string literals)**
'''
x = True
y = False
print(f"x AND y: {x and y}")

'''
Qui usiamo una **f-string**, che permette di inserire direttamente variabili o espressioni dentro una stringa preceduta da `f`.

---

## **Qual è la differenza principale?**
| Metodo      | Sintassi                            | Caratteristica 
|-------------|-------------------------------------|------------------------------------------------------------------|
| `.format()` | `"Test {0} {1}".format(val1, val2)` | I valori vengono sostituiti nei `{}` specificando l'indice |
| `f-string`  | `f"Test {val1} {val2}"`             | Inserisce direttamente le variabili senza bisogno di `.format()` |

### ** Esempio di confronto**
'''
# Con format()
nome = "Mario"
eta = 30
print("Ciao, mi chiamo {0} e ho {1} anni.".format(nome, eta))

# Con f-string
print(f"Ciao, mi chiamo {nome} e ho {eta} anni.")

'''
**Entrambi producono lo stesso output:**
```
Ciao, mi chiamo Mario e ho 30 anni.
```

---

## **Vantaggi delle f-string**
 **Più leggibili** (niente `{0}`, `{1}`, direttamente variabili)  
 **Più veloci** rispetto a `.format()` (eseguono meno operazioni)  
 **Supportano direttamente espressioni** dentro `{}`:
'''
a = 10
b = 5
print(f"La somma di {a} e {b} è {a + b}.")
# Output: La somma di 10 e 5 è 15.




## **🔹 Conclusione**
'''
- Se usi `.format()`, devi specificare la posizione dei valori nei `{}`.
- Se usi `f-string`, puoi **inserire direttamente** variabili ed espressioni **dentro `{}`**.
- ** Contrariamente alla mia esperienza e a quello che ho visto in giro, le f-string sono più 
     moderne e consigliate** (da Python 3.6+)...quindi usiamole!

 Quindi **questa riga**:
'''
print(f"x AND y: {x and y}")

#è semplicemente un **modo più pulito e veloce** di scrivere:

print("x AND y: {}".format(x and y))
'''


----------------------------------------------------------

Altri argomenti importanti non ancora trattati per Python base...


### ** Liste e comprensioni di lista**
- **Comprensione di lista** (modo più compatto per creare liste)
  ```python
'''
numeri = [x**2 for x in range(5)]
print(numeri)  # Output: [0, 1, 4, 9, 16]
'''

---

### ** Lambda functions (funzioni anonime)**
- **Quando servono funzioni brevi**
  ```python
  doppio = lambda x: x * 2
  print(doppio(5))  # Output: 10
  ```
  
Argomenti solo accennati...

#short hand list comprehension...una sintassi ridotta per le list
[print(citta) for citta in laMiaLista]
print("--")
[print(citta) for citta in laMiaLista if citta != "roma"]
#espressione for item in list if condizione == True   ....la sintassi.....
#fare riferimento alla documentazione per altri casi

-------------------------
In realtà fanno tutte parte delle **"one-liners" in Python**   

---

## ** 1 Short-Hand List Comprehension**  
È una **forma compatta** per creare liste o iterare su di esse in una sola riga.  

### **Esempio:**
```python
[print(citta) for citta in laMiaLista]
```
 **Cosa fa?** Stampa ogni città in `laMiaLista` senza bisogno di un ciclo `for` esplicito.

 **Con condizione (`if`)**:
```python
[print(citta) for citta in laMiaLista if citta != "roma"]
```
 Stampa tutte le città tranne `"roma"`.

---

## ** 2 Operatore Ternario**  
È un **if-else compatto** in una sola riga.  

### **Sintassi:**
```python
valore = valore_se_true if condizione else valore_se_false
```

### **Esempio:**
```python
eta = 20
messaggio = "Maggiorenne" if eta >= 18 else "Minorenne"
print(messaggio)  # Output: Maggiorenne
```
 Se `eta >= 18`, `messaggio = "Maggiorenne"`, altrimenti `"Minorenne"`.

---

## ** 3 Differenza tra List Comprehension e Operatore Ternario**  
| **Feature**            | **List Comprehension**     | **Operatore Ternario** |
|------------------------|----------------------------|------------------------|
| Crea una lista?        | ✅ Sì                     | ❌ No                  |
| Itera su elementi?     | ✅ Sì                     | ❌ No                  |
| Sostituisce `if-else`? | ❌ No (ma può usare `if`) | ✅ Sì                  |

### ** Esempio Confronto**
#### **List Comprehension**
```python
numeri = [1, 2, 3, 4, 5]
quadrati = [x**2 for x in numeri]
print(quadrati)  # Output: [1, 4, 9, 16, 25]
```
 **Crea una lista** con i quadrati dei numeri.

#### **Operatore Ternario**
```python
x = 5
tipo = "Pari" if x % 2 == 0 else "Dispari"
print(tipo)  # Output: Dispari
```
 **Assegna un valore in base alla condizione**.

---

## ** 4 Altre "One-Liners" Utili**
### **Lambda (funzione anonima in una riga)**
```python
doppio = lambda x: x * 2
print(doppio(4))  # Output: 8
```
 Funzione compatta per calcolare il doppio di un numero.

### **Join (per unire stringhe)**
```python
parole = ["Ciao", "come", "stai"]
frase = " ".join(parole)
print(frase)  # Output: "Ciao come stai"
```
 Unisce gli elementi di una lista con `" "`.

### **List Comprehension con if-else**
```python
numeri = [1, 2, 3, 4, 5]
descrizioni = ["Pari" if n % 2 == 0 else "Dispari" for n in numeri]
print(descrizioni)  # Output: ['Dispari', 'Pari', 'Dispari', 'Pari', 'Dispari']
```
 Combina **list comprehension + operatore ternario**! 

---

### ** Conclusione**
- **List Comprehension** → Per creare liste velocemente  
- **Operatore Ternario** → Per assegnare valori in base a una condizione  
- **Lambda, Join & Altri** → Per ottimizzare codice in una sola riga  


Conclusione
✅ For in una riga? → Sì, molto usato con List Comprehension
✅ While in una riga? → Possibile, ma meno leggibile
✅ If + for in una riga? → Sì, per filtrare dati:

pari = [x for x in range(10) if x % 2 == 0]
print(pari)  # Output: [0, 2, 4, 6, 8]

✅ While + if in una riga? → Si può fare, ma meglio evitarlo 

 Regola d'oro: Scrivere codice chiaro è meglio che scrivere codice compatto!!!


Vediamo con Chat GPT...

**Short-hand e operatori ternari non sono esattamente la stessa cosa**, anche se entrambi servono 
per scrivere codice più compatto.   

---

## **📌 1️⃣ Short-Hand (Sintassi Ridotta)**
Il termine **short-hand** (sintassi ridotta) si riferisce a qualsiasi metodo per scrivere codice
più compatto rispetto alla forma tradizionale.  

### **Esempi di Short-Hand**
✅ **List comprehension (forma compatta di `for`)**
```python
numeri = [x**2 for x in range(5)]
print(numeri)  # Output: [0, 1, 4, 9, 16]
```
🔹 Crea una lista in un'unica riga invece di usare un `for` tradizionale.  

✅ **For in una riga senza list comprehension**
```python
for x in range(3): print(x)
```
🔹 Evita di scrivere il `for` su più righe.  

✅ **If in una riga (senza else)**
```python
x = 10
if x > 5: print("Maggiore di 5")
```
🔹 Scrive una condizione `if` in una riga, senza necessità di `{}` come in altri linguaggi.  

---

## **📌 2️⃣ Operatore Ternario (Forma compatta di `if-else`)**
L'operatore **ternario** è una forma ridotta di `if-else` in una sola riga.  

### **Sintassi**
```python
valore = valore_se_true if condizione else valore_se_false
```

### **Esempio**
```python
eta = 20
messaggio = "Maggiorenne" if eta >= 18 else "Minorenne"
print(messaggio)  # Output: Maggiorenne
```
🔹 Funziona solo per **un'assegnazione condizionale**.

---

## **📌 Differenze Chiave**
| **Caratteristica**               | **Short-Hand (Sintassi ridotta)**    | **Operatore ternario**           |
|----------------------------------|--------------------------------------|----------------------------------|
| Cos'è?                           | Un modo compatto di scrivere codice  | Un'espressione `if-else` ridotta |
| Può contenere `for`?             | ✅ Sì (List Comprehension)          | ❌ No                            |
| Può contenere `if` senza `else`? | ✅ Sì                                | ❌ No                           |
| Può contenere `if-else`?         | ❌ No (tranne in list comprehension) | ✅ Sì                           |

---

## **📌 Esempi di Confronto**
### **Short-Hand (List Comprehension)**
```python
numeri = [x for x in range(10) if x % 2 == 0]
print(numeri)  # Output: [0, 2, 4, 6, 8]
```
🔹 Usa un `if`, ma **non può sostituire un vero `if-else`**.

### **Operatore Ternario**
```python
x = 10
messaggio = "Positivo" if x > 0 else "Negativo"
print(messaggio)  # Output: Positivo
```
🔹 Usa `if-else` per **assegnare un valore condizionale**.

---

### **🎯 Conclusione**
✅ **Short-hand ≠ Operatore ternario**  
✅ **Short-hand = modo per scrivere codice più compatto**  
✅ **L'operatore ternario è un caso specifico di short-hand, ma si usa solo per `if-else`**  

💡 **Ricorda:** Short-hand include anche **list comprehension, for in una riga, if senza else**, 
     mentre l'operatore ternario è solo un modo di scrivere un `if-else` compatto.  

-------------------------
Problema di Giovanni...
Puoi usare `range()` e una **tuple comprehension** (che in realtà è un generatore, quindi dovrai convertirlo in una tupla).  

Ecco come fare:  

```python
tupla_quadrati = tuple(x**2 for x in range(1, 6))
print(tupla_quadrati)  # Output: (1, 4, 9, 16, 25)
```

### **Spiegazione**
- `range(1, 6)`: genera i numeri da **1 a 5** (il 6 è escluso).
- `x**2`: calcola il quadrato di ogni numero.
- `tuple(...)`: converte il risultato in una tupla.

Se invece vuoi farlo senza comprehension, puoi usare `map()`:

```python
tupla_quadrati = tuple(map(lambda x: x**2, range(1, 6)))
print(tupla_quadrati)  # Output: (1, 4, 9, 16, 25)
```
-----
E possibile farlo senza **map()** e senza **tuple comprehension**, 
utilizzando un semplice ciclo `for` e la creazione manuale della tupla.  

Ecco il codice:  

```python
quadrati = []  # Creiamo una lista vuota
for x in range(1, 6):  # Iteriamo sui numeri da 1 a 5
    quadrati.append(x**2)  # Calcoliamo il quadrato e lo aggiungiamo alla lista

tupla_quadrati = tuple(quadrati)  # Convertiamo la lista in una tupla
print(tupla_quadrati)  # Output: (1, 4, 9, 16, 25)
```

### **Spiegazione**
1. Creiamo una lista vuota `quadrati`.
2. Usiamo un `for` per iterare sui numeri da **1 a 5**.
3. Ad ogni iterazione, calcoliamo `x**2` e lo aggiungiamo alla lista con `.append()`.
4. Dopo il ciclo, convertiamo la lista in una tupla con `tuple(quadrati)`.
5. Stampiamo il risultato.

Questo metodo è più lungo rispetto alla **tuple comprehension**, ma è più leggibile per chi sta imparando Python.

----

La funzione map() viene utilizzata per applicare una determinata funzione a ogni elemento di un iterabile, 
come una lista o una tupla e restituisce un oggetto map (che è un iteratore).

Cominciamo con un semplice esempio di utilizzo di map() per convertire un elenco di stringhe in un elenco di numeri interi.




s = ['1', '2', '3', '4']
res = map(int, s)
print(list(res))

Produzione
[1, 2, 3, 4]
Spiegazione: Qui abbiamo utilizzato la funzione int integrata per convertire ogni stringa nell'elenco s 
in un intero. La funzione map() si occupa di applicare int() a ogni elemento


La sintassi della funzione map() è la seguente:

map(funzione, iterabile)


Parametri:
funzione: la funzione che vogliamo applicare a ogni elemento dell'iterabile.
iterabile: l'iterabile di cui vogliamo elaborare gli elementi.

https://www.geeksforgeeks.org/python-map-function/
-------------------------

## ** Esercizi pratici consigliati**

- **Calcolatrice** (usa input, operatori e condizioni)
- **Gestione di una rubrica** (dizionari, liste)
- **Gioco dell'indovina numero** (random, cicli e condizioni)
- **Convertitore di temperatura** (funzioni)
- 

-------------------------------------------------------

'''

'''
Il **flowchart** (diagramma di flusso) per il nostro **script di gestione del magazzino**.


      +----------------------------------+
      |            INIZIO                |
      +----------------------------------+
                 |      
                 v
      +------------------------------+
      |  MOSTRA MENU                 |
      |  1. Aggiungi prodotto         |
      |  2. Visualizza prodotti       |
      |  3. Rimuovi prodotto          |
      |  4. Modifica quantità         |
      |  5. Esci                      |
      +------------------------------+
                 |
                 v
      +------------------------------+
      |  INSERISCI SCELTA             |
      +------------------------------+
                 |
      +---------+---------------------------------------------------------------+
      |                  |                  |                     |             |
      v                  v                  v                     v             v
+-------------+ +----------------+ +----------------+ +----------------+ +----------------+
| Scelta = 1 | | Scelta = 2      | | Scelta = 3      | | Scelta = 4      | | Scelta = 5      |
+-------------+ +----------------+ +----------------+ +----------------+ +----------------+
      |                       |                |                  |                  |
      v                       v                v                  v                  v
+----------------+  +----------------+ +----------------+ +----------------+ +----------------+
| INSERISCI      |  | SE MAGAZZINO    | | INSERISCI      | | INSERISCI      | | MOSTRA         |
| NOME E QUANTITÀ|  | È VUOTO         | | NOME PRODOTTO  | | NOME PRODOTTO  | | "USCITA..."    |
+----------------+  | MOSTRA "VUOTO"  | | SE TROVATO     | | SE TROVATO     | +----------------+
      |             | ALTRIMENTI      | | RIMUOVI        | | INSERISCI NUOVA|
      v             | MOSTRA PRODOTTI | | PRODOTTO       | | QUANTITÀ       |
+----------------+  +----------------+ +----------------+ +----------------+
| AGGIUNGI AL   |      | SE PRODOTTO NON TROVATO, MOSTRA "NON TROVATO"   |
| MAGAZZINO     |      | STESSA LOGICA PER MODIFICA QUANTITÀ             |
+----------------+     +------------------------------------------------+
      |
      v
+----------------+
| RITORNA AL MENU|
+----------------+
      |
      v
+----------------+
|      FINE      |
+----------------+


---------------------


### ** Flowchart Testuale (Pseudocodice)**
```
INIZIO
↓
MOSTRA MENU
↓
INSERISCI SCELTA
↓
SE scelta = 1:
    INSERISCI NOME E QUANTITÀ DEL PRODOTTO
    AGGIUNGI PRODOTTO AL MAGAZZINO
SE scelta = 2:
    SE MAGAZZINO È VUOTO:
        MOSTRA "MAGAZZINO VUOTO"
    ALTRIMENTI:
        MOSTRA LISTA PRODOTTI
SE scelta = 3:
    INSERISCI NOME DEL PRODOTTO DA RIMUOVERE
    SE PRODOTTO TROVATO:
        RIMUOVI PRODOTTO
    ALTRIMENTI:
        MOSTRA "PRODOTTO NON TROVATO"
SE scelta = 4:
    INSERISCI NOME DEL PRODOTTO DA MODIFICARE
    SE PRODOTTO TROVATO:
        INSERISCI NUOVA QUANTITÀ
        MODIFICA QUANTITÀ
    ALTRIMENTI:
        MOSTRA "PRODOTTO NON TROVATO"
SE scelta = 5:
    MOSTRA "USCITA DAL PROGRAMMA"
    TERMINA
ALTRIMENTI:
    MOSTRA "SCELTA NON VALIDA"
↓
RITORNA AL MENU
↓
FINE
```

---

-------------------------------------------------------
Creiamo uno **script semplice per la gestione di un magazzino** usando solo:  
**Input dell'utente**  
**Liste**  
**If, For, While**  
**Operatori**  

---

## ** Funzionalità dello script**  
1. Aggiungere un prodotto al magazzino  
2. Visualizzare i prodotti disponibili  
3. Rimuovere un prodotto  
4. Modificare la quantità di un prodotto  
5. Uscire dal programma  

---

'''
# Lista per memorizzare i prodotti del magazzino
magazzino = []

while True:
    print("\n GESTIONE MAGAZZINO ")
    print("1 Aggiungi prodotto")
    print("2 Visualizza prodotti")
    print("3 Rimuovi prodotto")
    print("4 Modifica quantità")
    print("5 Esci")
    
    scelta = input("Scegli un'opzione: ")

    # Aggiungere un prodotto
    if scelta == "1":
        prodotto = input("Nome del prodotto: ")
        quantita = int(input("Quantità: "))
        magazzino.append([prodotto, quantita])  # Aggiungiamo come lista [nome, quantità]
        print(f" {prodotto} aggiunto con {quantita} unità.")

    # Visualizzare i prodotti
    elif scelta == "2":
        if not magazzino:
            print(" Magazzino vuoto!")
        else:
            print("\n Lista prodotti:")
            for item in magazzino:
                print(f"- {item[0]}: {item[1]} unità")

    # Rimuovere un prodotto
    elif scelta == "3":
        prodotto = input("Nome del prodotto da rimuovere: ")
        trovato = False
        for item in magazzino:
            if item[0] == prodotto:
                magazzino.remove(item)
                print(f" {prodotto} rimosso dal magazzino.")
                trovato = True
                break
        if not trovato:
            print(" Prodotto non trovato!")

    # Modificare la quantità di un prodotto
    elif scelta == "4":
        prodotto = input("Nome del prodotto da modificare: ")
        trovato = False
        for item in magazzino:
            if item[0] == prodotto:
                nuova_quantita = int(input("Nuova quantità: "))
                item[1] = nuova_quantita
                print(f" Quantità di {prodotto} aggiornata a {nuova_quantita}.")
                trovato = True
                break
        if not trovato:
            print(" Prodotto non trovato!")

    # Uscire dal programma
    elif scelta == "5":
        print(" Uscita dal programma. A presto!")
        break

    else:
        print(" Scelta non valida! Riprova.")


### ** Come funziona?**
'''
- Il **magazzino è una lista di liste**, dove ogni elemento è `[prodotto, quantità]`.
- Usiamo un **while True** per tenere il programma attivo finché l'utente non sceglie di uscire.
- Il **menu interattivo** permette di **aggiungere, visualizzare, rimuovere o modificare prodotti**.
- Usiamo **if-elif-else** per gestire le diverse operazioni.

---

'''