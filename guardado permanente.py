import pickle

class Persona():

	def __init__(self, nombre, genero, edad):
		self.nombre=nombre
		self.genero=genero
		self.edad=edad

		print("se ha creado una persona con el nombre ", self.nombre)


	def __str__(self):
		return "{} {} {}".format(self.nombre, self.genero,
			self.edad) 

class Lista_persona():
	
	Lista=[]	

	def __init__(self):

		Listabinaria=open("guardadopermanente", "ab+")
		Listabinaria.seek(0)

		
		try:
			self.Lista=pickle.load(Listabinaria)
			print("se cargaron {} personas en el fichero".format(
				len(self.Lista)))
		except:
			print("el fichero esta vacio")	

		finally:
				Listabinaria.close()
				


	def agregarlista(self, personas):
		self.Lista.append(personas)  
							#con esto manipulamos la lista para que a
							#almacene lo que se le asigne en los paremetros 
							#del metodo o comportamiento
	def mostrarlista(self):
		for i in self.Lista:
			print(i) 

	def guardapersonasbinario(self):
		Listabinaria=open("guardadopermanente", "wb")
		pickle.dump(self.Lista, Listabinaria)
		Listabinaria.close()
		

	def mostrarbinarios(self):
		print("la siguiente informacion que se encuentra es ")
		for i in self.Lista:
			print(i)



listaI=Lista_persona()
persona=Persona("perez","hombre", 17)
listaI.agregarlista(persona)
listaI.mostrarbinarios()








					

					


