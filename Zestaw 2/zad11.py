# Podać sposób wyświetlania napisu word tak, aby jego znaki były rozdzielone znakiem podkreślenia.

word = "Losowytekst"

tekst_na_lista = (list(word))
tekst_na_lista = "_".join(tekst_na_lista)

print(tekst_na_lista)