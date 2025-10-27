
#Il tipo di dato stringa è molto importante in tutti i linguaggi...

#                  esempi di utilizzo delle stringhe
#   è indifferente "" o ''
#   no multilinea se non con """  """
#   una stringa...un array...un insieme di singoli caratteri

laMiaParola = 'torino'     
print (laMiaParola[0])
# prendere un solo carattere...si parte sempre da zero

#possiamo misurare la lunghezza
print (len(laMiaParola))
print("-----------------------------------")
#loop di una stringa approfondire su DelftStack
for i in "torino" :
    print (i)


#for(i=0;i<len(laMiaParola);i++)


print("-----------------***-------------------")


#una parte della stringa
laMiaParola2 = "torino milano roma"
print (laMiaParola2[:3])
print (laMiaParola2[3:5])
print (laMiaParola2[-2])

#ma ecco alcuni metodi da usare con le stringhe

print (laMiaParola2.upper())
#trasforma in maiuscolo

laMiaParola3 = "   TORINO milano roma"
print (laMiaParola3.lower())


#trasforma in minuscolo
print("-----------------222-------------------")

print (laMiaParola3.strip())
#toglie gli spazi vuoti all'inizio e alla fine

print (laMiaParola3.replace("l", "b"))
#sostituire una lettera

laMiaParola4 = "torino {}"
print (laMiaParola4.format(320.000))
#per concatenare tipi diversi

laMiaParola4 = "torino {1}, grandezza {0}"
print (laMiaParola4.format(320.000, 45))
#per concatenare tipi diversi con indice

laMiaParola4 = "torino {1}, grandezza {0}"
print (laMiaParola4.format(320.000, 45))
#per concatenare tipi diversi con indice

laMiaParola5 = "   TORINO milano roma \n \"bella\"  "  #\n per andare a capo
print (laMiaParola5)
#escape dei caratteri




#Accenniamo alla differenza tra i metodi e le funzioni.

print(laMiaParola3.index("r"))

#L'istruzione visualizza sullo schermo la posizione 
# dell'elemento nell'indice della lista












