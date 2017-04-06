#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma
#mensagem de erro e voltando a pedir as informações.

name = input("Digite o seu nome de acesso: ")
password = input("Digite sua senha: ")

while name == password:
    print("Sua senha não pode ser igual ao seu login, digite suas informações novamente")
    name = input("Digite o seu nome de acesso: ")
    password = input("Digite sua senha: ")
