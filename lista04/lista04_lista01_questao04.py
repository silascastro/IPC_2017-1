# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Tiago Ferreira Aranha                     1715310047
# Ulisses Antonio Antonino da Costa         1515090555
# Rodrigo Duarte de Souza                   1115140049
# Victor Hugo de Oliveira Carreira          1715310063
#
# 04.Faça um Programa que verifique se uma letra digitada é 
# vogal ou consoante.
# ----------------------------------------------------------
word = str(input("digite uma letra qualquer: "))
if (word == 'a') or (word == 'e') or (word == 'i') or (word == 'o') or (word == 'u'):
    print("VOGAL! ->", word)
else:
    print("CONSOANTE! ->", word)
