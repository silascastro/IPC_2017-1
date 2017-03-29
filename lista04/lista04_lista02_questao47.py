
#--------------------------------------------------------------------------
#Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#=======================================================================================
#Reinaldo da Silva Vargas 1715310054
#Natalia Cavalcante Xavier 1715310021
#Nayara da Silva Cerdeira da Costa 1715310038
#Marcus Vinicius Paes da Silva Santos 1515070060
#Matheus de Oliveira Marques 1515310514
#
#faça um programa que peça as horas iniciais,minutos iniciais,horas finais e minutos finis de um jogo. em seguida imprima na tela
# a soma da partida do jogo
hora_inicial = float(input('informe a hora inicial'))
minuto_inicial = int(input('informe o minuto inicial'))
hora_final= int(input('informe a hora final'))
minuto_final= int(input('informe o minuto final'))

calculando_time = (hora_inicial + hora_final)
minutoscalc = (minuto_inicial + minuto_final)

print('O jogo durou:', calculando_time, 'horas', 'e', minutoscalc, 'minutos')
