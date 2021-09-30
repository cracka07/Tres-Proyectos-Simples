from tkinter import *
import random
import time

def ganador():
   computadora.set(random.choice(["Piedra", "Papel", "Tijera"]))

   if (opcion.get()==1 and computadora.get()=="Tijera") or (opcion.get()==3 and computadora.get()=="Papel") or (opcion.get()==2 and computadora.get()=="Piedra"):


       print(lb1.set("GANASTE!!"))



   elif (opcion.get()==1 and computadora.get()=="Piedra") or (opcion.get()==3 and computadora.get()=="Tijera") or (opcion.get()==2 and computadora.get()=="Papel"):
       print(lb1.set("EMPATE!!"))


   elif (opcion.get()==3 and computadora.get()=="Piedra") or (opcion.get()==2 and computadora.get()=="Tijera") or (opcion.get()==1 and computadora.get()=="Papel"):
       print(lb1.set("Perdiste!!"))


   else:
       print(lb1.set("Error!\n vuelve a ingresar\n los datos"))
       print(computadora.set(""))





root=Tk()
opcion=IntVar()
computadora=StringVar()
lb1=StringVar()
img=PhotoImage(file="D:/Udemy-gmentoring/Python/piedra, papel o tijera/images1.gif")
Label(root,image=img,bd=10,bg="orange").place(x=370,y=190)

root.title("Piedra, papel o tijera")
root.geometry("500x400")
root.resizable(0,0)
root.config(bg="orange")



texto="""
Bievenidos a este nuevo juego muy popular. Usted jugará contra la computadora y ¿cómo?:
      
Deberá ingresar una opción entre piedra, papel o tijera para luego conocer el resultado."""
text1="""¿LISTO? A JUGAR!!!"""
l=Label(root,text=texto,bg="orange").place(x=5, y=10)
b=Label(root,text=text1,font=("Courier",15,"bold"),bg="orange").place(x=160,y=90)

us=Label(root,text="Seleccione una opción: ",bg="orange").place(x=10,y=150)

# en=Entry(root,textvariable=opcion,bg="gray",fg="white").place(x=10,y=180)
r=Radiobutton(root, text="Piedra", value=1, variable=opcion,bg="orange",cursor="hand2").place(x=10,y=180)
r1=Radiobutton(root, text="Papel", value=2,variable=opcion,bg="orange",cursor="hand2").place(x=80,y=180)
r2=Radiobutton(root, text="Tijera", value=3,variable=opcion,bg="orange",cursor="hand2").place(x=150,y=180)

lb=Label(root,text="La computadora ha escogido: ",bg="orange").place(x=10,y=210)
en=Entry(root,textvariable=computadora,bg="gray",fg="white",state=DISABLED).place(x=10,y=240)

boton=Button(root,text="Jugar",command=ganador,width=15,bd=5,bg="orange",fg="white",font=("Courier",10,"bold")).place(x=200,y=210)

label=Label(root,textvariable=lb1,bg="plum",width=20,height=5,font=("Courier",10, "bold")).place(x=100,y=290)
root.mainloop()