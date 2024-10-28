from tkinter import *

raiz=Tk() #almacena lo que hay en la ventana

raiz.title("mi primer programa")#titulo de la ventana

raiz.resizable(1,1)#nos permite modicar la ventana en tamaño(si o no)
#recibe parametro buleanos o 0 y 1 

raiz.iconbitmap("cplus.ico")#icono de la ventana
#y direccion mas el nombre del icono

raiz.geometry("650x350")
#tamaño por defecto del programa 

raiz.config(bg="red")#color de fondo del programa bg background
#y color del programa en ingles



raiz.mainloop() #bucle infinito que mantiene la venta abierta
#debe estar de ultimo lugar