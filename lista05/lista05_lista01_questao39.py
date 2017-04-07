# encoding: utf-8
#--------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# ULISSES ANTONIO ANTONINO DA COSTA - 1515090555
# TIAGO FERREIRA ARANHA - 1715310047
# VÍTOR SIMÕES AZEVEDO - 1715310025
# VICTOR HUGO DE OLIVEIRA CARREIRA - 1715310063
# REINALDO VARGAS - 1715310054
#
# 39. Faça um programa que leia dez conjuntos de dois valores,
# o primeiro representando o número do aluno e o segundo
# representando a sua altura em centímetros.
# Encontre o aluno mais alto e o mais baixo.
# Mostre o número do aluno mais alto e o número do
# aluno mais baixo, junto com suas alturas.
#--------------------------------------------------------------------------

c = 1

higher_student = ""
higher_student_height = 0

lower_student = ""
lower_student_height = 0

while c <= 2:
    student_name = input("Informe o nome do aluno: ")
    student_height = int(input("Informe a altura do aluno: "))

    if c == 1:
        higher_student_height = student_height
        lower_student_height = student_height
        higher_student = student_name
        lower_student = student_name
    else:
        if student_height > higher_student_height:
            higher_student_height = student_height
            higher_student = student_name
        elif student_height < lower_student_height:
            lower_student_height = student_height
            lower_student = student_name
    c = c + 1

print("O aluno mais alto é %s e mede %5.2f" % (higher_student, higher_student_height))
print("O aluno mais baixo é %s e mede %5.2f" % (lower_student, lower_student_height))
