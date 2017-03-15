# ------------------------------------------------- ---------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
# Carlos Eduardo Tapudima de Oliveira 1715310030
# Frederico Victor Alfaia Rodrigues 1515200030
# Joelson Pereira Lima 1715310060
# Lucas Gabriel Silveira Duarte 1715310053
# Reinaldo da Silva Vargas 1715310054
# Walter Nobre da Silva Conceição 1715310057
#
# 16 - Faça um programa que receba o valor dos catetos de um triangulo, calcule e mostre o valor da hipotenusa.
# ------------------------------------------------- ---------
print("Para os valores dos catetos e o calculo correto, insira valores maiores que zero")
cateto1 = float(input("Digite a medida do primeiro cateto: "))
cateto2 = float(input("Digite a medida do segundo cateto: "))
hipo = float(((cateto1**2)+(cateto2**2))**(1/2))

print("O valor da hipotenusa é ", round(hipo, 2))
