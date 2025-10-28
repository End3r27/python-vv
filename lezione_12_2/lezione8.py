#i set, non ordinati, non indicizzati, non modificabili, no duplicati

#puntualizziamo non modificabili:
#non puoi cambiare direttamente un elemento all'interno di un set in Python. 
# Tuttavia, puoi rimuovere l'elemento esistente e quindi aggiungere il nuovo 
# elemento al set!

ilMioSet = set ({"roma", "torino", "genova", "livorno"})
ilMioSet = {"roma", "torino", "genova", "livorno"}

print(ilMioSet)



print("prova")
#len(), type(), set() anche qui

#si accede agli elementi con i loop cioè i cicli
ilMioSet2 = {"roma", "torino", "genova", "livorno","bari","taranto"}
for citta in ilMioSet2:
    print(citta)


print("------------p-------------")


print("roma" in ilMioSet)

print(ilMioSet)

#aggiungere e rimuovere gli elementi
#add 
ilMioSet.add("venezia")
print(ilMioSet)

ilMioSet.update(ilMioSet2)
print(ilMioSet)
print("------------pppp------------")
#per rimuovere gli elementi: remove(),discard(),pop(),clear(),del
ilMioSet.remove("bari")
print(ilMioSet)
#solo se siamo sicuri dell'esistenza dell'elemento altrimenti:
ilMioSet.discard("taranto")
print(ilMioSet)

#togliere "l'ultimo" elemento: ...naturalmente a caso
ilMioSet.pop()
print(ilMioSet)

#per svuotare il set:
ilMioSet.clear()
print(ilMioSet)

#per eliminare completamente il set
#del ilMioSet
#print(ilMioSet)

