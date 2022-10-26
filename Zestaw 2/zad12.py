# Zbudować napis stworzony z pierwszych znaków wyrazów z wiersza line. Zbudować napis stworzony z ostatnich znaków wyrazów z wiersza line.
 
tekst = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus nec arcu ac ex tincidunt faucibus. In interdum urna magna, in accumsan turpis congue eu"
tekst = tekst.replace(",", "")
tekst = tekst.replace(".", "")

pierwsze_litery = []
ostatnie_litery = []

for i in tekst.split():
    pierwsze_litery.append(i[0])
    ostatnie_litery.append(i[-1])

print(f"Słowo złożone z pierwszych liter: \n{''.join(pierwsze_litery)}\n")
print(f"Słowo złożone z ostatnich liter: \n{''.join(ostatnie_litery)}\n")