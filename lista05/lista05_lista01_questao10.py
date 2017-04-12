# ----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Erik Atilio Silva Rey         1715310059
# Edson de Lima Barros          1715310043
# Enrique Leão Barbosa Izel     1715310048
# Diego Reis figueira           1515070169
# Diogo Roberto Duarte da Costa 1715310056
# Iury da Silva Coelho          1715310069
#
#10.Faça um programa que receba dois números inteiros e gere os números inteiros que estão no
#intervalo compreendido por eles.
#-----------------------------------------------------------------------------------------------------------------------

#Faça um programa que receba dois números inteiros e gere
# os números inteiros que estão no intervalo compreendido por eles.
#------------------------------------------------------------------

number1 = int(input('Digite um número inteiro: '))
number2 = int(input('Digite outro número inteiro: '))

if number1 < number2:
    diferenca = (number2 - number1)
    while number1 < diferenca:
        number1 = number1 + 1
        print(number1)

elif number1 > number2:
    diferenca = (number1 - number2)
    while number2 < diferenca:
        number2 = number2 + 1

        print(number2)


