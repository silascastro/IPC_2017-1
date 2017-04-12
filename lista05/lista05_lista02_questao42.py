prev_number = int(input("Digite um numero: "))
next_number = int(input("Digite outro numero: "))
fibonacci = 0
count = 1

n = int( input('Digite a quantidade de números da sequência fibonacci desejados: '))

while count <= n:
    if count == 1:
        print(prev_number, end = ' ')
    else:
        print(next_number, end = ' ')
        fibonacci = prev_number + next_number
        prev_number = next_number
        next_number = fibonacci
    count += 1