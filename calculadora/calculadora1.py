from tkinter import *

raiz=Tk()

miframe=Frame(raiz)

miframe.pack()

#set estalece un valor en pantalla
# get obtine lo que haya en pantalla y unelo con lo que pulse


numeroque=StringVar()





	

#--------------------pantalla-------------------------------------

pantalla=Entry(miframe,textvariable=numeroque)

pantalla.grid(row=1, column=1, pady=10, padx=10, columnspan=4)
#CUADRO DE TEXTO POSICIONADO Y CON SEPARACION X
#con columnspan decimos que esa pantalla no ocupe solo una 
#columna si que ocupe cuatro para que se adapte a los botones


pantalla.config(background="black", fg="#ffffff", justify=
	"right")
#patalla es un objeto lo manipulamos con config y decimo que
#el cuadro de texto es negro la fuente es blanca y tenga
#una aliniacion hacia la derecha 


#----------------------acciones------------------------------

def pulsado(num):
	numeroque.set(numeroque.get()+num)
#creamos una funcion que reciba por parametros 
	#set estalece un valor en pantalla
# get obtine lo que haya en pantalla y lo une con lo que pulse






#---------------------botones fila 1-------------------------------

boton7=Button(miframe, text="7", width=3, command=lambda:pulsado("7") )
boton7.grid(row=2, column=1, pady=5, padx=5)
#boton que almacena un objeto y decimos que se encuentra en mi
#frame texto del boton 7 y con ancho 3 
#command ejecuta y almacena lo que devuelve la funcion lambda
#evita que la funcion se ejecute antes y que la active cuando 
#pulsemos en el boton


boton8=Button(miframe, text="8", width=3, command=lambda:pulsado("8") )
boton8.grid(row=2, column=2, pady=5, padx=5)
#comand de alguna manera ejecuta la funcion y lo almacena alli


boton9=Button(miframe, text="9", width=3, command=lambda:pulsado("9") )
boton9.grid(row=2, column=3, pady=5, padx=5)

botondiv=Button(miframe, text="/", width=3 )
botondiv.grid(row=2, column=4, pady=5, padx=5)

#------------------botones fila 2--------------------------------

boton4=Button(miframe, text="4", width=3, command=lambda:pulsado("4"))
boton4.grid(row=3, column=1, pady=5, padx=5)


boton5=Button(miframe, text="5", width=3, command=lambda:pulsado("5"))
boton5.grid(row=3, column=2, pady=5, padx=5)


boton6=Button(miframe, text="6", width=3, command=lambda:pulsado("6"))
boton6.grid(row=3, column=3, pady=5, padx=5)


botonmulti=Button(miframe, text="x", width=3)
botonmulti.grid(row=3, column=4, pady=5, padx=5)


#----------------fila 3 de botones-------------------------

boton1=Button(miframe, text="1", width=3, command=lambda:pulsado("1"))
boton1.grid(row=4, column=1, pady=5, padx=5)

boton2=Button(miframe, text="2", width=3, command=lambda:pulsado("2"))
boton2.grid(row=4, column=2, pady=5, padx=5)

boton3=Button(miframe, text="3", width=3, command=lambda:pulsado("3"))
boton3.grid(row=4, column=3, pady=5, padx=5)

botonres=Button(miframe, text="-", width=3)
botonres.grid(row=4, column=4, pady=5, padx=5)



#------------fila de botones 4----------------------------

botoncoma=Button(miframe, text=",", width=3)
botoncoma.grid(row=5, column=1, padx=5, pady=5)


boton0=Button(miframe, text="0", width=3, command=lambda:pulsado("0"))
boton0.grid(row=5, column=2, padx=5, pady=5)


botonigual=Button(miframe, text="=", width=3)
botonigual.grid(row=5, column=3, padx=5, pady=5)


botonsuma=Button(miframe, text="+", width=3)
botonsuma.grid(row=5, column=4, padx=5, pady=5)









raiz.mainloop()
#bucle infino para que el programa se mantega abierto hasta
#que lo decidamos cerrar