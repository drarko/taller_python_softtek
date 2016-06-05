#Funciones de oren superior
def saludar(lang):
	def saludar_es():
		print "Hola"
	def saludar_en():
		print "Hi"
	def saludar_fr():
		print "Salut"
	lang_func = {"es": saludar_es,
	"en": saludar_en,
	"fr": saludar_fr}
	return lang_func[lang]
f = saludar("es")
f()
saludar("fr")()

#Iteracions de orden superior
#map
def cuadrado(n):
	return n**2

l = [1, 2, 3]
l2 = map(cuadrado, l)
print l2

#filter
def es_par(n):
	return (n % 2.0 == 0)

l2 = filter(es_par, l)
print l2

#reduce
def sumar(x, y):
	return x+y

l2 = reduce(sumar, l)
print l2

#lambda
l2 = filter(lambda n: n % 2.0 ==0 , l)
print l2

#compresion de listas
l2 = [n**2 for n in l]
print l2

#generadores
l2 = (n**2 for n in l)
print l2
