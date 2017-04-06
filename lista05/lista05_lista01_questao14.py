# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
#
# Prof. Jucimar Jr 
#
# Lukas Michel Souza Mota               1715310018
# Marcus Vinicius Paes da Silva Santos 1515070060
# Matheus de Oliveira Marques           1515310514
# Natália Cavalcante Xavier             1715310021
# Nayara da Silva Cerdeira da Costa     1715310038
#
# Faça um programa que peça 10 números inteiros, 
# calcule e mostre a quantidade de números pares e a quantidade de números impares.  
#----------------------------------------------------------

even_numbers = 0
odd_numbers = 0
i = 0

numbers = []

print("Informe os valores: ")

while i < 10 :
    numbers.append(int(input()))
    i += 1

i = 0

while i < 10 :
    if (numbers[i] % 2 == 0) :
        even_numbers += 1
    else :
        odd_numbers += 1
    i += 1

print("Pares: %d" % even_numbers)
print("Impares: %d" % odd_numbers)
