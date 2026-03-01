# 06_data_structures --- 01 Lists Interactive Program

# 06_data_structures --- 01 Programma Interattivo Liste

------------------------------------------------------------------------

## 📌 Description / Descrizione

EN: This program is an interactive CLI (Command Line Interface) tool
designed to practice Python **lists**.

IT: Questo programma è uno strumento interattivo da terminale (CLI)
progettato per esercitarsi con le **liste** in Python.

It allows the user to / Permette all'utente di:

-   Add numbers to a list / Aggiungere numeri alla lista
-   Remove numbers from a list / Rimuovere numeri dalla lista
-   Sort the list / Ordinare la lista
-   Display minimum and maximum values / Mostrare valore minimo e
    massimo
-   Exit the program / Uscire dal programma

------------------------------------------------------------------------

## 🎯 Learning Objectives / Obiettivi di apprendimento

EN: This program helps you understand:

IT: Questo programma ti aiuta a comprendere:

-   What a **list** is in Python / Cos'è una **lista** in Python
-   How to use the main methods / Come usare i metodi principali:
    -   `append()`
    -   `remove()`
    -   `sort()`
    -   `min()`
    -   `max()`
-   Membership testing with `in` / Verifica di appartenenza con `in`
-   How Python evaluates empty lists / Come Python valuta le liste vuote
-   How to build a simple interactive menu / Come costruire un semplice
    menu interattivo

------------------------------------------------------------------------

## 🧠 Key Concepts Used / Concetti chiave utilizzati

### 1️⃣ List Creation / Creazione Lista

``` python
num = []
```

EN: Creates an empty list.\
IT: Crea una lista vuota.

------------------------------------------------------------------------

### 2️⃣ Adding Elements / Aggiunta Elementi

``` python
num.append(n)
```

EN: Adds a number at the end of the list.\
IT: Aggiunge un numero alla fine della lista.

------------------------------------------------------------------------

### 3️⃣ Removing Elements / Rimozione Elementi

``` python
if n in num:
    num.remove(n)
```

EN: Removes the first occurrence of a number if it exists.\
IT: Rimuove la prima occorrenza del numero se presente.

------------------------------------------------------------------------

### 4️⃣ Sorting / Ordinamento

``` python
num.sort()
```

EN: Sorts the list in ascending order.\
IT: Ordina la lista in ordine crescente.

------------------------------------------------------------------------

### 5️⃣ Checking If List Is Not Empty / Verifica Lista Non Vuota

``` python
if num:
```

EN: An empty list evaluates to `False`, a non-empty list evaluates to
`True`.\
IT: Una lista vuota vale `False`, una lista con elementi vale `True`.

------------------------------------------------------------------------

## ▶️ How to Run / Come Eseguire

From inside the folder / Dall'interno della cartella:

``` bash
python 01_lists.py
```

------------------------------------------------------------------------

## 💡 Suggested Commit Message / Messaggio Commit Consigliato

    Add interactive lists manager (append, remove, sort, min/max)

------------------------------------------------------------------------

## 🚀 Next Step / Prossimo Step

Continue with / Continua con:

-   `02_tuples.py`
-   `03_sets.py`
-   `04_dictionaries.py`

Then move to sorting algorithms / Poi passa agli algoritmi di
ordinamento 🚀
