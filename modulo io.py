#metodo open para abrir o modificar un archivo externo
#from io import open 

#archivodetexto=open("archivo.txt", "r")

#texto=archivodetexto.readline()

#archivodetexto.close()

#print(texto)

from io import open 

archivodetexto=open("archivo.txt", "r")

archivodetexto.seek(len(archivodetexto.read())/2)

print(archivodetexto)

	#metodo str que permite convertir en cadena de 
	#texto la informacion de un objeto




