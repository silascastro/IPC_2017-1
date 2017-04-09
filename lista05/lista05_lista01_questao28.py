#---------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
#
# Joelson Pereira Lima 			    1715310060
# Gabriel Nascimento de Oliveira 	1715310052
# Hugo Thadeu Silva Cardoso         1715310013
# Jandinne Duarte de Oliveira 		1015070265
# Gabriel de Queiroz Souza		    1715310044
# Guilherme Silva de Oliveira		1715310034
#
# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada
#um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um. 

quantity = 0

while quantity <= 0:
    quantity = int(input("Digite a quantidade de CDs: "))
    if quantity <= 0:
        print("Quantidade deve ser positiva e diferente de 0")

value = 0
while value <=0:
    value = float(input("Digite o preço dos CDs: "))
    if value <= 0:
        print("Valor deve ser positivo e diferente de 0")
average = value/quantity

print("Quantidade de CDs é ", quantity)
print("Preço médio dos CDs é de R$" '%0.2f' %average)
