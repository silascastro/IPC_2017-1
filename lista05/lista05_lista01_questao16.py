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
#A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,
# 13,21,34,55,...Faça um programa que gere a série até que o
# valor seja maior que 500.
#-----------------------------------------------------------

prev_number = 0
next_number = 1
fibonacci = 0
count = 1

while fibonacci <= 500:
    if count == 1:
        print(prev_number, end = ' ')
    else:
        print(next_number, end = ' ')
        fibonacci = prev_number + next_number
        prev_number = next_number
        next_number = fibonacci
    count += 1
print(fibonacci)
