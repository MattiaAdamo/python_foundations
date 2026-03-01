# 06_data_structures --- 02 Tuples

  -------------
  \# 🇬🇧 ENGLISH
  VERSION

  \## 📌
  Description

  This script
  introduces
  **tuples**,
  an ordered
  and immutable
  data
  structure in
  Python.

  Unlike lists,
  tuples cannot
  be modified
  after
  creation.
  -------------

## 🎯 Learning Objectives

After this program you will understand:

-   What a tuple is
-   The difference between lists and tuples
-   Indexing and slicing
-   Unpacking (multiple assignment)
-   Immutability and why it matters
-   When to use tuples

------------------------------------------------------------------------

## 🧠 Key Concepts Used

### Tuple Creation

``` python
point = (10, 20)
```

Creates a tuple with two values.

------------------------------------------------------------------------

### Indexing

``` python
point[0]
```

Access elements by index.

------------------------------------------------------------------------

### Slicing

``` python
numbers[1:4]
```

Extract part of a tuple.

------------------------------------------------------------------------

### Unpacking

``` python
x, y = point
```

Assign multiple values at once.

------------------------------------------------------------------------

### Immutability

``` python
point[0] = 100  # TypeError
```

Raises an error because tuples cannot be modified.

------------------------------------------------------------------------

## Tuple vs List

  Feature                 List              Tuple
  ----------------------- ----------------- -------------------
  Ordered                 Yes               Yes
  Mutable                 Yes               No
  Can be dictionary key   No                Yes (if hashable)
  Performance             Slightly slower   Slightly faster

------------------------------------------------------------------------

## ▶️ How to Run

From inside the folder:

``` bash
python 02_tuples.py
```

------------------------------------------------------------------------

## 💡 Suggested Commit Message

    Add tuples basics with immutability and unpacking examples

------------------------------------------------------------------------

# 🇮🇹 VERSIONE ITALIANA

## 📌 Descrizione

Questo script introduce le **tuple**, una struttura dati ordinata e
immutabile in Python.

A differenza delle liste, le tuple non possono essere modificate dopo la
creazione.

------------------------------------------------------------------------

## 🎯 Obiettivi di apprendimento

Dopo questo programma comprenderai:

-   Cos'è una tuple
-   La differenza tra liste e tuple
-   Indicizzazione e slicing
-   Unpacking (assegnazione multipla)
-   Immutabilità e perché è importante
-   Quando usare le tuple

------------------------------------------------------------------------

## 🧠 Concetti chiave utilizzati

### Creazione Tuple

``` python
point = (10, 20)
```

Crea una tuple con due valori.

------------------------------------------------------------------------

### Indicizzazione

``` python
point[0]
```

Accede agli elementi tramite indice.

------------------------------------------------------------------------

### Slicing

``` python
numbers[1:4]
```

Estrae una parte della tuple.

------------------------------------------------------------------------

### Assegnazione multipla (Unpacking)

``` python
x, y = point
```

Assegna più valori contemporaneamente.

------------------------------------------------------------------------

### Immutabilità

``` python
point[0] = 100  # TypeError
```

Genera un errore perché le tuple non sono modificabili.

------------------------------------------------------------------------

## Confronto Tuple vs Lista

  Caratteristica                    Lista                   Tuple
  --------------------------------- ----------------------- ------------------------
  Ordinata                          Sì                      Sì
  Mutabile                          Sì                      No
  Può essere chiave di dizionario   No                      Sì (se hashable)
  Performance                       Leggermente più lenta   Leggermente più veloce

------------------------------------------------------------------------

## ▶️ Come Eseguire

Dall'interno della cartella:

``` bash
python tuples.py
```

------------------------------------------------------------------------

## 💡 Messaggio Commit Consigliato

    Add tuples basics with immutability and unpacking examples
