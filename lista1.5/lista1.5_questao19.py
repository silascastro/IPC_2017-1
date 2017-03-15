# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
# Diego Reis Figueira                1515070169
# Gabriel Barroso da Silva Lima      1715310011
# Rodolfo gomes do nascimento        1515200550
# Victor Hugo de Oliveira Carreira   1715310063
# Wesley da Silva Rocha              1715310026
#
# Sabe-se que para iluminar de maneira correta os cômodos de uma casa,
# para cada m², deve-se usar 18 W de potência. Faça um programa que
# receba as duas dimensões de um cômodo (em metros), calcule e mostre
# a sua área (em m²) e a potência de iluminação que deverá ser
# utilizada.
# ----------------------------------------------------------

length = float(input('Largura: '))
width = float(input('Comprimento: '))

area = length * width
potency = 18 * area

print('Area: %.2f metros quadrados' %area)
print('Potência: %.2f watt' %potency)
