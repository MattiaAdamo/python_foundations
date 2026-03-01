# 02_tuples.py
# Strutture Dati Python — TUPLE
# Python Data Structures — TUPLES

"""
IT:
Una tuple è una collezione ORDINATA e IMMUTABILE.
Non possiamo modificarla dopo la creazione.

EN:
A tuple is an ORDERED and IMMUTABLE collection.
It cannot be modified after creation.
"""

# =========================
# Esempi Base
# =========================

print("\n=== TUPLE BASICS / BASI TUPLE ===")

# Creazione tuple
# Tuple creation
point = (10, 20)

print("Point:", point)

# Accesso agli elementi (indicizzazione)
# Access elements (indexing)
print("First value:", point[0])
print("Second value:", point[1])

# Slicing
# Slicing
numbers = (1, 2, 3, 4, 5)
print("Slice [1:4]:", numbers[1:4])

# =========================
# Unpacking
# =========================

print("\n=== UNPACKING ===")

x, y = point
print("x =", x)
print("y =", y)

# Unpacking esteso
a, *middle, b = numbers
print("a =", a)
print("middle =", middle)
print("b =", b)

# =========================
# Immutabilità
# =========================

print("\n=== IMMUTABILITY TEST ===")

try:
    point[0] = 100
except TypeError as e:
    print("Error:", e)

# =========================
# Quando usare una tuple?
# =========================

print("\n=== WHEN TO USE TUPLES ===")
print("• Coordinate (x, y)")
print("• Record fissi")
print("• Valori di ritorno multipli")