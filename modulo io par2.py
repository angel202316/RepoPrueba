from io import open 

archivodetexto=open("archivo.txt", "r+")

#archivodetexto.seek(len(archivodetexto.read())/2)

#print(archivodetexto.read())

#archivodetexto.seek(10)
#print(archivodetexto.read())

lista_texto=archivodetexto.readlines()

print(lista_texto)

lista_texto[1]="esta linea fue agregada :v"

print(lista_texto)

archivodetexto.seek(0)

archivodetexto.writelines(lista_texto)
















