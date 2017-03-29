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
# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao
# usuário o valor do saque e depois informar quantas notas de cada valor serão
# fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor
# mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar
# com a quantidade de notas existentes na máquina.
#
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100,
# uma nota de 50, uma nota de 5 e uma nota de 1;
#
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100,
# uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
#  ----------------------------------------------------------

# Parâmetros inicias para o funcionamento do código
sake = int(input("Digite o valor do saque: "))
rest100 = sake % 100
rest50 = rest100 % 50
rest10 = rest50 % 10
rest5 = rest10 % 5
rest1 = rest5 % 1

if 600 >= sake >= 10:
    if rest100 > 0 or sake % 100 == 0:
        multiple100 = (sake - rest100)
        numberNotes100 = (multiple100/100)
        print("quantidade de notas de 100 foi: ", numberNotes100)
    if rest50 > 0 or sake % 50 == 0:
        multiple50 = (rest100 - rest50)
        numberNotes50 = (multiple50/50)
        print("quantidade de notas de 50 foi: ", numberNotes50)
    if rest10 > 0 or sake % 10 == 0:
        multiple10 = (rest50 - rest10)
        numberNotes10 = (multiple10/10)
        print("quantidade de notas de 10 foi: ", numberNotes10)
    
    
