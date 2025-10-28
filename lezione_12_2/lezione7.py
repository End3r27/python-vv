#le tuple...ordinate, indicizzate, non modificabili, permettono duplicati

laMiaTupla = ("roma","torino","milano")
#anche valori misti
print(laMiaTupla)

laMiaTupla2 = ("roma",)  #fondamentale che ci sia una virgola
print(type(laMiaTupla2))
#stessi usi di len(), type() e il costruttore tuple()

#stessa indicizzazione
print (laMiaTupla[0])
print (laMiaTupla[0:2])

#verificare se c'è un elemento
if "milano"in laMiaTupla:
    print("c'è milano")

#per modificare ci sono dei passaggi: da tupla a list e poi ancora a tupla
laMiaLista = list(laMiaTupla)
laMiaLista.remove ("milano")
laMiaTupla = tuple(laMiaLista)
print("---------tupla------")
print(laMiaTupla)
#ecco un uso concreto dei costruttori
print("----------------------") 
#per spacchettare
(a, b) = laMiaTupla
print(a)
print(b)
print("----------asterisco------------") 
(a, *b) = laMiaTupla
print(a)
print(b)
#qui possiamo notare che oltre alla stampa in output differente
#in realtà avviene un'altra cosa più importante:
#a avrà il valore 1.
#se laMiaTupla è (1, 2, 3, 4)  a avrà il valore 1.
#b sarà una lista contenente [2, 3, 4].
#Quindi, *b è un modo per catturare tutti gli elementi rimanenti in una lista. 
# Questo può essere molto utile quando non si sa in anticipo quanti elementi ci 
# saranno nella tupla o quando si vogliono gestire i restanti elementi in blocco.


print("-----::::::-----------------") 
#ciclare elementi:
for citta in laMiaTupla:
    print (citta)

    #stesse cose fatte con le liste con i... per il for e while
    #con il + si uniscono


laMiaTupla3 = laMiaTupla + laMiaTupla2
print(laMiaTupla3)

#count e index
numero = laMiaTupla3.count("roma")
print(numero)

numero2 = laMiaTupla3.index("torino")
print(numero2)


#in definitiva, la grande differenza, non sono modificabili e hanno le ()