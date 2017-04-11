# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Grupo 08
# Victor Summer Oliveira Pantaleao 1715310042
# Walter Nobre Da Silva Conceição  1715310057
# Wesley da Silva Rocha            1715310026
# Wilbert Luís Evangelista Marins  1715310055
# Yuri Leandro de Aquino Silva     1615100462
#
#Faça um programa que leia 5 números e informe a soma e a mé-
#dia dos números.
#-----------------------------------------------------------
count = 1
amount = 0

while count <= 5:
    num = float(input("Digite um número: "))
    count += 1
    amount += num

med = amount / 5

print('Soma total dos números: %.2f ' % amount)
print('Média dos números: %.2f' % med)
