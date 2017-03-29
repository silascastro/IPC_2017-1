# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
# Felipe Eduardo Silva de Almeida	  1715310031
# Felipe Guerreiro Federico Vitor
# Federico Vitor
# Gabriel Alves
# Gabriel Barroso
#
# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram
# para desenvolver o programa que calculará os reajustes.
#   Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
#   baseado no salário atual:
#       salários até R$ 280,00 (incluindo) : aumento de 20%
#       salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#       salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#       salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#       o salário antes do reajuste;
#       o percentual de aumento aplicado;
#       o valor do aumento;
#       o novo salário, após o aumento.
#  ----------------------------------------------------------
salaryBefor = float(input("Digite seu salário atual: "))

if salaryBefor <= 280:
    print("Seu salário atual é: ", salaryBefor)
    print("Seu salário receberá um reajuste de 20%")
    salaryIncrase = (salaryBefor * 0.2)
    print("O aumento será de: ", salaryIncrase)
    salaryAfter = (salaryBefor + salaryIncrase)
    print("Com o reajuste seu salário será: ", salaryAfter)
else:
    if 280 < salaryBefor <= 700:
        print("Seu salário atual é: ", salaryBefor)
        print("Seu salário receberá um reajuste de 15%")
        salaryIncrase = (salaryBefor * 0.15)
        print("O aumento será de: ", salaryIncrase)
        salaryAfter = (salaryBefor + salaryIncrase)
        print("Com o reajuste seu salário será: ", salaryAfter)
    else:
        if 700 < salaryBefor < 1500:
            print("Seu salário atual é: ", salaryBefor)
            print("Seu salário receberá um reajuste de 10%")
            salaryIncrase = (salaryBefor * 0.1)
            print("O aumento será de: ", salaryIncrase)
            salaryAfter = (salaryBefor + salaryIncrase)
            print("Com o reajuste seu salário será: ", salaryAfter)
        else:
            if salaryBefor >= 1500:
                print("Seu salário atual é: ", salaryBefor)
                print("Seu salário receberá um reajuste de 5%")
                salaryIncrase = (salaryBefor * 0.05)
                print("O aumento será de: ", salaryIncrase)
                salaryAfter = (salaryBefor + salaryIncrase)
                print("Com o reajuste seu salário será: ", salaryAfter)
