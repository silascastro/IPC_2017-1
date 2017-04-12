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
athlete = input("Atleta: ")
jump1 = float(input("Primeiro Salto: "))
jump2 = float(input("Segundo Salto: "))
jump3 = float(input("Terceiro Salto: "))
jump4 = float(input("Quarto Salto: "))
jump5 = float(input("Quinto salto: "))


if jump1 > jump2 and jump1 > jump3 and jump1 > jump4 and jump1 > jump5:
    print("Maior = ", jump1)
    higher = jump1
elif jump2 > jump1 and jump2 > jump3 and jump2 > jump4 and jump2 > jump5:
    print("Maior = ", jump2)
    higher = jump2
elif jump3 > jump1 and jump3 > jump2 and jump3 > jump4 and jump3 > jump5:
    print("Maior = ", jump3)
    higher = jump3
elif jump4 > jump1 and jump4 > jump2 and jump4 > jump3 and jump4 > jump5:
    print("Maior = ", jump4)
    higher = jump4
elif jump5 > jump1 and jump5 > jump2 and jump5 > jump3 and jump5 > jump4:
    print("Maior = ", jump5)
    higher = jump5

if jump1 < jump2 and jump1 < jump3 and jump1 < jump4 and jump1 < jump5:
    print("Menor = ", jump1)
    lower = jump1
elif jump2 < jump1 and jump2 < jump3 and jump2 < jump4 and jump2 < jump5:
    print("Menor = ", jump2)
    lower = jump2
elif jump3 < jump1 and jump3 < jump2 and jump3 < jump4 and jump3 < jump5:
    print("Menor = ", jump3)
    lower = jump3
elif jump4 < jump1 and jump4 < jump2 and jump4 < jump3 and jump4 < jump5:
    print("Menor = ", jump4)
    lower = jump4
elif jump5 < jump1 and jump5 < jump2 and jump5 < jump3 and jump5 < jump4:
    print("Menor = ", jump5)
    lower = jump5

media = (jump1+jump2+jump3+jump4+jump5-higher-lower)/3
print("A média dos demais saltos do atleta é ", media)
