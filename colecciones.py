l = [22, 23 , True, [1, "pepe"]]

print (type(l))
print (l[2])
print (l[3][1])


t = ("hola", 1 , 2, l)
print (type(t))
print (t[3])


d = {"nombre":"Gustavo", "apellido":"Ghioldi", "edad":38, "lista":l, "tupla":t }

print (d["nombre"])
print (type(d))
print (type(d["edad"]))
print (type(d["tupla"]))

