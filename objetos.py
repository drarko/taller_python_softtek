#objetos
class Coche:
	"""Abstraccion de los objetos coche"""
	def __init__(self, gasolina):
		self.gasolina = gasolina
		print "Tenemos: ",gasolina," litros"
	def arrancar(self):
		if self.gasolina > 0:
			print "Arranca"
		else:
			print "No Arranca"
	def conducir(self):
		if self.gasolina > 0:
			self.gasolina -= 1
			print "Quedan: ",self.gasolina, " litros"
		else:
			print "No se mueve"



mi_coche = Coche(3)
mi_coche.arrancar()
mi_coche.conducir()
mi_coche.conducir()
mi_coche.conducir()
mi_coche.conducir()
mi_coche.arrancar()

#herencia
class Instrumento:
	def __init__(self, precio):
		self.precio = precio
	def tocar(self):
		print "estamos tocando musica"

	def romper(self):
		print "eso lo pagas tu"
		print "Son: ", self.precio, " $$$"


class Bateria(Instrumento):
	pass

class Guitarra(Instrumento):
	pass


#herencia multiple
class Terrestre:
	def desplazar(self):
		print "El animal anda"

class Acuatico:
	def desplazar(self):
		print "el animal nada"

class Cocodrilo(Acuatico, Terrestre):
	pass

c = Cocodrilo()
c.desplazar()

#encapsulacion
class Encapsulacion:
	def publico(self):
		print "desde el metoo publico"
	def __privado(self):
		print "desde el metodo privado"

enc = Encapsulacion()
enc.publico()
enc._Encapsulacion__privado() """haciendo un poco de trampa"""
