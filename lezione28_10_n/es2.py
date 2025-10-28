# Programma di gestione di una scuola
studenti = []
insegnanti = []
collaboratori = []
while True:
    print("\n GESTIONE SCUOLA ")
    print("1 Aggiungi studente")
    print("2 Aggiungi insegnante")
    print("3 Aggiungi collaboratore")
    print("4 Visualizza tutti")
    print("5 Rimuovi persona")
    print("6 Esci")
    
    scelta = input("Scegli un'opzione: ")

    # Aggiungere uno studente
    if scelta == "1":
        cognome = input("Cognome dello studente: ")
        nome = input("Nome dello studente: ")
        telefono = input("Numero di telefono: ")
        studenti.append([cognome, nome, telefono])
        print(f" Studente {nome} {cognome} aggiunto.")

    # Aggiungere un insegnante
    elif scelta == "2":
        cognome = input("Cognome dell'insegnante: ")
        nome = input("Nome dell'insegnante: ")
        telefono = input("Numero di telefono: ")
        insegnanti.append([cognome, nome, telefono])
        print(f" Insegnante {nome} {cognome} aggiunto.")

    # Aggiungere un collaboratore
    elif scelta == "3":
        cognome = input("Cognome del collaboratore: ")
        nome = input("Nome del collaboratore: ")
        telefono = input("Numero di telefono: ")
        collaboratori.append([cognome, nome, telefono])
        print(f" Collaboratore {nome} {cognome} aggiunto.")

    # Visualizzare tutti
    elif scelta == "4":
        print("\n Studenti:")
        for s in studenti:
            print(f"- {s[1]} {s[0]}, Tel: {s[2]}")
        print("\n Insegnanti:")
        for i in insegnanti:
            print(f"- {i[1]} {i[0]}, Tel: {i[2]}")
        print("\n Collaboratori:")
        for c in collaboratori:
            print(f"- {c[1]} {c[0]}, Tel: {c[2]}")

    # Rimuovere una persona
    elif scelta == "5":
        tipo = input("Rimuovere (studente/insegnante/collaboratore): ").strip().lower()
        cognome = input("Cognome: ")
        nome = input("Nome: ")
        telefono = input("Numero di telefono: ")

        if tipo == "studente":
            for s in studenti:
                if s[0] == cognome and s[1] == nome and s[2] == telefono:
                    studenti.remove(s)
                    print(f" Studente {nome} {cognome} rimosso.")
                    break
            else:
                print(" Studente non trovato.")

        elif tipo == "insegnante":
            for i in insegnanti:
                if i[0] == cognome and i[1] == nome and i[2] == telefono:
                    insegnanti.remove(i)
                    print(f" Insegnante {nome} {cognome} rimosso.")
                    break
            else:
                print(" Insegnante non trovato.")

        elif tipo == "collaboratore":
            for c in collaboratori:
                if c[0] == cognome and c[1] == nome and c[2] == telefono:
                    collaboratori.remove(c)
                    print(f" Collaboratore {nome} {cognome} rimosso.")
                    break
            else:
                print(" Collaboratore non trovato.")

    # Uscire dal programma
    elif scelta == "6":
        print(" Uscita dal programma. A presto!")
        break

    else:
        print(" Scelta non valida! Riprova.")