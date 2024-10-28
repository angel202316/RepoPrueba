from tkinter import *

raiz=Tk()

miframe=Frame(raiz, width=400, height=500)
#creamos el contenedor del frama y especificamos que pertenece a raiz
# y al frame le especificamos un tamaño

miframe.pack()
#con esto empaquetamos el frame a la raiz

mimage=PhotoImage(file="off.png")

milabel=Label(miframe, image=mimage)

#milabel=Label(miframe, text="ostia pero mi miren ps :v", 
#	fg="red", font=("Comic Sans MS", 18))

#el contenedor que nos permitirá manipular y almacenar en el 
#especificando en contenedor donde se realizaran los cambios
#text nos permite mostrar texto
#fg es el color de la fuente 
#font el tipo de fuente que utilizaremos y el tamaño debe ir en este orden
#Label mayuscula



milabel.place(x=100, y=100)
#metodo place para ubicar el texto atravez de coordenadas

#Label para abreviar si no lo utilizaremos de nuevo label
#Label(miframe, text="ostia pero").place(x=100, y=100)


raiz.mainloop()