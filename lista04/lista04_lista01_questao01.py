# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
# Felipe Eduardo Silva de Almeida	  1715310031
# Felipe Guerreiro Federico Vitor
# Federico Vitor
# Gabriel Alves
# Gabriel Barroso
#
# Faça um Programa que peça dois números e imprima o maior deles.
#  ----------------------------------------------------------

number1 = float(input("Primeiro número: "))
number2 = float(input("Segundo número: "))

if number1 > number2:
    print("O maior número é: ", number1)
else:
    if number1 < number2:
        print("O maior número é: ", number2)
    else:
        print("Os dois números são iguais")
