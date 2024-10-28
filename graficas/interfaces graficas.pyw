from tkinter import *

raiz=Tk() #almacena lo que hay en la ventana

raiz.title("mi primer programa")#titulo de la ventana

raiz.resizable(1,1)#nos permite modicar la ventana en tamaño(si o no)
#recibe parametro buleanos o 0 y 1 

#raiz.iconbitmap("cplus.ico")#icono de la ventana
#y direccion mas el nombre del icono

raiz.geometry("650x350")
#tamaño por defecto del programa hay que especificarselo pero al
#frame por este tamaño es adaptable 

raiz.config(bg="yellow")#color de fondo del programa bg background
#y color del programa en ingles

miframe=Frame() #nos permitira crear cosas en la ventana

miframe.pack(fill="both", expand="1")#nos permitira empaquetar ese frema a la ventana
#principal en esta zona nos permite anclar el frame en una
#lugar arriba o en varias direcciones a la vez 
#anchor maneja puntos cardinales n,s,w,e combinando con size y su lugar en ingles
#rellenarlo la raiz fill
#expand espande la (y) de fill dandole positivo
#both en las dos direcciones en fill

miframe.config(bg="green")#color del frame en ingles

miframe.config(width="650", height="350")#tamaño del frame
#debe ir separado con comaas


miframe.config(relief="groove")
#estos son los borde puede ser del frame o la raiz hay q especificar
#borde groove, sunken

miframe.config(bd="34")
#con esto le decimos que el borde sea de x tamaño por defecto este es 0

miframe.config(cursor="pirate")
#cambiar el estilo del cursos cuando lo posicionamos en el frame o en la raiz
#cursor hand2, pirate

raiz.mainloop() #bucle infinito que mantiene la venta abierta
#debe estar de ultimo lugar