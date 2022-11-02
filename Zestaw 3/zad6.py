# Napisać program rysujący prostokąt zbudowany z małych kratek. Należy zbudować pełny string, a potem go wypisać. 
# Przykładowy prostokąt składający się 2x4 pól ma postać:
# +---+---+---+---+
# |   |   |   |   |
# +---+---+---+---+
# |   |   |   |   | 
# +---+---+---+---+

def grid(row, col):
  sep = "\n" + "+---"*col + "+\n"
  return sep + ("|   "*col + "|" + sep)*row

print("Wprowadz wysokosc:")
wysokosc = int(input())

print("Wprowadz szerokosc:")
szerokosc = int(input())

print(grid(wysokosc,szerokosc))