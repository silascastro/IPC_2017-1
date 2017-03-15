# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
# Carlos Eduardo Tapudima de Oliveira       1715310030
# Frederico Victor Alfaia Rodrigues         1515200030
# Joelson Pereira Lima	                    1715310060
# Lucas Gabriel Silveira Duarte             1715310053
# Reinaldo da Silva Vargas	                1715310054
# Walter Nobre da Silva Conceição           1715310057
#
# 14 - Faça um programa que receba o ano de nascimento de uma
# pessoa e o ano atual, calcule e mostre:
# a) a idade dessa pessoa em anos;
# b) a idade dessa pessoa em meses;
# c) a idade dessa pessoa em dias;
# d) a idade dessa pessoa em semanas;
# ----------------------------------------------------------

print ('---------------------Subtração de 2 números---------------------')
try:
    a = input ('Digite o ano atual: ')
    a = int(a)
    b = input ('Digite o ano de nascimento: ')
    b = int(b)
    c = a - b
    d = c * 12
    e = c * 365
    f = c * 48
    print ('A soma: ',a,'  - ',b,' é igual a : ',c,' que é a idade da pessoa em anos')
    print(' A multiplicação ',c,' * ',12,' é igual a : ',d,' que é a idade da pessoa em meses')
    print(' A multiplicação ',c,' * ',365,' é igual a : ',e,' que é a idade da pessoa em dias')
    print('A multiplicação ',c,' * ',48,' é igual a: ',f,' que é a idade da pessoa em semanas')
except ValueError:
    print('Somente números são aceitos, tente novamente!')

