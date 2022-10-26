# Posortować wyrazy z napisu line raz alfabetycznie, a raz pod względem długości. Wskazówka: funkcja wbudowana sorted().

line = "jeden dwa trzy cztery piec szesc siedem osiem dziewiec"

print(f"Wyrazy posortowane alfabetycznie:\n{sorted(line.split())}\n")

print(f"Wyrazy posortowane od najkrótszego do najdłuższego:\n{sorted(line.split(), key=len)}")