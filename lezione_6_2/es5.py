numeri = [5, 12, 7, 9, 3, 21, 8]
iva = 10 / 100
for i in numeri:
    importo_iva = i * iva / 100
    importo_totale = i + importo_iva
    print(importo_totale)