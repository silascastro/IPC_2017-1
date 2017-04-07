#Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
n_numbers = float(input("Digite o tamanho de um conjunto (números de 0-10000): "))

while n_numbers < 0 or n_numbers > 10000:
    print("Número invalido, digite novamente")
    n_numbers = float(input("Digite o tamanho de um conjunto (números de 0-10000): "))

counter = 1
sum = 0
lowest = 0
higher = n_numbers
position = 0

while counter <= n_numbers:
    position = counter
    sum = sum + position
    counter = counter + 1

print("o menor numero é: ", lowest)
print("O maior numero é: ", higher)
print("A soma é",sum)

