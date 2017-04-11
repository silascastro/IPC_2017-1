# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Grupo 08
# Victor Summer Oliveira Pantaleao 1715310042
# Walter Nobre Da Silva Conceição  1715310057
# Wesley da Silva Rocha            1715310026
# Wilbert Luís Evangelista Marins  1715310055
# Yuri Leandro de Aquino Silva     1615100462
#
# Dado um país A, com 5000000 de habitantes e uma taxa de natalidade de 3% ao ano, e
# um país B com 7000000 de habitantes e uma taxa de natalidade de 2% ao ano,
# escrever um algoritmo em PORTUGOL que seja capaz de calcular e iterativamente e
# no fim imprimir o tempo necessário para que a população do país A ultrapasse a
# população do país B.
# ----------------------------------------------------------

a = 5000000 # total de habitantes no país A
b = 7000000 # Total de habitantes no país B
c = 0 # contador

while a < b: # usamos while para dar, neste caso, um "período de tempo limitado", onde o loop(ou o "programa") acabará quando a meta dita for atingida
    a = a + (a * 3 / 100) # total de habitantes em A somado ao total de habitantes em A abrangendo a taxa de natalidade deste país
    b = b + (b * 2 / 100) # total de habitantes em B somado ao total de habitantes em B abrangendo a taxa de natalidade deste país
    c = c + 1 # contador somado a mais um referente aos anos necessarios para o país A ultrapassar o país B em relação ao número de habitantes
print('The total of years that the country *A* will have to pass the population of the country *B* will be',c,'years')


