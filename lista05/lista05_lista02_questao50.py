num = float(input("Informe valor: "))
cont = 19
val = 1
fat = 1
aux = 1
soma = num
print("S = ", num, end="")
while cont > 0:
    while fat <= val:
        fat = fat * val
        val = val + 1
    if aux % 2 == 0:
        print(" + %.1f/%d!" % (num, aux), end="")
        soma = soma + (num / fat)
    else:
        print(" - %.1f/%d!" % (num, aux), end="")
        soma = soma - (num / fat)
    if cont == 1:
        print(" = %.2f" % (soma))
    aux = aux + 1
    val = 1
    fat = aux
    cont = cont - 1