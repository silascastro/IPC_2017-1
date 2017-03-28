
#------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr.
#
# João Vitor de Cordeiro B. Gonçalves   1515140036
# Joelson Pereira Lima                  1715310060
# Judá Salazar Braga                    1515200050
# Kethelen Tamara Braga Barbosa         1525212002
# Lucas Gabriel Silveira                1715310053 

import math

numeros = input()

x1, y1 = map(float, numeros.split(' '))

numeros2 = input()

x2, y2 = map(float, numeros2.split(' '))

print('%.4f' %math.sqrt( pow(x2 - x1, 2) + pow(y2 - y1, 2) ))
