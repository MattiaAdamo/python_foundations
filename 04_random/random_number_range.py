import random

print("=== Random Number Generator ===")

# Ask the user for range
# Chiedi all'utente l'intervallo
min_value = int(input("Insert minimum value: "))
max_value = int(input("Insert maximum value: "))

random_number = random.randint(min_value, max_value)

print("Generated number is:", random_number)