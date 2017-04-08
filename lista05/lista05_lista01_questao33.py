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




