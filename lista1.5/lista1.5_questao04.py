#---------------------------------------------------------------------
#Introdução a Programação dos Computadores - IPC
#Universidade do Estado do Amazonas - UEA
#Prof. Jucimar Jr.
#Adham Lucas da Silva Oliveira           1715310001
#Enrique Leão Barbosa Izel               1715310048
#Erik Atilio Silva Rey                   1715310059
#Ulisses Antonio Antonino da Costa       1515090555
#Guilherme Silva de Oliveira             1715310034
#Faça um programa que receba duas notas, calcule e mostre a média ponderada dessas duas notas, 
#considerando peso 2 para a primeira nota e peso 3 para a segunda nota
#----------------------------------------------------------------------
note1= float(input('primeira nota'))
note2= float(input('segunda nota'))
average= (note1*2 + note2*3) / 5
print(average)
