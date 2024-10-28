import pickle

class Vehiculo():
	def __init__(self, marca, modelo):
		self.marca=marca
		self.modelo=modelo
	
	def descripcion(self):
		print("la marca es: ", self.marca, "y el modelo: ", self.modelo)	
		
carro1=Vehiculo("renaul", "xxx")
carro2=Vehiculo("toyota", "xx1")
carro3=Vehiculo("mustang", "xx2")

vehiculo=[carro1, carro2, carro3]




binario_objetos=open("archivo_binario1", "wb")

pickle.dump(vehiculo, binario_objetos)

binario_objetos.close()


binario_objetos1=open("archivo_binario1", "rb")

lista_objetos=pickle.load(binario_objetos1)

for i in lista_objetos:
	print(i.descripcion())





