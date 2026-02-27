# Temperature Converter - Celsius to Fahrenheit
# Convertitore di temperatura - da Celsius a Fahrenheit

# Ask the user to enter the temperature in Celsius
# Chiede all'utente di inserire la temperatura in gradi Celsius
celsius = float(input("Insert temperature in Celsius: "))

# Conversion formula
# Formula di conversione
fahrenheit = (celsius * 9/5) + 32

# Print the result formatted with 2 decimal places
# Stampa il risultato formattato con 2 cifre decimali
print(f"{celsius:.2f}°C correspond to {fahrenheit:.2f}°F")