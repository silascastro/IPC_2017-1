#---------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
#
# Adham Lucas da Silva Oliveira           1715310059
# Alexandre Marques Uchôa                 1715310028
# André Luís Laborda Neves                1515070006
# Carlos Eduardo Tapudima de Oliveira	  1715310030
# Aracille de Souza Barbosa               1315120206
# Dayana Picanço Marquez                  1715310058
#
#Faça um programa que peça uma nota, entre zero e dez.
#Mostre uma mensagem caso o valor seja inválido
#  e continue pedindo até que o usuário informe um valor válido.
#-----------------------------------------------------------------
note = float(input('Digite uma nota entre 0 e 10'))

while note > 10 or note < 0

    print('Valor inválido')
    note = float(input('Digite uma nota entre 0 e 10'))
