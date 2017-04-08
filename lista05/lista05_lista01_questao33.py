#----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
#
# Adham Lucas da Silva Oliveira           1715310059
# Alexandre Marques Uchôa                 1715310028
# André Luís Laborda Neves                1515070006
# Carlos Eduardo Tapudima de Oliveira	  1715310030
# Aracille de Souza Barbosa               1315120206
# Dayana Picanço Marquez                  1715310058
#
#O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia um conjunto indeterminado
#de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.
#-----------------------------------------------------------------------------------------------------------------------
qte_temp = int(input("Digite a quantidade de temperaturas desejadas: "))

cont = 0
sum_temp = 0
high = 0
low = 100

while cont < qte_temp:

    temp = float(input("Digite o valor da temperatura: "))

    if temp > high:
        high = temp

    if temp < low:
        low = temp

    sum_temp += temp
    cont += 1

med_temp = sum_temp / qte_temp
print ('A maior temperatura foi %.0f e a menor foi %.0f' %(high,low))
print ('A média de temperaturas foi %.1f' %med_temp)




