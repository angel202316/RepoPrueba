class Persona():

	def __init__(self, nombre, edad, lugar):
		self.nombre=nombre

		self.edad=edad
		
		self.lugar=lugar


	def descripcion(self):
		print("su nombre es: ", self.nombre, "su edad es: ", self.edad,
		 "vive en ", self.lugar )

class Empleado(Persona):

	def __init__(self, salario, antiguedad, nombreE,
		edadE, lugarE):

		super().__init__(nombreE, edadE, lugarE)

		self.salario=salario
		
		self.antiguedad=antiguedad

	def descripcion(self):
		super().descripcion()
		print("y salario ", self.salario, "con antiguedad", 
		self.antiguedad )


Angel=Empleado(1500, 20, "Angel", 17, "caracas")	

Angel.descripcion()




