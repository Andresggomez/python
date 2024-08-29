"""Edgar Andres Guarin Gomez"""
import sys

# Programas basicos en lenguaje python 3

# 1. Convertir pisos de EE.UU a modelo USA
inp = input('Piso Europeo? ')
usf = int(inp) + 1
print('En USA estaria en el piso', usf)

# 2. Numeros pares o impares
num = input('Ingrese un numero: ')
if int(num) % 2 == 0 :
    print(num, 'es un numero par')
else:
    print(num, 'es un numero impar')

# 3. Saludo al usuario
name = input('Como te llamas: ')
print('Hola', name+' es un gusto saludar!')

# 4. Convertir horas * trabajo en un pago
horas = input('Cuantas horas trabajo este semana: ')
COSTO_HORA = 4333
pagototal = int(horas) * COSTO_HORA
print('Esta semana su pago sera de', pagototal)

# 5. Comprobar que un numero es mayor que 1 y menor a 100
x = int(input('Ingresa un numero: '))
if x > 1 :
    print('Mayor a 1')
    if x < 100 :
        print(x, 'Es menor que 100')
    else :
        print(x, 'Es mayor a 100')

# 6. sar try/except en el programa de horas para que esten numeros

horas = input('Cuantas horas trabajo este semana: ')
costo_hora = input('Costo por hora: ')
try:
    horas = int(horas)
    costo_hora = int(costo_hora)
except ImportError:
    print('Error, no escribio un numero')
    sys.exit()

pagototal = horas * costo_hora
print('Esta semana su pago sera de', pagototal)
