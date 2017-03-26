#-----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr.
# Erik Atlio Silva Rey                  1715310059
# Edson de Lima Barros                  1715310043
# Enrique Leão Barbosa Izel             1715310048
# Evandro Padilha Barroso Filho         1715310009
# Fang Yao                              1115180236
#
#Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em
# branco e em seguida, os valores na sequência como foram lidos.
#Entrada
#A entrada contem três números inteiros.
#Saída
#Imprima a saída conforme foi especificado.
#-----------------------------------------------------------------------------------------------------------------------

a, b, c = input().split()
A = int(a)
B = int(b)
C = int(c)

if (A > B and A > C) and (B > C):
    print(C)
    print(B)
    print(A)
if (A > B and A > C) and (C > B):
    print(B)
    print(C)
    print(A)
if (B > C and B > A) and (A > C):
    print(C)
    print(A)
    print(B)
if (B > C and B > A) and (C > A):
    print(A)
    print(C)
    print(B)
if (C > B and C > A) and (A > B):
    print(B)
    print(A)
    print(C)
if (C > B and C > A) and (B > A):
    print(A)
    print(B)
    print(C)
print()
print(A)
print(B)
print(C)