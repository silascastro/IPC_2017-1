
#Introdução a Programação de Computadores - IPC
#Universidade do Estado do Amazonas - UEA
#
#Ulisses Antonio Da Costa            1515090555
#Thiago ferreira Aranha 		     1715310047
#vitor simões Azevedo			     1715310025
#victor hugo de oliveira carreira	 1715310063
#Reinaldo vargas 			         1715310054

#---------------------------------------------------------------------------------------------------
#Escreva um algoritmo em PORTUGOL que receba oito números do usuário e imprima
#o logaritmo de cada um deles na base 10.


import math

print("=1================")
entrada_log1 = int(input("dgite seu primeiro numero:"))
while entrada_log1 > 0 :
      entrada_log1 = math.log10(entrada_log1)
      entrada_log1 = int(input("dgite seu primeiro numero:"))
      print(entrada_log1)
if entrada_log1 == 0:
      entrada_log1 = int(input("dgite seu primeiro numero:"))
      entrada_log1 = math.log10(entrada_log1)
      print(entrada_log1)

print("=2================")
entrada_log2 = int(input("dgite seu segundo numero:"))
while entrada_log2 > 0 :
       entrada_log2 = math.log10(entrada_log2)
       print(entrada_log2)
if entrada_log2 == 0:
       entrada_log2 = int(input("dgite seu segundo numero:"))
       entrada_log2 = math.log10(entrada_log2)
       print(entrada_log2)

print("==3===============")
entrada_log3 = int(input("dgite seu terceiro numero:"))
while entrada_log3 > 0:
        entrada_log3 = math.log10(entrada_log3)
        print(entrada_log3)
if entrada_log3 ==0:
        entrada_log3 = int(input("dgite seu terceiro numero:"))
        entrada_log3 = math.log10(entrada_log3)
        print(entrada_log3)

print("===4==============")
entrada_log4 = int(input("dgite seu quarto numero:"))
while entrada_log4 > 0 :
      entrada_log4 = math.log10(entrada_log4)
      print(entrada_log4)
if entrada_log4 == 0:
      entrada_log4 = int(input("dgite seu quarto numero:"))
      entrada_log4 = math.log10(entrada_log4)
      print(entrada_log4)

print("====5=============")
entrada_log5 = int(input("dgite seu quinto numero:"))
while entrada_log5 > 0 :
      entrada_log5 = math.log10(entrada_log5)
      print(entrada_log5)
if entrada_log5 ==0:
      entrada_log5 = int(input("dgite seu quinto numero:"))
      entrada_log5 = math.log10(entrada_log5)
      print(entrada_log5)

print("=====6============")
entrada_log6 = int(input("dgite seu sexto numero:"))
while entrada_log6 > 0:
      entrada_log6 = math.log10(entrada_log6)
      print(entrada_log6)
if entrada_log6 == 0:
      entrada_log6 = int(input("dgite seu sexto numero:"))
      entrada_log6 = math.log10(entrada_log6)
      print(entrada_log6)

print("======7===========")
entrada_log7 = int(input("dgite seu sétimo numero:"))
while entrada_log7 > 0 :
      entrada_log7 = math.log10(entrada_log7)
      print(entrada_log7)
if entrada_log7 == 0:
      entrada_log7 = int(input("dgite seu sétimo numero:"))
      entrada_log7 = math.log10(entrada_log7)
      print(entrada_log7)

print("=======8==========")
entrada_log8 = int(input("dgite seu oitavo numero:"))
while entrada_log8 > 0:
      entrada_log8 = math.log10(entrada_log8)
      print(entrada_log8)
if entrada_log8 == 0:
      entrada_log8 = int(input("dgite seu oitavo numero:"))
      entrada_log8 = math.log10(entrada_log8)
      print(entrada_log8)
print("CALCULO DE LOGARÍTMOS BASE 10 FINALIZADO")