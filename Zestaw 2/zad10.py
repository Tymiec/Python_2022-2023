# Mamy dany napis wielowierszowy line. 
# Podać sposób obliczenia liczby wyrazów w napisie.
# Przez wyraz rozumiemy ciąg "czarnych" znaków, oddzielony od innych wyrazów białymi znakami (spacja, tabulacja, newline).

line = """jeden dwa trzy cztery piec szesc siedem osiem dziewiec
            jeden dwa trzy cztery piec szesc siedem osiem dziewiec
            jeden dwa trzy cztery piec szesc siedem osiem dziewiec
            jeden dwa trzy cztery piec szesc siedem osiem dziewiec"""

print("W tekście jest", len(line.split()), "słów")