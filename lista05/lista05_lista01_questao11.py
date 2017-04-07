# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Evandro Padilha Barroso Filho     1715310009 
# Gabriel Barroso da Silva Lima     1715310011
# Frederico Victor Alfaia Rodrigues 1515200030 
# Felipe Eduardo Silva de Almeida   1715310031 
# Felipe Guerreiro De Mello         1315120052 
# Silas castro de Mendonça          1715310066
#
#11.Altere o programa anterior para mostrar no final a soma dos números.
#
# ----------------------------------------------------------

number = int(input("Digite um número inteiro: "))
number_2 = int(input("Digite um número inteiro: "))
acumulator = 0

if number > number_2:
    higher = number
    lower = number_2

else:
    higher = number_2
    lower = number

while lower < (higher - 1):
    lower = lower + 1
    acumulator = acumulator + lower
    print(lower)

print(acumulator)

