taller_python_softtek

|   |   |
|---|---|
|![Image of Guido](https://pbs.twimg.com/profile_images/424495004/GuidoAvatar.jpg)| Creador: Guido van Rossum Guido van Rossum es un científico de la computación, conocido por ser el autor del lenguaje de programación Python. Nació y creció en los Países Bajos (Holanda).

## Tipos Básicos
- Números:
    - 3 (entero) 
    - 15.57 (de coma flotante) 
    - 7 + 5j (complejos)
- Cadenas de texto: como “Hola Mundo”
- Valores booleanos: True (cierto) y False (falso).

```python
#Podemos revisar los tipos básicos de la siguient manera
e = 3 #entero
f = 15.57 #flotante
c = 7 + 5j #complejos
type(e)
type(f)
type(c)
s = "Hola Mundo!" #cadena
type(s)
b = True #boleano
type(b)
```
## Colecciones
### Listas
La lista es un tipo de colección ordenada. Sería equivalente a lo que en otros lenguajes se conoce por arrays, o vectores.
```Python
l = [22, True, “una lista”, [1, 2]] # creacion de una lista
l[0] # 22
l[1] # True
```
Las listas pueden contener listas
```Python
l = [1, [2, 3]]
type(l[1]) #<type 'list'>
l[1][0] #  2
```
### Tuplas
Su diferencia con las listas estriba en que las tuplas no poseen estos mecanismos de modificación a través de funciones tan útiles de los que hablábamos al final de la anterior sección.
Además son inmutables, es decir, sus valores no se pueden modificar una vez creada; y tienen un tamaño fijo.
A cambio de estas limitaciones las tuplas son más “ligeras” que las listas, por lo que si el uso que le vamos a dar a una colección es muy básico, puedes utilizar tuplas en lugar de listas y ahorrar memoria.
```Python
t = (1, 2, "hola", ["hi", "bye"], (1 , 2, 3))
```

### Diccionario
Los diccionarios, también llamados matrices asociativas, deben su nombre a que son colecciones que relacionan una clave y un valor.

```Python
d = {"Love Actually": "Richard Curtis", "Kill Bill": "Tarantino", "Amélie": "Jean-Pierre Jeunet"}
d["Love Actually"] # devuelve “Richard Curtis”
```

## Control de Flujo
###if
```Python
if mi_var== "Gustavo":
    print "sos Gustavo"
else:
    print "No eres gustavo"
#o en una sola linea
var = "par" if (num % 2 == 0) else "impar"
```

###Bucles

## Funciones
## Orientación a Objetos
## Programación Funcional
## Excepciones (si llegamos!!!)
