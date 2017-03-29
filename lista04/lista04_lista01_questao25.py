#--------------------------------------------------------------------------
#Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#=======================================================================================
#Reinaldo da Silva Vargas 1715310054
#Natalia Cavalcante Xavier 1715310021
#Nayara da Silva Cerdeira da Costa 1715310038
#Marcus Vinicius Paes da Silva Santos 1515070060
#Matheus de Oliveira Marques 1515310514
#========================================================================================
#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a #participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser #classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, #ele será classificado como "Inocente".

print("DIGITE 1 PARA(SIM) OU DIGITE (0) PARA NAO")

resposta1 = int(input("TELEFONOU PARA A VITIMA?"))
resposta2 = int(input("ESTEVE NO LOCAL DO CRIME?"))
respota3 = int(input("MORA PERTO DA VITINMA?"))
resposta4 = int(input("DEVIA PARA A VITIMA?"))
resposta5 = int(input("JA TRABALHOU PARA A VITIMA?"))

soma = (resposta1+resposta2+resposta3+resposta4+resposta5)

if soma == 2 :
    print("suspeito")
elif soma > 2 and soma <= 4:
    print("cumplice")
elif soma >= 5:
    print("culpado")
else:
    print("ta de boa")
