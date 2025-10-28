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

