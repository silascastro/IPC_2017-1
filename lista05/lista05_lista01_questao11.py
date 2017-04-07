#Altere o programa anterior para mostrar no final a soma dos números.

number = int(input("Digite um número inteiro: "))
number_2 = int(input("Digite um número inteiro: "))
acumulator = 0

if number > number_2:
    higher = number
    lower = number_2

else:
    higher = number_2
    lower = number


while lower < (higher - 1):
    lower = lower + 1
    acumulator = acumulator + lower
    print(lower)

print(acumulator)

