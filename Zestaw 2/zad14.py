# Znaleźć: (a) najdłuższy wyraz, (b) długość najdłuższego wyrazu w napisie line.

str = "Lorem ipsum dolor sit amet consectetur"
str = str.split (' ')

len(str[0])
max = 0
slowo = ""

for words in str:
    if (len(words)) > max:
        max = (len(words))
        slowo = words
    

print("Najdłuższe słowo ma:", max, "liter\n")
print("Najdłuższym słowem jest:", slowo)


