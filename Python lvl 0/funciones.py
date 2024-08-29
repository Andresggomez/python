"""programas con funciones"""
import sys
import random

def saludo():
    """Pide nombre y saluda al usuario"""
    print("Hola, soy la funcion saludo()")
    nombre = input("Como te llamas: ")
    txt = "Mucho gusto "+nombre+" es un palcer saludarte, soy python3"
    return txt

#print(saludo())

num_list = [random.randint(-10000, 100000) for _ in range(50 )]

def maxnum(lista):
    """Pide una lista de numeros y calcular el valor maximo"""
    maximo = -1
    for numero in lista:
        if numero > maximo:
            maximo = numero
        else:
            continue
    return maximo

print(maxnum(num_list))

def fibbo(num):
    """Calcula la secuencia fiboonaci con el numero que indiquen"""
    num = list(range(1, num+1))
    print(num)
    tmp = 0
    for fibo in num:
        if num == 1:
            print(fibo)
        else:
            tmp = num[fibo - 1] + num[fibo - 2]
            print(tmp)
    return 0
#fibbo(4)

total = 0
suma = 0

while True:
    num = input("Ingrese un numero: ")
    if num == "done":
        break
    try:
        num = int(num)
    except TypeError:
        print("Bad Data")
        continue
    total = total + num
    suma = suma + 1


print (total, suma, total / suma)

sys.exit()
