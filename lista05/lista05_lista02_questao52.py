# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
# Lukas Michel Souza Mota               1715310018
# Marcus Viniciius Paes da Silva Santos 1515070060
# Matheus de Oliveira Marques           1515310514
# Natália Cavalcante Xavier             1715310021
# Nayara da Silva Cerdeira da Costa     1715310038
#
#52) Implementar um algoritmo em PORTUGOL para calcular o sen(X). O valor de X
#deverá ser digitado em graus. O valor do seno de X será calculado pela soma dos 15
#primeiros termos da série a seguir:
# senx= x-x^3/3!+x^5/5!...
#--------------------------------------------------------
cont1 = 1
cont2 = 3
fat = 1
contfat = 1
x = (float(input("Informe graus de x:")))
sen = x
while cont1 <=15:
    while contfat <= cont2:
        fat = fat * contfat
        contfat+=1
    if cont1 % 2 != 0:
         sen -= (x**cont2)/fat
    else:
         sen += (x**cont2)/fat
    cont1 += 1
    cont2 += 2
print(sen)
