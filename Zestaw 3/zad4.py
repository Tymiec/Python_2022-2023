# Napisać program pobierający w pętli od użytkownika liczbę rzeczywistą x (typ float) i wypisujący x oraz trzecią potęgę x. 
# Zatrzymanie programu następuje po wpisaniu z klawiatury stop. 
# Jeżeli użytkownik wpisze napis zamiast liczby, to program ma wypisać komunikat o błędzie i kontynuować pracę.

while True:
    string_in = input("Wprowadź liczbę lub wpisz \"stop\" aby zatrzymać pracę programu: ")
    if string_in.lower() == "stop":
        break
    try:
        num_in = float(string_in)
        print(f"\nWprowadzona liczba:", num_in)
        num_in = num_in ** 3
        print(f"Wprowadzona liczba do ^3: ", num_in,"\n")
    except:
        print("\nNie wprowadzono liczby ani nie przerwano działania programu komedną \"stop\", wprowadź liczbę lub zatrzyma program komendą \"stop\":\n")