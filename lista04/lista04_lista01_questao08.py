# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Grupo 10
# Walter Nobre da Silva Conceição 1715310057
#
# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.


c = input('write the price of the first product: R$ ')
c = int(c)
g = input('write de price of the second product: R$ ')
g = int(g)
t = input('write the price of the third product: R$ ')
t = int(t)

if c < g < t  or c < t < g and c:
    print('the first is the cheapest product, so buy it')
elif g < c < t or g < t < c:
    print('the second is the cheapest product, so buy it')
elif t < c < g or t < g < c:
    print('The third is the cheapest product, so buy it')
else:
    print('all products have the same price')


