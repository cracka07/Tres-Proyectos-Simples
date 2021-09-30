from tkinter import *
import random
import time

numAl = random.randint(1, 10)

def adivinador():

    # prediccion.set(0)
    numero = prediccion.get()

    if numero < numAl:

        print(cumplir.set("Intente otra vez, este número es muy pequeño"))

    elif numero > numAl:

        print(cumplir.set("Intente otra vez, este número es muy grande"))

    elif numero == numAl:
        print(cumplir.set(f"FELICITACIONES. NÚMERO CORRECTO: {numAl}!!!"))

        prediccion.set("")





root=Tk()

cumplir=StringVar()
prediccion=IntVar()



root.geometry("490x400")
root.resizable(0,0)
root.title("Adivinador")
root.config(bg="yellow")
root.iconbitmap("D:/Udemy-gmentoring/Python/adivinaNumero/adivina_n.ico")

texto0="""Adivinador"""
texto="""Bienvenido a este entretenido juego, en el que usted va hacer el 
protagonista. Tendrá que adivinar un número que es generado al azar."""

et1=Label(root,text=f"{texto0}",font=("Courier", 25, "bold"),fg="green",bg="yellow").place(x=100,y=15)
et2=Label(root,text=f"{texto}",bg="yellow",font=("Courier", 8, "bold")).place(x=10,y=100)

msg = Label(root, text=f"Adivina el número: ",bg="yellow").place(x=15, y=200)
a=Entry(root,textvariable=prediccion,width=10).place(x=126, y=200)

c = Label(root,textvariable=cumplir,bg="plum",width=65,bd=5).place(x=10, y=260)

boton = Button(root, text="Comprobar", command=adivinador,cursor="hand2",bd=3,bg="orange").place(x=200,y=195)


root.mainloop()