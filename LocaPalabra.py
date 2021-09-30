from tkinter import *
from tkinter import messagebox

def comprueba():
   if dueño.get()=="dueño" and mal.get()=="mal" and ojos.get()=="ojos" and desobedecer.get()=="desobedecer" and niños.get()=="niños" and corazon.get()=="corazón" and pedir.get()=="pedir" and dar.get()=="dar" and esencial.get()=="esencial":
       messagebox.showinfo("Correcto"," Buen trabajo!!!")
       dueño.set("")
       mal.set("")
       ojos.set("")
       esencial.set("")
       pedir.set("")
       dar.set("")
       desobedecer.set("")
       niños.set("")
       corazon.set("")

   else:
       messagebox.showwarning("Atención","Inténtalo usted puede!!!")
       dueño.set("")
       mal.set("")
       ojos.set("")
       esencial.set("")
       pedir.set("")
       dar.set("")
       desobedecer.set("")
       niños.set("")
       corazon.set("")



ventana=Tk("")

dueño=StringVar()
mal=StringVar()
ojos=StringVar()
corazon=StringVar()
esencial=StringVar()
pedir=StringVar()
dar=StringVar()
desobedecer=StringVar()
niños=StringVar()


ventana.title("LOCA PALABRA")
ventana.geometry("645x500")
ventana.resizable(0,0)
ventana.config(bg="orange",
               bd=5,
               relief="sunken")


imagen=PhotoImage(file="D:/Udemy-gmentoring/Python/INTERFAZ GRÁFICA/imagen.png")
label=Label(ventana,image=imagen).place(x=0,y=0)
et=Label(ventana,text="LOCA PALABRA",font=("Courier", 30, "bold"),fg="green",bg="gray").place(x=150,y=10)
et1=Label(ventana,text="Del libro famoso y popular 'El Principito', las siguientes oraciones tiene espacios en blanco que tiene "
                       "que completar\n con la palabra que falte. Esas palabras están desordenada."
                       "Coloquelas en donde crea que iría.""",bg="orange").place(x=10,y=70)

et2=Label(ventana,text="A JUGAR!!!!!!!",bg="orange",fg="green",font=("Courier", 20, "bold")).place(x=220,y=110)

et3=Label(ventana,text="Las siguientes palabras a utilizar en el texto son: ",bg="orange").place(x=10,y=150)
et3=Label(ventana,text="pedir , niños, dar, mal, desobedecer, dueño, esencial, corazón",bg="orange").place(x=10,y=180)

et4=Label(ventana,text="1) Eres el                                              de tu vida y tus emociones, nunca lo olvides. Para bien y para mal ",bg="gray").place(x=10,y=208)
en4=Entry(ventana,textvariable=dueño).place(x=65,y=210)
en4a=Entry(ventana,textvariable=mal).place(x=522,y=210)


et5=Label(ventana,text="2) Todas las personas mayores fueron al principio                                           (aunque pocas de ellas lo recuerdan). ").place(x=10,y=230)
en5a=Entry(ventana,textvariable=niños).place(x=275,y=230)

et6=Label(ventana,text="3) Cuando el misterio es demasiado impresionante, es imposible desobedecer). ",bg="gray").place(x=10,y=250)
en6a=Entry(ventana,textvariable=desobedecer).place(x=355,y=250)


et7=Label(ventana,text="4) Solo hay que pedir                                  a cada uno lo que cada uno puede dar. ").place(x=10,y=270)
en7a=Entry(ventana,textvariable=pedir).place(x=96,y=270)
en7b=Entry(ventana,textvariable=dar).place(x=410,y=270)


et8=Label(ventana,text="5) No se ve bien sino es con el corazón                              . Lo esencial                             es invisible a los ojos.",bg="gray" ).place(x=10,y=290)
en8a=Entry(ventana,textvariable=corazon).place(x=175,y=290)
en8b=Entry(ventana,textvariable=esencial).place(x=328,y=291)
en8c=Entry(ventana,textvariable=ojos).place(x=542,y=291)

boton=Button(ventana,text="Comprobar", command=comprueba,bd=3,bg="gray",cursor="hand2").place(x=320,y=320)


et4=Label(ventana,text="Oraciones célebres del gran libro 'El Principito' de 'Antoine de Saint-Exupéry'",bg="orange",font=("Courier",10,"bold") ).place(x=5,y=360)


ventana.mainloop()