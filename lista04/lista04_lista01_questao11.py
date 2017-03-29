#--------------------------------------------------------------------------
#Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
# Diogo Duarte
# Felipe Eduardo Silva de Almeida   1715310031
# Felipe Guerreiro de Mello         1315120052
# Frederico Victor Alfaia Rodrigues 1515200030
# Gabriel Barroso da Silva Lima     1715310011
#
#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#    Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#    salários até R$ 280,00 (incluindo) : aumento de 20%
#    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#    salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#    o salário antes do reajuste;
#    o percentual de aumento aplicado;
#    o valor do aumento;
#    o novo salário, após o aumento.
#-------------------------------------------------------------------------------------

sal1 = float(input("digite um salário"))

if sal1 <= 280:

    sal2 = sal1*1.2
    
    per = 20

else:
    
    if sal1 <= 780:
        
        sal2 = sal1*1.15
        
        per = 15
    
    else:
        
        if sal1 <= 1500:
            
            sal2 = sal1*1.1
            
            per = 10
        
        else:
     
            sal2 = sal1*1.05
            
            per = 5

dif = sal2 - sal1

print("salário anterior: R$", sal1, "reais || salário atual: R$", sal2, "reais")

print("percentual de aumento aplicado: ", per,"% || valor do aumento: R$", dif, "reais")
