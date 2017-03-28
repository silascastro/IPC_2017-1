import math

numeros = input()

x1, y1 = map(float, numeros.split(' '))

numeros2 = input()

x2, y2 = map(float, numeros2.split(' '))

print('%.4f' %math.sqrt( pow(x2 - x1, 2) + pow(y2 - y1, 2) ))