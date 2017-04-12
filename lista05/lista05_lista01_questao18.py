#-----------------------------
# Atraso na entrega
# Felipe Eduardo | Grupo 3
# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
#-----------------------------


mayor = 0
addiction = 0
conjunt_numbers = int(input("Digite quantos numeros farão parte do conjunto: "))
c = 1
while c <= conjunt_numbers:
    number = int(input("Digite %dº número"%c))
    if c == 1:
        minor = number
    if number < minor:
        minor = number
    if number > mayor:
        mayor = number
    addiction = addiction + number
    c = c + 1
print("menor = ", minor)
print("mayor = ", mayor)
print("soma = ", addiction)
