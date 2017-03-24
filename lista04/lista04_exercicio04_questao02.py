#-----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr.
# Erik Atlio Silva Rey                  1715310059
# Edson de Lima Barros                  1715310043
# Enrique Leão Barbosa Izel             1715310048
# Evandro Padilha Barroso Filho         1715310009
# Fang Yao                              1115180236
#
#2.Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
#-----------------------------------------------------------------------------------------------------------------------
number01 = int(input("Digite um número: "))
if number01 < 0:
    print(number01, "É negativo")

if number01 > 0:
    print(number01, "É positivo")
else:
    if number01 == 0:
        print(number01, "É igual a ZERO")
