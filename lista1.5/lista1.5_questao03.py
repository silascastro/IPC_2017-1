#---------------------------------------------------------------------
#Introdução a Programação dos Computadores - IPC
#Universidade do Estado do Amazonas - UEA
#Prof. Jucimar Jr.
#Adham Lucas da Silva Oliveira           1715310001
#Enrique Leão Barbosa Izel               1715310048
#Erik Atilio Silva Rey                   1715310059
#Ulisses Antonio Antonino da Costa       1515090555
#Guilherme Silva de Oliveira             1715310034
#Faça um programa que receba dois números, calcule e mostre a divisão 
#do primeiro número pelo segundo. Sabe-se que o segundo número não pode
#ser zero, portanto não é necessário se preocupar com validações
#----------------------------------------------------------------------
n1 = float(input("numerador: "))                       #receber o primeiro número (n=number)
n2 = float(input("denominador (Não pode ser 0!!): "))  #receber o segundo número
division = (n1/n2)                                     #dividir o primeiro pelo segundo
print(division)                                        #resultado da divisão
