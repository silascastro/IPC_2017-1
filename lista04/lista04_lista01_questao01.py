#--------------------------------------------------------------------------
#Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
# Diogo Duarte
# Felipe Eduardo Silva de Almeida   1715310031
# Felipe Guerreiro de Mello         1315120052
# Frederico Victor Alfaia Rodrigues 1515200030
# Gabriel Barroso da Silva Lima     1715310011
#
#Faça um Programa que peça dois números e imprima o maior deles. 
#-------------------------------------------------------------------------------------

a = float(input("digite um valor"))

b = float(input("digite outro valor"))

if a>b:

    print(a, "é maior que" ,b)

else:

    if b>a:
        print(b, "é maior que", a)
    else:

        print(b, "e", a, "são iguais")
