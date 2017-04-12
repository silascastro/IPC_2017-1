#----------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
# Evandro Padilha Barroso Filho     1715310009
# Gabriel Barroso da Silva Lima     1715310011
# Frederico Victor Alfaia Rodrigues 1515200030
# Felipe Eduardo Silva de Almeida   1715310031
# Felipe Guerreiro De Mello         1315120052
# Silas castro de Mendonça          1715310066
#
# 42) A série de RICCI difere da série de FIBONACCI porque os dois primeiros termos são
# fornecidos pelo usuário. Os demais termos são gerados da mesma forma que a série de
# FIBONACCI. Criar um algoritmo em PORTUGOL que imprima os N primeiros
# termos da série de RICCI e a soma dos termos impressos, sabendo-se que para existir
#esta série serão necessários pelo menos três termos. 
#
#----------------------------------------------------------------

prev_number = int(input("Digite um numero: "))
next_number = int(input("Digite outro numero: "))
fibonacci = 0
count = 1

n = int(input('Digite a quantidade de números da sequência fibonacci desejados: '))

while count <= n:
    if count == 1:
        print(prev_number, end = ' ')
    else:
        print(next_number, end = ' ')
        fibonacci = prev_number + next_number
        prev_number = next_number
        next_number = fibonacci
    count += 1
