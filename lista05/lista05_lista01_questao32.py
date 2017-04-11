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
# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
# Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
# ----------------------------------------------------------

fat = 1
num = int(input('Write a number: '))
while num > 0:
    if num <= 0:
        print(num)
    else:
        print(num)
    fat = num * fat
    num = num - 1
print(fat)
