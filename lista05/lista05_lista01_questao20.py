# ----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
# Gabriel Nascimento de Oliveira    1715310052
# Gabriel de Queiroz Souza          1715310044
# Guilherme Silva de Oliveira       1715310034
# Hugo Thadeu Silva Cardoso         1715310013
# Jandinne Duarte de Oliveira       1015070265
#
#Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial
#a números inteiros positivos e menores que 16.

def fatorial(n):
   if n <= 1:
      return 1
   else:
      return n * fatorial(n-1)
n = int(input("Insira um numero natural n: "))

if n < 16:
    print ("O fatorial de n é: ", fatorial(n))
else:
    print("404 Not Found")