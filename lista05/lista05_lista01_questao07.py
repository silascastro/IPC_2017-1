# --------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# ULISSES ANTONIO ANTONINO DA COSTA - 1515090555
# TIAGO FERREIRA ARANHA - 1715310047
# VÍTOR SIMÕES AZEVEDO - 1715310025
# VICTOR HUGO DE OLIVEIRA CARREIRA - 1715310063
# REINALDO VARGAS - 1715310054
#
#7)Faça um programa que leia 5 números e informe o maior número.
#
number1 = int(input("digite um número: "))
number2 = int(input("digite mais um número: "))
number3 = int(input("digite mais um número: "))
number4 = int(input("digite mais um número: "))
number5 = int(input("digite mais um número: "))

while number1 > number2 and number1 > number3 and number1 > number4 and number1 > number5:
    print("o maior número é o: ", number1)
    break
    
while number2 > number1 and number2 > number3 and number2 > number4 and number2 > number5:
    print("o maior número é o: ", number2)
    break
    
while number3 > number1 and number3 > number2 and number3 > number4 and number3 > number5:
    print("o maior número é o: ", number3)
    break
    
while number4 > number1 and number4 > number2 and number4 > number3 and number4 > number5:
    print("o maior número é o: ", number4)
    break
    
while number5 > number1 and number5 > number2 and number5 > number3 and number5 > number4:
    print("o maior número é o: ", number5)
    break
    
else:
    print("operação invalida! números iguais")
