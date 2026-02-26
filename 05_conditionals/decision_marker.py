# ============================================================
# decision_maker.py
# Simple program to practice if / elif / else conditions
# Programma semplice per esercitarsi con if / elif / else
# ============================================================

# Ask the user to insert a number
# Chiediamo all'utente di inserire un numero
number = float(input("Insert a number: "))

print("\n--- ANALYSIS REPORT ---")

# ------------------------------------------------------------
# POSITIVE / NEGATIVE / ZERO CHECK
# Controllo se il numero è positivo, negativo o zero
# ------------------------------------------------------------

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# ------------------------------------------------------------
# EVEN OR ODD CHECK (only works correctly for integers)
# Controllo pari o dispari (funziona correttamente solo per interi)
# ------------------------------------------------------------

if number.is_integer():  # Check if the number is an integer
    if int(number) % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
else:
    print("The number is not an integer, cannot determine even/odd.")

# ------------------------------------------------------------
# RANGE CLASSIFICATION
# Classificazione per intervalli
# ------------------------------------------------------------

if number >= 0 and number <= 10:
    print("The number is between 0 and 10.")
elif number > 10 and number <= 100:
    print("The number is between 11 and 100.")
elif number > 100:
    print("The number is greater than 100.")
else:
    print("The number is negative (range classification skipped).")

print("\nAnalysis completed.")