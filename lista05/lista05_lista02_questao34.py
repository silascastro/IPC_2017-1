# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr.
# GRUPO 9
# Fang Yao                         1115180236
# Antonio Diego Furtado da Silva   1715310004
#
# Escreva um algoritmo que calcule o quociente da divisão de A por B
#   (número inteiros e positivos), ou seja, A div B, através de subtrações sucessivas.
# Esses dois valores são passados pelo usuário através do teclado.
#
#----------------------------------------------------------------

dividendo = int(input("Informe o Dividendo (A): "))
divisor = int(input("Informe o Divisor (B): "))

resto = dividendo
quociente = 0

while resto >= divisor:
  resto -= divisor
  quociente += 1

print("Valor do Quociente de A/B é %d" %quociente)
#print("Valor do resto de A/B é %d" %resto)
