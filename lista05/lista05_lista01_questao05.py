#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
#Valide a entrada e permita repetir a operação.

a = float(input("digite a população do primeiro país: "))
b = float(input("digite a população do segundo país: "))
tax_a = float(input("digite a taxa de crescimento do primeiro país: "))
tax_b = float(input("digite a taxa de crescimento do segundo país: "))
years = 0

while a < b or a == b:
    a = a + (a * tax_a)
    b = b + (b * tax_b)
    print(a)
    years = years + 1
print("será necessário %i anos para o país a ultrapasar o país b" %years)
