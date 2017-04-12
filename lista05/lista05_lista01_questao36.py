# -----------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
# Gabriel Nascimento de Oliveira    1715310052
# Gabriel de Queiroz Souza          1715310044
# Guilherme Silva de Oliveira       1715310034
# Hugo Thadeu Silva Cardoso         1715310013
# Jandinne Duarte de Oliveira       1015070265
# Joelson Pereira Lima              1715310060
#
# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o 
# fatorial várias vezes e limitando o fatorial números inteiros positivos e menores que 16.
# -----------------------------------------------------------------------------------------
a = int(input())
b = int(input())
c = int(input())
count = b

while count <= c:
    print(a , "X" , count, "=", a*count)
    count +=1
