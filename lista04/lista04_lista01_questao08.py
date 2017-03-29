# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Grupo 10
# Walter Nobre da Silva Conceição 1715310057
#
# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.


x = input('write the price of the first product: R$ ')
x = int(x)
y = input('write de price of the second product: R$ ')
y = int(y)
z = input('write the price of the third product: R$ ')
z = int(z)

if x < y < z  or x < z < y and x:
    print('the first is the cheapest product, so buy it')
elif y < x < z or y < z < x:
    print('the second is the cheapest product, so buy it')
elif z < x < y or z < y < x:
    print('The third is the cheapest product, so buy it')
else:
    print('all products have the same price')


