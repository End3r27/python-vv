

#Introduzione a Python - prima parte

# La prima cosa che si scrive in un programma è quello che fa, 
# la versione, l'autore, il copyright.
# Con il # si possono fare i commenti su una riga 
""" Questo è un esempio di commento su piu righe 
(per python non c'è distinzione tra virgole singole o doppie)
I commenti servono per chiarire il codice a noi, a distanza 
di tempo, e per chiarire il codice agli altri sviluppatori.
"""
# Il cancelletto consente di aggiungere un commento 
# anche dopo il codice sulla stessa riga
''' 
vediamo altre caratterisctiche di python:
-Python è molto severo con l'indentazione;
-dopo ogni comando non occorre usare il ;
-Le variabili sono i primissimi argomenti per realizzare un
programma, altro non sono che delle scatole con un nome e un 
contenuto.
Possiamo nominare le nostre variabili attraverso delle specifiche:
- camelCase es. mioNumero
- PascalCase (poco utilizzato) es. MioNumero (infatti l'iniziale maiuscola
                                              si usa per le classi)
- snake_case es. mio_numero
Occorrono nomi corretti e adatti, occore dare nomi appropriati 
alle variabili che riflettano la loro funzione nel codice.
Non è una buona pratica nominare 2 variabili con lo stesso nome
(naturalmente in ambiti diversi (scope))
Le variabili possono essere singole o multiple
'''
numeroIniziale = 9 #in python la variabile non si deve dichiarare ma solo inizializzare nello stesso momento

# come possiamo notare occorre un nome, un operatore di assegnazione e un valore

# quello di sopra è un commento in line, ossia accanto al codice.

mioNumeroDecimale = 3.14 # in informatica per fare la virgola si usa il punto

ilMioNome = "Edoardo" # Questo è un esempio di una variabile di tipo stringa



#vediamo ora qualche esempio di un tipo di dato "collezioni"

citta = ["Roma", "Milano", "Torino"] # Questo è un primo esempio di variabile di tipo List, 

#le list sono come gli array di tutti gli altri linguaggi

iMieiNumeri = [1,2,3,4] # list di numeri

# per poter prendere un singolo valore da una list c'è bisogno 
# di un indice per es. [2] prenderà il valore 3, ma lo vedremo poi.
# L'attività di recuperare un numero 
# attraverso l'indice si chiama indexing; mentre per recuperare 
# più valori si usa lo slicing...lo vedremo poi.

# Ci sono tanti tipi di variabili in Python, completiamo quelle essenziali:

variabile_vera = True 

variabile_falsa = False

# le due variabili booleane rappresentano il concetto di verità o 
# falsità di una espressione, si utilizzano per le decisioni e il
# controllo di flusso di un programma, molto usate nelle if.

#vediamo meglio le variabili con questi due link:
#quelle essenziali:
#https://aulab.it/guide-avanzate/variabili-e-tipi-di-dati-in-python/
#un pò piu in dettaglio:
#https://www.html.it/pag/39743/variabili-e-commenti-in-python/




# esistono delle parole, Keyword, che non possono essere utilizzate 
# per nominare le variabili in quanto riservate.
# sconsigliato usare lettere accentate o apostrofo

#esiste la possibilita di assegnare piu variabili nella stessa 
# riga di codice con l'assegnamento multiplo:
a, b, c = 3, 4, 5

#variabili di appoggio:

y = 30
x = 20
z = x+y 
print(z)

# le variabili di appoggio si predispongono per ospitare 
# un valore o il frutto di un operazione. A tal proposito facciamo
# un esercizio...come poter scambiare fra di loro il valore di
# due variabili?

numAlfa = 1
numBeta = 2
numGamma = numAlfa
numAlfa = numBeta
numBeta = numGamma

print(numAlfa)
print(numBeta)

# Abbiamo già conosciuto la funzione print() che usiamo per
# stampare qualcosa. Vediamo ora altre funzioni python....
# la funzione type... quando occorre scoprire il tipo di una 
# variabile; è una funzione built-in (ossia incorporata in Python)
print("------vediamo il tipo di dato di z---------")
print(type(z))

#vediamo ora la funzione abs....
numNegativo = -5
print(abs(numNegativo)) 

# come possiamo notare la funzione restituisce il valore assoluto di un numero.
# per utilizzare le funzioni occorre il nome della funzione, le parentesi 
# e al loro interno, l'argomento o gli argomenti.

#il numero minore
x = min(5,10,15)
print (x)

#il numero maggiore
x = max(5,10,15)
print (x)

#la potenza di un numero
x = pow(5,2)
print (x)

#python ha tantissime funzioni built in...
#https://docs.python.it/html/lib/built-in-funcs.html



#abbiamo anche conosciuto la funzione input.
#questa funzione, come possiamo notare, oltre ad avere
#un argomento, restituisce anche un valore...

ilMioSaluto = input("scrivi un saluto .....")  
    
print(ilMioSaluto)

#quindi le funzioni possono avere argomenti e restituire
#qualcosa! Nel nostro caso la funzione input stampa la frase
#sul monitor invitando l'utente a scrivere un saluto. Il saluto
#scritto dall'utente andrà a finire nella variabile di appoggio
#ilMioSaluto che poi stamperemo con il print. Quindi la funzione
#input restituisce il saluto ma naturalmente occorre predisporre
#una variabile che possa contenerlo.


#Abbiamo capito che in un programma ci sono le variabili, i dati.
#Ma cosa ne facciamo? Con i dati facciamo delle operazioni...
#Proviamo allora a fare un semplice programma che possa accettare
#due numeri da tastiera e fare la somma che verrà stampata a video.
#Possiamo fare tante cose oltre la somma.... Vediamo allora i vari operatori
#di python:
#https://www.html.it/pag/39742/numeri-e-operatori-logici-in-python/

#quindi con i dati possiamo usare gli operatori aritmetici,
#gli operatori di confronto, gli operatori logici etc.etc.
#facciamo con tutti questi operatori alcuni esempi.
#Approfittiamo anche per aggiungere al nostro print la formattazione
#di testo e numeri insieme
numero = 34
#print("proviamo" + numero)
print("riproviamo", numero)
nome = "dan"
cognome = "mel"
print(nome +"  " + cognome)
print(nome ,"", cognome)

print("aggiungiamo un separatore per evidenziare meglio l'output con il codice")
print("----------------------------------------")
#la cosa serve sia nello script che nel terminal
print("molto meglio con la formattazione:")

# 1. Operatori aritmetici
# -----------------------

a = 10
b = 3

print("Operazioni aritmetiche:")
print(f"Somma: {a} + {b} = {a + b}")       # Addizione
print(f"Sottrazione: {a} - {b} = {a - b}") # Sottrazione
print(f"Moltiplicazione: {a} * {b} = {a * b}")  # Moltiplicazione
print(f"Divisione: {a} / {b} = {a / b}")   # Divisione
print(f"Divisione intera: {a} // {b} = {a // b}") # Divisione intera
print(f"Modulo (resto): {a} % {b} = {a % b}")  # Modulo
print(f"Esponenziazione: {a} ** {b} = {a ** b}") # Esponenziazione


# 2. Operatori di confronto
# -------------------------

print("\nOperazioni di confronto:")#notiamo lo \n che serve per andare a capo
print(f"{a} è uguale a {b}? {a == b}")   # Uguale
print(f"{a} è diverso da {b}? {a != b}") # Diverso
print(f"{a} è maggiore di {b}? {a > b}")   # Maggiore
print(f"{a} è minore di {b}? {a < b}")    # Minore
print(f"{a} è maggiore o uguale a {b}? {a >= b}") # Maggiore o uguale
print(f"{a} è minore o uguale a {b}? {a <= b}")  # Minore o uguale

#Gli operatori di confronto restituiscono sempre valori booleani.
#naturalmente in modo più semplice...
verifica = a == b
print(verifica)


# 3. Operatori logici
# -------------------

x = True
y = False

print("\nOperatori logici:")
print(f"x AND y: {x and y}")  # Operatore AND (e)
print(f"x OR y: {x or y}")    # Operatore OR (o)
print(f"NOT x: {not x}")      # Operatore NOT (negazione)

#in genere gli operatori logici combinano, insieme agli
#operatori di confronto, delle condizioni multiple.

# 4. Operatori di assegnazione
# ----------------------------

c = 5
print("\nOperatori di assegnazione:")
print(f"Inizializzazione c = {c}")
c += 3   # c = c + 3
print(f"c += 3: {c}")
c -= 2   # c = c - 2
print(f"c -= 2: {c}")
c *= 2   # c = c * 2
print(f"c *= 2: {c}")
c /= 2   # c = c / 2
print(f"c /= 2: {c}")
c %= 3   # c = c % 3
print(f"c %= 3: {c}")
c **= 2  # c = c ** 2
print(f"c **= 2: {c}")

# 5. Operatori di appartenenza
# ----------------------------

my_list = [1, 2, 3, 4, 5]
print("\nOperatori di appartenenza:")
print(f"3 è in my_list? {3 in my_list}")   # Operatore 'in'
print(f"10 non è in my_list? {10 not in my_list}")  # Operatore 'not in'

# 6. Operatori di identità
# ------------------------

d = [1, 2, 3]
e = [1, 2, 3]
f = d

print("\nOperatori di identità:")
print(f"d è f? {d is f}")  # 'is' verifica se due oggetti sono lo stesso oggetto
print(f"d è e? {d is e}")  # Anche se il contenuto è uguale, 'is' verifica l'identità in memoria
print(f"d non è e? {d is not e}")  # Verifica se non sono lo stesso oggetto

#Operatori di confronto, logici, di appartenenza, di identità, 
#restituiscono sempre un valore booleano; sono quindi chiamati
#operatori condizionali. La condizione può essere vera o falsa.


# 7. Operatori bitwise (a livello di bit)
# ---------------------------------------

g = 6  # In binario: 110
h = 3  # In binario: 011

print("\nOperatori bitwise:")
print(f"g AND h: {g & h}")  # Operatore AND bit a bit

#ne chiariamo uno per tutti...
#AND bit a bit (&): confronta i bit di due numeri, restituendo 
# 1 solo quando entrambi i bit sono 1

print(f"g OR h: {g | h}")   # Operatore OR bit a bit
print(f"g XOR h: {g ^ h}")  # Operatore XOR bit a bit
print(f"NOT g: {~g}")       # Operatore NOT bit a bit
print(f"g shift a sinistra di 1: {g << 1}")  # Shift a sinistra
print(f"g shift a destra di 1: {g >> 1}")    # Shift a destra


'''
Ricapitoliamo:

Operatori aritmetici: usati per eseguire operazioni matematiche.
+, -, *, /, //, %, **


Operatori di confronto: confrontano due valori e restituiscono 
True o False.
==, !=, >, <, >=, <=


Operatori logici: combinano espressioni booleane.
and, or, not

Operatori di assegnazione: usati per assegnare valori a una 
variabile.
=, +=, -=, *=, /=, %=, **=

Operatori di appartenenza: verificano se un valore è presente 
in una sequenza (lista, stringa, ecc.).
in, not in

Operatori di identità: controllano se due variabili puntano 
allo stesso oggetto.
is, is not

Operatori bitwise: operano sui singoli bit di numeri interi.
&, |, ^, ~, <<, >>

'''
'''
Possiamo a tal proposito aggiungere solo per chi desiderasse approfondire:
gli operatori bitwise possono essere usati non solo con variabili
ma anche per lavorare direttamente con spazi di memoria e dati 
a basso livello, in particolare quando si ha a che fare con 
linguaggi come C, dove puoi accedere alla memoria direttamente.
In Python, però, non hai accesso diretto alla memoria, ma puoi 
comunque manipolare i bit che rappresentano i numeri interi o
le variabili.
In sintesi:
I bit di un dato (la rappresentazione binaria) corrispondono ai 
bit nella memoria del computer. Tuttavia, il modo in cui questi 
bit vengono memorizzati può dipendere dal tipo di dato (intero,
stringa, float, ecc.).
Nei linguaggi di basso livello come C, puoi accedere direttamente 
alla memoria e vedere come i dati sono memorizzati. In Python, 
invece, la gestione della memoria è astratta, ma puoi comunque
manipolare i bit attraverso le variabili.
Facciamo un esempio:
Le stringhe sono tipicamente memorizzate come una sequenza di byte. 
Ogni carattere viene codificato come una serie di bit (ad esempio,
utilizzando la codifica ASCII o UTF-8).

Se memorizzi la stringa "ABC", ogni carattere viene convertito 
nella sua rappresentazione binaria:

'A' → 01000001 (65 in decimale)
'B' → 01000010 (66 in decimale)
'C' → 01000011 (67 in decimale)

Ma vediamo meglio i due contesti (variabili, memoria):

1. Operatori bitwise sulle variabili (in Python)
In Python, quando usi gli operatori bitwise (&, |, ^, ecc.), stai 
operando sui bit dei numeri interi memorizzati nelle variabili. 
Ad esempio, quando scrivi:


a = 6  # a è memorizzato come 110 nei bit (in binario)
b = 3  # b è memorizzato come 011 nei bit (in binario)

result = a & b  # Esegue un AND bitwise su a e b
L'operatore bitwise funziona sui bit che compongono i valori 
delle variabili a e b, ma non agisce direttamente sulla memoria 
fisica (cioè, sugli indirizzi di memoria). In Python, i numeri 
sono già rappresentati in binario internamente, quindi gli operatori 
bitwise sono un modo per manipolare direttamente la loro rappresentazione binaria.

2. Operatori bitwise applicati a spazi di memoria (livello più basso)
In linguaggi di basso livello come C o assembly, gli operatori bitwise possono 
essere utilizzati direttamente per manipolare blocchi di memoria. 
Questo è particolarmente utile quando lavori con:

registri del processore,
indirizzi di memoria (ad esempio, quando lavori su sistemi embedded o driver di dispositivi),
operazioni su byte (ad esempio, quando comunichi con hardware direttamente).
In C, ad esempio, puoi manipolare blocchi di memoria direttamente usando puntatori e operatori bitwise. 
Ecco un esempio in C:


unsigned char byte = 0b10101010; // byte con valore binario
byte = byte & 0b11110000;        // Mantiene i 4 bit più alti, azzera i 4 bit più bassi
In questo caso, stai operando direttamente sulla memoria che contiene il byte,
il che può essere utile per ottimizzare la gestione della memoria o controllare l'hardware.

3. Python e accesso alla memoria
In Python, non si ha accesso diretto alla memoria come in C o linguaggi di basso livello. 
Tuttavia, Python può manipolare dati binari (ad esempio, bit o byte) in modo molto comodo, attraverso:

bytearray e bytes (manipolazione di sequenze di byte),
struct (per lavorare con dati binari strutturati),
numpy (per elaborare array di bit e byte).

'''
