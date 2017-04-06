# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Evandro Padilha Barroso Filho 1715310009 
# nome completo do aluno 2	matrícula do aluno 2
# nome completo do aluno 3	matrícula do aluno 3
# nome completo do aluno 4	matrícula do aluno 4
#
# #03.Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';
# ----------------------------------------------------------

name = (input("Digite seu nome (min: 3 caracteres): "))
age = int(input("Digite sua idade: "))
sallary = float(input("Digite seu salário: "))
sex = input("Digite seu sexo usando f para feminino e m para masculino: ")
civil_state = input("Digite seu estado civil(s, c, v, d): ")

def validation(name, age, sallary, sex, civil_state,):
    if len(name) < 3 or age < 0 or age > 150 or sallary <= 0 or sex not in ['f', 'm'] or civil_state not in ['s', 'c',
                                                                                                            'v','d']:
        return False
    else:
        validation == True

while validation(name, age,sallary, sex, civil_state) == False:
    print("Algum campo está invalido, por favor digite novamente os campos")
    name = input("Digite seu nome (min: 3 caracteres): ")
    age = int(input("Digite sua idade: "))
    sallary = float(input("Digite seu salário: "))
    sex = input("Digite seu sexo usando f para feminino e m para masculino: ")
    civil_state = input("Digite seu estado civil(s, c, v, d): ")

print("Informações atualizadas")
