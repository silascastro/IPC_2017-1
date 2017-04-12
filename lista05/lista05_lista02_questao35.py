number_a = float(input("Digite um numero: "))
number_b = float(input("Digite outro numero: "))
c = 1
summation = 0
while c <= number_a and c <= number_b:
    if (number_a % c == 0) and (number_b % c == 0):
        summation = summation + 1
    c += 1
if summation <= 1:
    print("São primos entre si")
else:
    print("Não são primos entre si")