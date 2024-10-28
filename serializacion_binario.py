import pickle

binario=open("archivo_binario", "rb")

lista=pickle.load(binario)

print(lista)