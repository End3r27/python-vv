mia_lista = ["gianni", "federico", "marco", "anna", "margherita"]

for nome in mia_lista:
    print(nome)

a = input("inserisci a: ")
b = input("inserisci b: ")
c = input("inserisci c: ")
d = input("inserisci d: ")

if a > b:
    print(a)
    if c > d:
        print(c)
else:
    print(b, d)

