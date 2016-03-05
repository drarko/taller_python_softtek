#IF
mi_variable = "gustavo"

if mi_variable == "gustavo":
	print "Hola Gustavo"
elif mi_variable=="juan":
	print "hola Juan"
else:
	print "Hola Mundo"
print "Muchas gracias"

num =1
var = "par" if (num%2 == 0) else "impar"
print var

#WHILE
edad = 0
while edad < 18:
	edad = edad + 1
	print "Felicidades. tienes "+ str(edad)

#for

secuencia = ["uno", "dos", "tres"]

for elemento in secuencia:
	print elemento
