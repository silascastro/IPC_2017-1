# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Grupo 08
# Victor Summer Oliveira Pantaleao 1715310042
# Walter Nobre Da Silva Conceição  1715310057
# Wesley da Silva Rocha            1715310026
# Wilbert Luís Evangelista Martins 1715310055
# Yuri Leandro de Aquino Silva     1615100462
#
#A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,
# 13,21,34,55,...Faça um programa que gere a série até que o
# valor seja maior que 500.
#-----------------------------------------------------------

cont1 = 1
fib = 0
anterior = 0
posterior = 1
print(0)
print(1)

while cont1 < 15:
    fib = anterior + posterior
    anterior = posterior
    posterior = fib
    cont1 = cont1 + 1
    print(fib)
