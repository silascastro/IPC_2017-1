# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr.
# 
# Vitor Summer Oliveira Pantaleão  1715310042
# Walter Nobre Da Silva Conceição  1715310057
# Wesley da Silva Rocha            1715310026
# Wilbert Luis Evangelista Marins  1715310055
# Yuri Leandro de Aquino Silva     1615100462
#
# Faça um programa que calcule o mostre a média aritmética de N notas.
#-----------------------------------------------------------

quantidade = int(input("Quantidade de médias "))
contador = 0
variavel = 0

while contador < quantidade:
    medias = float(input("Média %d: " % (contador+1)))
    variavel = variavel + medias
    contador += 1;
variavel = variavel / quantidade

print("A média aritmética é %.2f" % variavel)
