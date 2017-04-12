#---------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#Natália Cavalcante Xavier     1715310021
#Nayara da Silva Cerdeira da Costa 1715310038
#Marcus Viniciius Paes da Silva Santos 1515070060
#Matheus de Oliveira Marques 1515310514
#Lukas Michel Souza Mota 1715310018

#Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
# No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados.
# O seu resultado fica sendo a média dos três valores restantes
# Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos
# e depois informe a média dos saltos conforme a descrição acima informada(retirar o melhor e o pior salto e depois calcular a média).
# Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são ordenados.
#  O programa deve ser encerrado quando não for informado o nome do atleta.
salto1 = float(input("Digite o valor do primeiro salto "))
salto2 = float(input("Digite o valor do segundo salto "))
salto3 = float(input("Digite o valor do terceiro salto "))
salto4 = float(input("Digite o valor do quarto salto "))
salto5 = float(input("Digite o valor do quinto salto "))
nome=input("Infome o nome do atleta")
while nome != "":
    if salto1 < salto2 and salto1 < salto3 and salto1 < salto4 and salto1 < salto5:
     print("menor salto",salto1)
     salto1=0
    elif salto2 < salto1 and salto2 < salto3 and salto2 < salto4 and salto2 < salto5:
     print("menor salto",salto2)
     salto2=0
    elif salto3 < salto1 and salto3 < salto2 and  salto3 < salto4 and salto3 < salto5:
     print("menor salto",salto3)
     salto3=0
    elif salto4 < salto1 and salto4 < salto2 and salto4 < salto3 and salto4 < salto5:
     print("menor salto",salto4)
     salto4=0
    elif salto5 < salto1 and salto5 < salto2 and salto5 < salto3 and salto5 < salto4:
     print("menor salto",salto5)
     salto5=0

    if salto1 > salto2 and salto1 > salto3 and salto1 > salto4 and salto1 > salto5:
     print("maior salto",salto1)
     salto1=0
    elif salto2 > salto1 and salto2 > salto3 and salto2 > salto4 and salto2 > salto5:
        print("maior salto",salto2)
        salto2=0
    elif salto3 > salto1 and salto3 > salto2 and  salto3 > salto4 and salto3 > salto5:
        print("maior salto",salto3)
        salto3=0
    elif salto4 > salto1 and salto4 > salto2 and salto4 > salto3 and salto4 > salto5:
        print("maior salto",salto4)
        salto4=0
    elif salto5 > salto1 and salto5 > salto2 and salto5 > salto3 and salto5 > salto4:
        print("maior salto",salto5)
    salto5=0

    media=salto1+salto2+salto3+salto4+salto5/2

    print("Média dos saltos",media)