# --------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# ULISSES ANTONIO ANTONINO DA COSTA  1515090555
# TIAGO FERREIRA ARANHA              1715310047
# VÍTOR SIMÕES AZEVEDO               1715310025
# VICTOR HUGO DE OLIVEIRA CARREIRA   1715310063
# REINALDO VARGAS                    1715310054
#
#23)Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário
#O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos
#Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados
#---------------------------------------------------------------------------


primo = int(input("digite um numero inteiro"))
limite = primo
numero = 1
c = 1
p = 0


while numero <= limite:
    i = numero -1
    while i > 1:
        if numero % i == 0: break
        i -= 1
        c += 1
    else:
        print(numero,)
        p += 1
    numero += 1

print("\n\nForam encontrados %d números primos." %p)
print("Foram feitas %d divisões." %c)
