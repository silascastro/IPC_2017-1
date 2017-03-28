dia = int(input("Digite um numero de 1 a 7: "))
if dia == 1 or dia == 2 or dia == 3 or dia == 4 or dia == 5 or dia == 6 or dia == 7:
	if dia == 1:
		print("DOMINGO")
	if dia == 2:
		print("SEGUNDA")
	if dia == 3:
		print("TERÇA")
	if dia == 4:
		print("QUARTA")
	if dia == 5:
		print("QUINTA")
	if dia == 6:
		print("SEXTA")
	if dia == 7:
		print("SABADO")
else:
	print("O numero digitado é invalido")
