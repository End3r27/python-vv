#introduzione a Python - seconda parte.

#prima di passare ai costrutti importanti (if,for,while,etc.etc)
#vediamo come python considera come valori booleani anche altre
#situazioni:

#risultano essere False
# bool (None)
'''
None è uno strumento utile per indicare un'assenza di valore, 
un risultato non valido o una variabile non inizializzata,
ed è largamente usato in Python in contesti in cui non è 
necessario un valore significativo.
In Python, None è un oggetto speciale che rappresenta l'assenza 
di valore o un valore "null".
In Python, None è un oggetto della classe NoneType.
È una vera e propria istanza, il che significa che può essere 
manipolata e trattata come qualsiasi altro oggetto in Python.
Può essere passato come argomento a una funzione o memorizzato
in una variabile.
Null non esiste in python e si usa solo None.
In alcuni linguaggi di programmazione, ci sono differenze concettuali 
tra null e None, oppure si usano entrambi in contesti diversi per 
rappresentare l'assenza di valore o comportamenti particolari.

'''
# bool (0)
# bool ("")
# bool (())     quindi tuple vuote
# bool ([])     list vuota
# bool ({})     dict e set vuoti

print("--------esempi su True e False-------------------")

laMiaVariabile= True
lamiavariabile = []
print(bool(lamiavariabile))

lamiavariabile2 = bool(1)

print(lamiavariabile2)

#vediamo ora il casting...

print("------------esempi di casting esplicito------------------")

#casting
#esplicito

x = 4.5
y = "dani"
#print(x+y)
x = str(4.5)
print(x+y)
z = int("6")
print("-----------------------------------")
l = int("6")
m = 3
n = l+m

print(n)
print("-----------------------------------")

#casting
#implicito
print("---------casting implicito--------------------------")
a=10
b=5.6
c=a+b
print(c)
print(a)

print("-----------la condizione if-----------")


#la condizione if

#scritta in sintassi o in grammatica sarebbe
#if condizione : istruzione 
#come sarà la sintassi per inizializzare le variabili?



y = 20
if y <19:
    print("ciao")
    print("buongiorno")
    print("buon pomeriggio")
else:
    print("buonasera")
    
    
    
if y > 19:
    print("buona serata")
    print("buon riposo")
    print("buon pomeriggio")
            
    



y = 14
if y == 14:
   print("è uguale a 14")
else:
    print("non è uguale a 14")
print("------------------------------")


r = 14
if r != 14:
    print("non è uguale a 14")
else:
    print("è uguale a 14")

    
r = 13
if r != 13:
    print("non è uguale")
elif r == 13:
    print ("si")
else:
    print("non so")

#di elif ce ne possono essere quanti se ne vuole


#operatori logici and, or e not
u = 13
if 10 <= u <= 20 or u == 14: #come se ci fosse un and...compreso tra 10 e 20
    print("è compreso tra 10 e 20   1°caso")
else:
    print("non è compreso tra 10 e 20 oppure è 14")
print("-------------------**-------------------")


t = 13
if t > 10 and t < 20:
    print("è compreso tra 10 e 20   2°caso")
else:
    print("non è compreso tra 10 e 20  2")
   # t = 13
print("-------------------***-------------------")
q = 11
if q < 10 or q < 20:
    print("è compreso tra 10 e 20   3°caso")
else:
    print("non è compreso tra 10 e 20  3")
print("-------------------###-------------------")
t = 13
if t > 10 or t == 20:
    print("è compreso tra 10 e 20   4°caso")
else:
    print("non è compreso tra 10 e 20  4")
print("-------------------xxxx-------------------")
x = 12
if not(x > 10):
    print("non è compreso dal 10 in poi   5")
else:
    print("è compreso dal 10 in poi  5°caso")

#short hand
if x > 10: print("vero")

print("vero") if x < 10 else print("falso")

#https://www.html.it/pag/15275/loperatore-ternario/

#https://lorenzoneri.com/operatore-ternario-in-python-come-funziona/

#https://it.from-locals.com/python-if-conditional-expressions/

# if annidati

if x % 2 == 0:
    print ("pari")
    if(x>10):
        print("pari e maggiore di dieci")
else:
    print ("dispari")
    
#proviamo a realizzare un programma che chieda all'utente
#di digitare un numero e di stampare a video se si tratta
#di un numero pari o dispari.

print("-------------il ciclo for----------------")
 # il ciclo for


seq = [1,2,3,4,5,]
for numeri in seq:
    print('Il quadrato di', numeri, 'è', numeri**2)

print("----------------------")

for n in range(1, 100):
     #print(n)
     if n==50:
         print('il quadrato di', n, 'è', n**2)
     #print('il quadrato di', n, 'è', n**2)
     
print("----------------------")    
for n in range(1, 6):
     print('Il cubo di', n, 'è', n**3)

print("----------------------")


    
#vediamo il for con una lista:
laMiaLista = ["milano","roma","torino","genova"]

for città in laMiaLista:
     print(città)
     
#for annidati...

for i in range(3):

  for j in range(4):

   print(i, j)



#vediamo il for con una parola
laMiaParola = "buondi'"

for i in laMiaParola:
      print(i)



laMiaLista2 = [2,7,9,34,56,76,21]
ilMioNumero = 33

for i in laMiaLista2:
     print(ilMioNumero+i)
         
         
prezzi = [22,70,91,34,56,76,21]
iva = 22

for i in prezzi:
      importo_iva = i*iva/100
      importo_totale = i+importo_iva
      print(importo_totale)

print("------------il ciclo while-------------")
#while
#loop o ciclo
#break, continue, else

i = 2
while i < 8:
    print(i)
    i += 1
    
    
   
print ("ciao1")

i = 0
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1



print ("ciao2")



i = 0
while i < 6:
    i += 1 
    if i == 3:
        continue
    print(i)

print ("ciao3")

i = 0

while i < 6:
    print(i)
    i += 1
else :
        print("ho finito")

'''
pass e continue a confronto...fanno cose diverse. 
pass semplicemente non fa nulla, mentre continue 
va avanti con l'iterazione del ciclo successivo.
"After executing pass" una ulteriore istruzione 
verrebbe eseguita. Dopo continue, non lo sarebbe.
tratto da:
https://stackoverflow.com/questions/9483979/is-there-a-difference-between-pass-and-continue-in-a-for-loop-in-python
(pronuncia come si legge...una vera lezione sul pass più della documentazione ufficiale!)

'''  

print("--------no pass-----------")  

a = [5, 3, 4]
for element in a:
     if not element:
      pass
      #print(element)    #il print deve stare nell'if 
 
print("--------si pass-----------")       

a = [0, 1, 2]
for element in a:
     if not element:
      #pass              #il pass ci dà la possibilità di "implementare l'if"
      print(element)
 
print("--------continue----------")


for element in a:
     if not element:
         continue
     print(element)
     
#Durante il corso comunque vedremo altri utilizzi del pass.
#In definitiva: if...le istruzioni non possono essere vuote, 
# ma se per qualche motivo hai un'istruzione if senza contenuto, 
# inserisci la pass per evitare di ricevere un errore!!!



 


   

    


 


print ("-------break-------")
        
i = 0
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1



print ("-------continue-------")

i = 0
while i < 6:
    i += 1 
    if i == 3:
        continue
    print(i)


