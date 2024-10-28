#class Coche():
#	def __init__(self):

#		self.largo=150
#		self.ruedas=4
#		self.ancho=150
#		self.enmarcha=False
#
#	def rum(self):
#			self.enmarcha=True

#coche1=Coche()

#coche1.rum()


#print(coche1)				

class Vehiculos():

	def __init__(self, marca, modelo):
		self.marca=marca
		self.modelo=modelo
		self.tamaño=150
		self.enmarcha=False

	def arranque(self):
		self.enmarcha=True

	def ancho(self, tamaño):
		self.tamaño=tamaño

class Moto(Vehiculos):
	pass

moto1=Moto("centauro", "xxx")	

print(moto1.modelo)

moto1.ancho(220)

print(moto1.tamaño)		


class MotoElectica(Vehiculos):
	def __init__(self, marca, modelo):
		super().__init__(marca, modelo)
		self.bateria=False
		self.ruedas=4

	def Carga(self):	
		self.bateria=True
	

class CarroE(MotoElectica,Vehiculos):
	
	pass

carroe1=CarroE("renaul", "930")

print(carroe1.enmarcha)

carroe1.arranque()

print(carroe1.enmarcha)

print(isinstance(carroe1, Vehiculos))





































		