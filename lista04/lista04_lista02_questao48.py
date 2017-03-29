# -*- coding: utf-8 -*-
# --------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Tiago Ferreira Aranha                     1715310047
#
# URI Online Judge | 1048
# Salary Increase
# --------------------------------------------------------------------------------------

salary = float(input())

if 0 < salary <= 400.00:
    increase_percentual = 0.15
elif 400.01 < salary <= 800.00:
    increase_percentual = 0.12
elif 800.01 < salary <= 1200.00:
    increase_percentual = 0.10
elif 1200.01 < salary <= 2000.00:
    increase_percentual = 0.07
else:
    increase_percentual = 0.04

print("Novo salario: %5.2f" % (salary + salary * increase_percentual))
print("Reajuste ganho: %5.2f" % (salary * increase_percentual))
print("Em percentual: %d" % (increase_percentual * 100), "%")