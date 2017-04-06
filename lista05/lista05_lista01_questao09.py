#---------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
#
# Adham Lucas da Silva Oliveira           1715310059
# Alexandre Marques Uchôa                 1715310028
# André Luís Laborda Neves                1515070006
# Carlos Eduardo Tapudima de Oliveira	    1715310030
# Aracille de Souza Barbosa               1315120206
# Dayana Picanço Marquez                  1715310058
#
#Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
#----------------------------------------------------------------------------

contador = 1

while 0 < contador < 50:
    progressão_aritmetica = 1 + (contador - 1)*1
    contador = contador + 1
    if progressão_aritmetica % 2 != 0:
        print(progressão_aritmetica)
