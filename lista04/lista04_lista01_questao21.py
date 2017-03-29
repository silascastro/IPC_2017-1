#--------------------------------------------------------------------------
#Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
#Gabriel Barroso da Silva Lima 1715310011
#Felipe Eduardo Silva de Almeida 1715310031
#Frederico Victor Alfaia Rodrigues 
1515200030
#Diogo Duarte
#Felipe Guerreiro de Mello 1315120052
#Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar 
#quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo 
#é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina. 
#-------------------------------------------------------------------------------------

saq = float(input("valor do saque: "))
while saq < 10 or saq > 600:
    saq = float(input("valor inválido, digite um valor entre R$10 e R$600: "))
n100 = int(saq / 100)
saq = saq - (n100 * 100)
n50 = saq / 50
saq = saq - (n50 * 50)
n10 = saq / 10
saq = saq - (n10 * 10)
n5 = saq / 5
saq = saq - (n5 * 5)
print ("serão necessárias: ")
print (n100, "nota(s) de R$100")
print (n50, "nota(s) de R$50")
print (n10, "nota(s) de R$10")
print (n50, "nota(s) de R$5")
print (int(saq), "nota(s) de R$1")