#----------------------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Adham Lucas da Silva Oliveira           1715310059
# Alexandre Marques Uchôa                 1715310028
# André Luís Laborda Neves                1515070006
# Carlos Eduardo Tapudima de Oliveira	    1715310030
# Aracille de Souza Barbosa               1315120206
# Dayana Picanço Marquez                  1715310058
#Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma 
#varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada. 
#----------------------------------------------------------------------------------------------------------------------------------
n_person = int(input("Digite o número de pessoas da turma: "))

cont = 0
sum_age = 0

while cont < n_person :
    age = int(input("Digite a idade: "))
    sum_age = sum_age + age
    cont += 1

average_age = sum_age / n_person

if 0 < average_age <= 25 :
    print ('A Turma é jovem')

if 26 <= average_age <= 60 :
    print ('A Turma é adulta')

if average_age > 60 :
    print ('A turma é velha')
