#i dictionary: ordinati,modificabili ma no duplicati (solo per le chiavi)
# funzionano con coppie chiave-valore (come gli oggetti in js)
#anche con dict possiamo usare i metodi type(), len()

ilMioDict = {"nome":"claudio","cognome":"rossi","eta":25}

#meglio un nome appropriato anche in virtù
#della futura programmazione ad oggetti
persona = {"nome":"claudio","cognome":"rossi","eta":25}
persona2 = {"nome":["claudio","andrea"],"cognome":"rossi","eta":25}


#per accedere agli elementi:
print(persona["cognome"]) #niente indici ma chiavi e valori

print(persona.get("nome")) #uguale al get
print(persona2.get("nome")) #uguale al get

print(persona.keys()) #elenco delle chiavi

print(persona.values()) #elenco dei valori

print(persona.items()) #elenchi...come le tuple

print("nome" in persona) #per vedere se presente una chiave

#vediamo ora la modifica di un elemento:
persona ["nome"] = "andrea"
print(persona)

persona.update({"nome": "anna"})
print(persona)

#vediamo ora l'aggiunta di un elemento: (chiaramente una coppia)
#altrimenti sarebbe una modifica)
persona ["indirizzo"] = "roma"
print(persona)

persona.update({"via": "gorizia"})
print(persona)

print("--------------------------")

#per rimuovere elementi:
persona.pop("via")
print(persona)

persona.popitem() #rimozione ultimo elemento
print(persona)

#persona.clear() #un dict vuoto
#print(persona)

#del persona #eliminazione del dict
#print(persona)
#oppure 
print("---------------####------------------")
del persona ["eta"]
print(persona)

#per ciclare:
for x in persona:  #per le chiavi
    print(x)

for x in persona:  #per i valori
    print(persona[x])

for x in persona.values(): #ancora valori
    print(x)

for x in persona.keys(): #ancora chiavi
    print(x)

print("-------------------...-----------------------")

#con items si creano tuple...quindi 2 valori
for x,y in persona.items(): #ancora valori
    print(x,y)

print("-------------------,,,,,,----------------------")
#per copiare:
pers_elenco2 = persona.copy()
print (pers_elenco2)

pers_elenco3 = dict(persona)
print (pers_elenco3)

#dict annidati:
pers_elenco4 = {
        "nome":"claudio",
        "cognome":"rossi",
        "eta":25,
        "indirizzo": {
            "citta": "milano",
            "via": "leopardi giacomo",
            "numero": 45
            }
}
print (pers_elenco4)
print(pers_elenco4["indirizzo"]["via"])

'''
Il dizionario Python è molto simile alle liste, ma a differenze di queste ultime, 
caratterizzate da un indice (numerico) progressivo per ogni elemento, 
nei dizionari abbiamo una relazione chiave-valore.

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}


Forse potrà sembrare strana questa relazione se pensassimo a un dict con due liste…
Come sincronizzare le liste? Lo studieremo prossimamente grazie alle due librerie più importanti di Python: Numpy e Pandas.     
ds = {           #un dataset ...
    'mesi' : ['gennaio','febbraio','marzo','aprile','maggio'],
    'giorni' : [31,28,31,30,31]  }
'''





