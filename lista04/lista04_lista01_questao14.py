#--------------------------------------------------------------------------
#Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr

#Reinaldo da Silva Varas 1715310054
#Natalia Cavalcante Xavier 1715310021
#Nayara da Silva Cerdeira da Costa 1715310038
#Marcus Vinicius Paes da Silva Santos 1515070060
#Matheus de Oliveira Marques 1515310514
#-------------------------------------------

n1= float(input("Digite sua primeira nota "))
n2=float(input("Digite sua segunda nota  "))
m=(n1+n2)/2

if m >9 and m < 10:
    print("Aprovado,conceito A")
if m > 7.5 and m < 9:
    print("Aprovado,conceito B")
if m > 6 and m < 7.5:
    print("Aprovado,conceito C")
if m > 4 and m < 6:
    print("Reprovado,conceito D")
if m > 0 and m < 4:
    print("Reprovado,conceito E")

print("Sua primeira nota foi ",n1)
print("Sua segunda nota foi ",n2)
print("Sua media foi ",m)
