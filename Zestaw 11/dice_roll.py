# Napisać program z GUI, który symuluje rzut kostką sześcienną. 
# Program powinien mieć przycisk uruchamiający rzut kostką i etykietę wyświetlającą wynik 
# (liczba od 1 do 6 lub odpowiedni obrazek).
from tkinter import *
import random

frame = Tk()
frame.configure(bg="white")
frame.geometry("720x360")
def roll():
    dots = ["1","2","3","4","5","6"]
    label.configure(
        text=f"{random.choice(dots)}")
    label.pack()

roll_button = Button(frame, text="Rzuć kostkom!", width=20, height=2, font=15, bg="gray", bd=2, command=roll)
roll_button.pack(padx=10, pady=15)  
  
label = Label(frame, font=("arial", 200), bg="white", fg="black")
  
frame.mainloop()