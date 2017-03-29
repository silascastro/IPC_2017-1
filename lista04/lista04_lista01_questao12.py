#-----------------------------------------------------------------------------------------------------------------------
## Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Guilherme Silva de Oliveira       1715310034
# Gabriel Nascimento de Oliveira    1715310052
# Gabriel de Queiroz Souza          1715310044
# Hugo Thadeu Silva Cardoso         1715310013
# Ian Gabriel Costa Machado         1215120276
#
#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda
#que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto
#mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
#O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo
#No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#-----------------------------------------------------------------------------------------------------------------------

x=float(input('horas trabalhadas'))
y=float(input('ganhos por hora'))
SalarioBruto=x*y
print('Salario Bruto',SalarioBruto)
Sindicato= SalarioBruto*0.03
print('Sindicato', Sindicato)
FGTS=SalarioBruto*0.11
print('FGTS', FGTS)
IR5=5%SalarioBruto
IR10=10%SalarioBruto
IR20=20%SalarioBruto
if SalarioBruto<=900:
    print('Salario Liquido', SalarioBruto-Sindicato, 'IR Isento')
else:
    if 900<SalarioBruto<1500:
        print('Salario Liquido', SalarioBruto-Sindicato-IR5, 'IR 5%')
    else:
        if 1500<SalarioBruto<2500:
            print('Salario Liquido', SalarioBruto-Sindicato-IR10, 'IR 10%')
        else:
            print('Salario Liquido', SalarioBruto-Sindicato-IR20, 'IR 20%')