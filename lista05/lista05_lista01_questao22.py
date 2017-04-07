# ----------------------------------------------------------
# Introducao a Programacao de Computadores - IPC
#
# Universidade do Estado do Amazonas - UEA
#
# Prof. Jucimar Jr
#
# Lukas Michel Souza Mota               1715310018
# Marcus Vinicius Paes da Silva Santos  1515070060
# Matheus de Oliveira Marques           1515310514
# Natalia Cavalcante Xavier             1715310021
# Nayara da Silva Cerdeira da Costa     1715310038
#
# Altere o programa de calculo dos numeros primos, 
# informando, caso o numero nao seja primo, por quais numero ele eh divisivel.
#----------------------------------------------------------

number = int(input("Informe um numero: "))
divisibles = []

aux = number - 1
cont = 0

while aux > 1 :
    if (number % aux) == 0 :
        cont += 1
        divisibles.append(aux)
    aux -= 1    

if cont == 0 :
    print("O valor eh primo !")
else :
    print("O valor nao eh primo !")
    print("Divisores de %d: " % number)
    print(divisibles)
