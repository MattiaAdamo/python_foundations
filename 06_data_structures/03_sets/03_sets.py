# -*- coding: utf-8 -*-
"""
03_sets.py — Strutture Dati Python: SET
--------------------------------------
EN: Educational script about SETS: uniqueness, fast membership checks,
    and classic set operations (union, intersection, difference).
IT: Script didattico sui SET: unicità, controllo di appartenenza veloce,
    e operazioni tra insiemi (unione, intersezione, differenza).

Run / Esegui:
    python 03_sets.py
"""

# IT: Un set è una collezione NON ordinata di elementi UNICI.
# EN: A set is an UNORDERED collection of UNIQUE items.


# =========================
# THEORY + EXAMPLES
# =========================
def demo_basics():
    print("\n=== SET BASICS / BASI SET ===")

    # Creating a set (duplicates are removed)
    # Creazione set (i duplicati vengono rimossi automaticamente)
    s = {1, 2, 2, 3, 4, 4}
    print("Set / Insieme:", s)

    # Add element
    # Aggiunta elemento
    s.add(10)
    print("After add(10) / Dopo add(10):", s)

    # Membership check (very fast)
    # Controllo appartenenza (molto veloce)
    print("Is 3 in set? / 3 è nel set?", 3 in s)

    # remove() vs discard()
    # IT: remove() genera errore se l'elemento non esiste; discard() no.
    # EN: remove() raises an error if missing; discard() does not.
    s.discard(999)  # no error / nessun errore
    try:
        s.remove(999)
    except KeyError as e:
        print("Expected KeyError / KeyError atteso:", e)

    # Convert list -> set to remove duplicates
    # Conversione lista -> set per rimuovere duplicati
    names = ["anna", "luca", "anna", "mario", "luca"]
    unique_names = set(names)
    print("\nNames / Nomi:", names)
    print("Unique / Unici:", unique_names)


def demo_operations():
    print("\n=== SET OPERATIONS / OPERAZIONI TRA SET ===")
    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}
    print("A:", a)
    print("B:", b)

    # Union / Unione
    print("A | B (union / unione):", a | b)

    # Intersection / Intersezione
    print("A & B (intersection / intersezione):", a & b)

    # Difference / Differenza
    print("A - B (difference / differenza):", a - b)
    print("B - A (difference / differenza):", b - a)

    # Symmetric difference / Differenza simmetrica
    print("A ^ B (symmetric diff / diff simmetrica):", a ^ b)


# =========================
# MINI CLI EXERCISE
# =========================
def normalize_word(w: str) -> str:
    # IT: Normalizziamo la parola per confronto (lower + strip).
    # EN: Normalize word for comparison (lower + strip).
    return w.strip().lower()


def unique_words_analyzer():
    print("\n=== UNIQUE WORDS ANALYZER / ANALIZZATORE PAROLE UNICHE ===")
    print("EN: Write a sentence and I'll show unique words.")
    print("IT: Scrivi una frase e ti mostro le parole uniche.")

    sentence1 = input("\nSentence 1 / Frase 1: ").strip()
    sentence2 = input("Sentence 2 (optional) / Frase 2 (opzionale): ").strip()

    words1 = [normalize_word(w) for w in sentence1.split() if normalize_word(w)]
    set1 = set(words1)

    print("\n--- Results for sentence 1 / Risultati frase 1 ---")
    print("Total words / Parole totali:", len(words1))
    print("Unique words / Parole uniche:", len(set1))
    print("Set / Insieme:", set1)

    if sentence2:
        words2 = [normalize_word(w) for w in sentence2.split() if normalize_word(w)]
        set2 = set(words2)

        print("\n--- Results for sentence 2 / Risultati frase 2 ---")
        print("Total words / Parole totali:", len(words2))
        print("Unique words / Parole uniche:", len(set2))
        print("Set / Insieme:", set2)

        # Common words / Parole in comune
        common = set1 & set2
        print("\nCommon words / Parole in comune:", common)

        # Words only in sentence 1 / Solo in frase 1
        only_1 = set1 - set2
        print("Only in sentence 1 / Solo in frase 1:", only_1)

        # Words only in sentence 2 / Solo in frase 2
        only_2 = set2 - set1
        print("Only in sentence 2 / Solo in frase 2:", only_2)


if __name__ == "__main__":
    demo_basics()
    demo_operations()
    unique_words_analyzer()
