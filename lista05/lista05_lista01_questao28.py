quantidade = 0

while quantidade <= 0:
    quantidade = int(input("Digite a quantidade de CDs: "))
    if quantidade <= 0:
        print("Quantidade deve ser positiva e diferente de 0")

valor = 0
while valor <=0:
    valor = float(input("Digite o preço dos CDs: "))
    if valor <= 0:
        print("Valor deve ser positivo e diferente de 0")
average = valor/quantidade

print("Quantidade de CDs é ", quantidade)
print("Preço médio dos CDs é de R$" '%0.2f' %average)