#--------------------------------------------------------------------------
#Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
# Diogo Roberto Duarte da Costa     1715310056
# Felipe Eduardo Silva de Almeida   1715310031
# Felipe Guerreiro de Mello         1315120052
# Frederico Victor Alfaia Rodrigues 1515200030
# Gabriel Barroso da Silva Lima     1715310011
#
# Criar um programa que receba três medidas e indique o perímetro do triângulo.
# Se não for possível, calcular o trapézio tendo a e b como bases e c como altura
#-------------------------------------------------------------------------------------

a = float(input())
b = float(input())
c = float(input())
sep = (a+b+c)/2
if sep < a or sep < b or sep < c:
    sep = (a+b)*c
    print("Area = " a+b+c)
else:
    sep*=2
    print("Perimetro =" (a+b)*c)
