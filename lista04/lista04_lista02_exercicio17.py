#--------------------------------------------------------------------------
#Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr

#Reinaldo da Silva Varas 1715310054
#Natalia Cavalcante Xavier 1715310021
#Nayara da Silva Cerdeira da Costa 1715310038
#Marcus Vinicius Paes da Silva Santos 1515070060
#Matheus de Oliveira Marques 1515310514
#Criar um programa que indique quantos litros sao necessários para realizar uma viagem
#-------------------------------------------------------------------------------------

timetrip=float(input("Informe o tempo de viagem: "))
speed=float(input("Informe a velocidade: "))
distance=speed*timetrip
liters= distance/12
print("São necessarios %.3f " %liters,"litros")