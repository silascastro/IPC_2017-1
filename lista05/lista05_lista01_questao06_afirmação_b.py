# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
#
# Prof. Jucimar Jr 
#
# Lukas Michel Souza Mota 1715310018
#
# Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.
# Depois modifique o programa para que ele mostre os números um ao lado do outro. 
#----------------------------------------------------------

number = 1
number_str = ""

while number < 21:
    number_str = number_str + str(number)
    number = number + 1

print(number_str)
