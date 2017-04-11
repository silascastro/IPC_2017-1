# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Grupo 08
# Victor Summer Oliveira Pantaleao 1715310042
# Walter Nobre Da Silva Conceição  1715310057
# Wesley da Silva Rocha            1715310026
# Wilbert Luís Evangelista Marins  1715310055
# Yuri Leandro de Aquino Silva     1615100462
#
# Escreva um algoritmo em PORTUGOL que determine se um dado número N (digitado pelo usuário) é primo ou não.
# ----------------------------------------------------------

n = int(input("write a number: "))

if n == 2 or n != 1 and n % 2 == 1:
    print('prime number')
else:
    print('not')



