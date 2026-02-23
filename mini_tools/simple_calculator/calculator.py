"""
Simple Calculator / Calcolatrice Semplice
-----------------------------------------
🇬🇧 A small terminal calculator that performs +, -, *, / on two numbers.
🇮🇹 Una piccola calcolatrice da terminale che esegue +, -, *, / su due numeri.

Author / Autore: Mattia Adamo
Repo: python-foundations (mini_tools/simple_calculator)
"""

# 🇬🇧 Function to safely read a number from the user.
# 🇮🇹 Funzione per leggere in modo sicuro un numero inserito dall'utente.
def read_number(prompt: str) -> float:
    while True:
        user_input = input(prompt)
        try:
            return float(user_input)
        except ValueError:
            # 🇬🇧 If the input is not a valid number, ask again.
            # 🇮🇹 Se l'input non è un numero valido, richiedilo.
            print("❌ Input non valido. Inserisci un numero (es. 12.5).")
            print("❌ Invalid input. Please enter a number (e.g., 12.5).")


# 🇬🇧 Function to read a valid operator (+, -, *, /).
# 🇮🇹 Funzione per leggere un operatore valido (+, -, *, /).
def read_operator(prompt: str) -> str:
    valid_ops = {"+", "-", "*", "/"}
    while True:
        op = input(prompt).strip()
        if op in valid_ops:
            return op

        # 🇬🇧 If the operator is invalid, show the allowed ones.
        # 🇮🇹 Se l'operatore non è valido, mostra quelli consentiti.
        print("❌ Operazione non valida. Scegli tra: +, -, *, /")
        print("❌ Invalid operation. Choose one of: +, -, *, /")


# 🇬🇧 Function that performs the calculation.
# 🇮🇹 Funzione che esegue il calcolo.
def calculate(num1: float, num2: float, operator: str):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        # 🇬🇧 Handle division by zero.
        # 🇮🇹 Gestione divisione per zero.
        if num2 == 0:
            return "Errore: non è possibile dividere per zero / Error: cannot divide by zero"
        return num1 / num2

    # 🇬🇧 This should not happen because we validate the operator before.
    # 🇮🇹 Questo non dovrebbe accadere perché validiamo l'operatore prima.
    return "Operazione non valida / Invalid operation"


# 🇬🇧 Main program entry point.
# 🇮🇹 Punto di ingresso del programma principale.
def main():
    print("=== Calcolatrice Semplice / Simple Calculator ===")

    # 🇬🇧 Read the two numbers from the user.
    # 🇮🇹 Leggi i due numeri dall'utente.
    num1 = read_number("Inserisci il primo numero / Enter the first number: ")
    num2 = read_number("Inserisci il secondo numero / Enter the second number: ")

    # 🇬🇧 Read the operator.
    # 🇮🇹 Leggi l'operatore.
    operator = read_operator("Scegli un'operazione (+, -, *, /): ")

    # 🇬🇧 Perform calculation and show result.
    # 🇮🇹 Esegui il calcolo e mostra il risultato.
    result = calculate(num1, num2, operator)
    print("\nRisultato / Result:", result)


# 🇬🇧 Run the program only if executed directly (not imported).
# 🇮🇹 Esegui il programma solo se lanciato direttamente (non importato).
if __name__ == "__main__":
    main()