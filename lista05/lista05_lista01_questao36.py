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
# Desenvolva um programa que faça a tabuada de um número qualquer 
# inteiro que será digitado pelo usuário, mas a tabuada não deve 
# necessariamente iniciar em 1 e terminar em 10, o valor inicial e 
# final devem ser informados também pelo usuário, conforme exemplo abaixo:
#   Montar a tabuada de: 5
#   Começar por: 4
#   Terminar em: 7
#   Vou montar a tabuada de 5 começando em 4 e terminando em 7:
#   5 X 4 = 20
#   5 X 5 = 25
#   5 X 6 = 30
#   5 X 7 = 35
#
#----------------------------------------------------------------

table = int(input())
start = int(input())
end = int(input())
count = start
print("Vou montar a tabuada de", table, "começado em", start, "e terminando em", end)
while count <= end:
    print(table , "X" , count, "=", table*count)
    count +=1
