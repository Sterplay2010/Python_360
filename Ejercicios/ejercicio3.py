'''

Obtener el radio y longitud de un circulo en python

'''


import math
r = float(input("Ingrese el radio: "))
area = math.pi*r**2
longitud = 2*math.pi*r
print(f"El area es {area:.1f} y la longitud es {longitud:.1f}")