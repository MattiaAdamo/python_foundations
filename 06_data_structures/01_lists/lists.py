# 01_lists.py
# Strutture Dati Python — LISTE
# Python Data Structures — LISTS

# Creiamo una lista vuota
# Create an empty list
num = []

# Ciclo infinito per mantenere attivo il menu
# Infinite loop to keep the menu running
while True:

    # Stampa della lista corrente
    # Print current list
    print("\nCurrent list:", num)

    # Menu opzioni
    print("1 - Add number")
    print("2 - Remove number")
    print("3 - Sort list")
    print("4 - Show min and max")
    print("5 - Exit")

    # Input utente
    # User input
    choice = input("Choose an option: ")

    # =========================
    # Opzione 1: Aggiungi numero
    # Option 1: Add number
    # =========================
    if choice == '1':
        # Convertiamo l'input in intero
        # Convert input to integer
        n = int(input("Enter number to add: "))

        # Aggiungiamo il numero alla lista
        # Append number to list
        num.append(n)

    # =========================
    # Opzione 2: Rimuovi numero
    # Option 2: Remove number
    # =========================
    elif choice == "2":
        n = int(input("Enter number to remove: "))

        # Verifichiamo che il numero sia nella lista
        # Check if number exists in list
        if n in num:
            num.remove(n)  # rimuove la prima occorrenza
        else:
            print("Number not in list")

    # =========================
    # Opzione 3: Ordina lista
    # Option 3: Sort list
    # =========================
    elif choice == "3":
        num.sort()  # ordinamento crescente

    # =========================
    # Opzione 4: Mostra min e max
    # Option 4: Show min and max
    # =========================
    elif choice == "4":

        # Una lista vuota è False in Python
        # An empty list evaluates to False
        if num:
            print("Min:", min(num))
            print("Max:", max(num))
        else:
            print("List is empty")

    # =========================
    # Opzione 5: Esci
    # Option 5: Exit
    # =========================
    elif choice == "5":
        break

    # Caso non valido
    # Invalid option
    else:
        print("Invalid option")