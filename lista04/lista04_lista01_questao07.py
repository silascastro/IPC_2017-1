#------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr.
#
# Vitor Summer Oliveira Pantaleão 	1715310042
# Vítor Simões Azevedo 			1715310025
# Wesley da Silva Rocha			1715310026
# Wilbert Luís Evangelista Marins 	1715310055
# Yuri Leandro de Aquino Silva 		1615100462
#
# Faça um Programa que leia três números
# e mostre o maior e o menor deles.
#------------------------------------------------------------------------------

n1 = float(input('Digite um numero: '))
n2 = float(input('Digite um numero: '))
n3 = float(input('Digite um numero: '))

lower = n1
if n2 < lower:
	lower = n2 
if n3 < lower:
	lower = n3
higher = n1
if n2 > higher:
	higher = n2
if n3 > higher:
	higher = n3

print('O menor é: %d' %lower)
print('O maior é: %d' %higher)
