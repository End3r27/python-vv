quit = False

while not quit:
    print("-------------------------------")
    print("Scegli un'operazione:")
    print("1. Operazioni aritmetiche")
    print("2. Operazioni di confronto")
    print("3. Operazioni logiche")
    print("4. Operazioni potenza/radice")
    print("5. Esci")
    print("-------------------------------")

    scelta = input("Inserisci il numero dell'operazione desiderata: ")

    if scelta == '1':
        print("-------------------------------")
        print("1. Addizione")
        print("2. Sottrazione")
        print("3. Moltiplicazione")
        print("4. Divisione")
        print("5. Torna indietro")
        op = input("Scegli l'operazione: ")
        
        if op != '5':
            num1 = float(input("Inserisci il primo numero: "))
            num2 = float(input("Inserisci il secondo numero: "))
            
            if op == '1':
                print(f"Risultato: {num1} + {num2} = {num1 + num2}")
            elif op == '2':
                print(f"Risultato: {num1} - {num2} = {num1 - num2}")
            elif op == '3':
                print(f"Risultato: {num1} * {num2} = {num1 * num2}")
            elif op == '4':
                if num2 != 0:
                    print(f"Risultato: {num1} / {num2} = {num1 / num2}")
                else:
                    print("Errore: Divisione per zero non consentita.")

    elif scelta == '2':
        print("-------------------------------")
        print("1. a > b")
        print("2. a < b")
        print("3. a >= b")
        print("4. a <= b")
        print("5. Torna indietro")
        op = input("Scegli l'operazione: ")
        
        if op != '5':
            num1 = float(input("Inserisci il primo numero: "))
            num2 = float(input("Inserisci il secondo numero: "))
            
            if op == '1':
                print(f"Risultato: {num1} > {num2} = {num1 > num2}")
            elif op == '2':
                print(f"Risultato: {num1} < {num2} = {num1 < num2}")
            elif op == '3':
                print(f"Risultato: {num1} >= {num2} = {num1 >= num2}")
            elif op == '4':
                print(f"Risultato: {num1} <= {num2} = {num1 <= num2}")

    elif scelta == '3':
        print("-------------------------------")
        print("1. a not b")
        print("2. a == b")
        print("3. a in b")
        print("4. a not in b")
        print("5. Torna indietro")
        op = input("Scegli l'operazione: ")
        
        if op != '5':
            if op in ['3', '4']:
                a = input("Inserisci una stringa: ")
                b = input("Inserisci una stringa in cui cercare: ")
                if op == '3':
                    print(f"Risultato: {a} in {b} = {a in b}")
                elif op == '4':
                    print(f"Risultato: {a} not in {b} = {a not in b}")
            else:
                num1 = float(input("Inserisci il primo numero: "))
                num2 = float(input("Inserisci il secondo numero: "))
                if op == '1':
                    print(f"Risultato: not {num1} = {not num1}")
                elif op == '2':
                    print(f"Risultato: {num1} == {num2} = {num1 == num2}")

    elif scelta == '4':
        print("-------------------------------")
        print("1. a ** b")
        print("2. a ** (1/b)")
        print("3. b ** a")
        print("4. b ** (1/a)")
        print("5. Torna indietro")
        op = input("Scegli l'operazione: ")
        
        if op != '5':
            num1 = float(input("Inserisci il primo numero: "))
            num2 = float(input("Inserisci il secondo numero: "))
            
            if op == '1':
                print(f"Risultato: {num1} ** {num2} = {num1 ** num2}")
            elif op == '2':
                if num2 != 0:
                    print(f"Risultato: {num1} ** (1/{num2}) = {num1 ** (1/num2)}")
                else:
                    print("Errore: Divisione per zero non consentita.")
            elif op == '3':
                print(f"Risultato: {num2} ** {num1} = {num2 ** num1}")
            elif op == '4':
                if num1 != 0:
                    print(f"Risultato: {num2} ** (1/{num1}) = {num2 ** (1/num1)}")
                else:
                    print("Errore: Divisione per zero non consentita.")

    elif scelta == '5':
        quit = True
        print("Uscita dal programma.")
    else:
        print("Scelta non valida. Riprova.")
