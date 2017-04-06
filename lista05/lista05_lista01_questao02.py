# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# nome completo do aluno 1	matrícula do aluno 1
# nome completo do aluno 2	matrícula do aluno 2
# nome completo do aluno 3	matrícula do aluno 3
# nome completo do aluno 4	matrícula do aluno 4
# nome completo do aluno 5	matrícula do aluno 5
#
#02.Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma
#mensagem de erro e voltando a pedir as informações.
# ----------------------------------------------------------

name = input("Digite o seu nome de acesso: ")
password = input("Digite sua senha: ")

while name == password:
    print("Sua senha não pode ser igual ao seu login, digite suas informações novamente")
    name = input("Digite o seu nome de acesso: ")
    password = input("Digite sua senha: ")
