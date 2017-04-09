# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Grupo 08
# Victor Summer Oliveira Pantaleao 1715310042
# Walter Nobre Da Silva Conceição  1715310057
# Wesley da Silva Rocha            1715310026
# Wilbert Luís Evangelista Martins 1715310055
# Yuri Leandro de Aquino Silva     1615100462
#
#Faça um programa que leia 5 números e informe a soma e a mé-
#dia dos números.
#-----------------------------------------------------------

c = 0
sum = 0

while c < 5 :
    num = int(input("Digite um número:"))
    c = c + 1
    sum = sum + num

med = sum / 5
print(sum,med)
