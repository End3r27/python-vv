#list, tuple, set, dictionary
#sono collezioni di dati...()....[].....{}
#cambiano le proprietà...oltre alle parentesi

#qui c'è un ordine ben preciso! 
#sono indicizzati....0 1 2 3 4 ....vi possiamo accedere
#sono modificabili, possiamo aggiungere, cambiare, rimuovere elementi
#potrebbero essere anche immutabili, dipende...
#permette duplicati...due volte genova p.e. oppure no

#le liste: collezioni ordinate, modificabili anche con duplicati...sempre []
laMiaLista = ["milano","roma","torino","genova"]
print (laMiaLista [0])
laMiaLista2 = ["milano", 600, True]
#anche di tipi diversi
#type(), len(), list() che è un costruttore con (). 
print(type(laMiaLista))
print(len(laMiaLista))
laMiaLista3 = list(("marco","andrea","giacomo","luca"))
print (laMiaLista3 [1])
#possiamo usare il range:
print (laMiaLista3 [1:])
print (laMiaLista3 [:2])
#per modificare un valore:
laMiaLista3 [0] = "francesco"
print (laMiaLista3)
laMiaLista3 [1:3] = ["tizio","caio"]
print (laMiaLista3)
#per inserire un valore:
print("--------------------------------")
laMiaLista3.append ("franco")
print (laMiaLista3)
#per inserire un valore:
laMiaLista3.insert (1,"antonio")
print (laMiaLista3)
#possiamo estendere:
laMiaLista3.extend(laMiaLista2)
print (laMiaLista3)
#per rimuovere gli elementi:
laMiaLista3.remove("francesco")
print (laMiaLista3)
print("------------------------111-------------------")
laMiaLista3.pop(2)
print (laMiaLista3)
del laMiaLista3 [0]
print (laMiaLista3)
del laMiaLista3 
#print (laMiaLista3)

print("--:::::--------------------") 
laMiaLista3 = list(("marco","andrea","giacomo","luca"))
print (laMiaLista3)
laMiaLista3.clear()
print (laMiaLista3)
 #for con indice...da 0 a 4 escluso

for i in range(len(laMiaLista)):
   print(laMiaLista[i]) 
  # print(len(laMiaLista))

print("--------------****-----------------")
   
#while 
print("---------------#####-------") 
i=0
while i< len(laMiaLista):
   print(laMiaLista[i])
   i = i+1
print("----------------------") 
#short hand list comprehension...una sintassi ridotta per le list
[print(citta) for citta in laMiaLista]
print("--")
[print(citta) for citta in laMiaLista if citta != "roma"]
#espressione for item in list if condizione == True   ....la sintassi.....
#fare riferimento alla documentazione per altri casi

#per ordinare la lista: 
laMiaLista.sort()
print("1",laMiaLista)

laMiaLista.sort(reverse=True)
print("2", laMiaLista)

#copiare una lista
laMiaLista4 = laMiaLista.copy()
print("3", laMiaLista4)

laMiaLista5 = list (laMiaLista)

#unire due liste:
for citta in laMiaLista4:
   laMiaLista5.append(citta)
print ("4",laMiaLista5)

laMiaLista6 = laMiaLista5 + laMiaLista4

print ("5",laMiaLista6)

print(laMiaLista2)
print(laMiaLista3)
laMiaLista2.extend (laMiaLista3)
print ("6",laMiaLista2)




#le tuple: collezioni ordinate ma immutabili. Possono esserci duplicati.

#i set: collezioni non ordinate, non indicizzate, non modificabili, nessun duplicato.

#i dictionary: collezioni ordinate e modificabili, nessun duplicato.
