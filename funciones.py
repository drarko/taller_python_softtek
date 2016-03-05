def saludar (arg_1 = "uno", arg_2="dos", *otros):
	print arg_1
	print arg_2
	print otros

saludar()

saludar(1, 2)

saludar("tres")

saludar("first", "second", "3ro", "4to", "5to")

def doble_return (p1, p2):
	return p1, p2

print doble_return(3, 4)
(mi_var_1, mi_var_2) = doble_return("Hola", 5)
print mi_var_1
print mi_var_2
