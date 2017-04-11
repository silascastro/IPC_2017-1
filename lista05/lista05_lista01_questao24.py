quantidade = int(input("Quantidade de médias "))
contador = 0
variavel = 0
while contador < quantidade:
    medias = float(input("Média %d: " % (contador+1)))
    variavel = variavel + medias
    contador += 1;
variavel = variavel / quantidade
print("A média aritmética é %.2f" % variavel)