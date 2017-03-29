# -*- coding: utf-8 -*-
# --------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Tiago Ferreira Aranha                     1715310047
#
# URI Online Judge | 1038
# Snack
# --------------------------------------------------------------------------------------

x = int(input())
y = float(input())

if x == 1:
    price = 4.00
elif x == 2:
    price = 4.50
elif x == 3:
    price = 5.00
elif x == 4:
    price = 2.00
else:
    price = 1.50

print("Total: R$ %2.2f" % float(price * y))
