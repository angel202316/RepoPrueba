from tkinter import *

raiz=Tk()

minombre=StringVar()
#variable que la asignaremos para que sea de texto y podamos modificarla 




miframe=Frame(raiz, width=400, height=400)
#aqui la varible almacena al frame el cual podemos manipularlo
#predefinimos que ese frame tengo un tamaño
miframe.pack()

nombre=Entry(miframe, textvariable=minombre)
#almacenador de entry que se localizará en mi frame
#textvariable es que la variable nombre ya se le asigne lo que haya
#almacenado en la otra variable minombre y especificamos que será de tipo texto 

nombre.grid(row=0, column=1, pady=10, padx=10)
#fila 0 dela columna 1 
#en este caso lo utilizamos para separar el nombre que aparece flotando
#con pady en la separacion del padding en vertical
#con padx en la separacion del padding en horizontal

nombre.config(fg="blue", justify="center")
#modificar con el metodo config valores de ese objeto
#fg color de letra y justify aliniacion del texto

password=Entry(miframe)

password.grid(row=1, column=1)



apellido=Entry(miframe)

apellido.grid(row=2, column=1, pady=10, padx=10)


direccion=Entry(miframe)

direccion.grid(row=3, column=1, pady=10, padx=10)


comentarios=Text(miframe, width=16, height=5)
#metodo Text es para agregar text pero con mas lineas y las propiedades
#de tamaño para definircelo y que no ocupe el predeterminado


comentarios.grid(row=4, column=1, pady=10, padx=10)
#en la posicion donde se encontrará ese cuadro de texto y su separacion







nombreL=Label(miframe, text="nombre :")
#almancen de cuadro estatico que lo encotraremos en miframe

nombreL.grid(row=0, column=0, sticky="e",pady=10, padx=10)
#fila 0 de la columna 0 osea al lado de el cuadro de texto
#sticky es para mover esos elementos aun direccion en concreto
#que está representada en puntos cardinales n,s,e,w tambien
#se puede utilizar ambos valores a la vez
#aqui para separar lo que ya definimos en la columnas y filas


passwordL=Label(miframe, text="Password :")

passwordL.grid(row=1, column=0, sticky="e", pady=10, padx=10)

password.config(show="*")
#show es como ocultar y el caracter que mostraremos




apellidoL=Label(miframe, text="apellido :")

apellidoL.grid(row=2, column=0, sticky="e", pady=10, padx=10)


direccionL=Label(miframe, text="direccion casa :")

direccionL.grid(row=3, column=0, sticky="e",pady=10, padx=10)


comentariosL=Label(miframe, text="Comentarios: ")

comentariosL.grid(row=4, column=0, sticky="e", pady=10, padx=10)


barravertical=Scrollbar(miframe, command=comentarios.yview)
#se crea un escroll osea una barra de desplazamiento que se 
#encuentra en mi frame y con commad especificamos que pertenece
#a la caja de texto y que será una barradesplazamiento vertical



barravertical.grid(row=4, column=2, sticky="n,s,e,w")
#esa barra de desplazamiento vertical se posicionará 
#al lado de la caja de texto y con sticky la ampliamos para que 
#se adapte y pueda ser visible 

comentarios.config(yscrollcommand=barravertical.set)
#entramos en la configuracion del cuadro de texto que le 
#asignamos la barra vertical y modificamos su comportamiento



def Codigoboton():
	minombre.set("angel :V")
#variable que con set se le agregará un valor de tipo texto



boton=Button(raiz, text="Enviar alv :v", command=Codigoboton)
#creamos una variable que almacena un metodo buton y se encuentra en raiz
#en ese metodo definimos un nombre con text y 
#command llamamos a ejecutar una funcion al presionar el boton


boton.pack()




#asignar










raiz.mainloop()