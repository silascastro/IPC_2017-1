#------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr.
#
# João Vitor de Cordeiro B. Gonçalves   1515140036
# Joelson Pereira Lima                  1715310060
# Judá Salazar Braga                    1515200050
# Kethelen Tamara Braga Barbosa         1525212002
# Lucas Gabriel Silveira                1715310053


print("Digite M para masculino e F para feminino")
gender = input("Digite \"M\" ou \"F\": ")

if gender == "M":
	print("O gênero digitado foi MASCULINO")
else:
	if gender == "F":
		print("O gênero digitado foi FEMININO")
	else:
		print("O gênero digitado é INVÁLIDO")
