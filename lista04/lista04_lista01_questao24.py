<<<<<<< HEAD
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
#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.

num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
operation = input("Digite a operação desejada (A - Adição, S - Subtração, M - Multiplicação, D - Divisão)")
add = (num1+num2)
sub = (num1-num2)
mult = (num1*num2)
div = (num1/num2)

if operation == "A" or operation == "a" or operation == "S" or operation == "s" or operation == "M" or operation == "m" or operation == "D" or operation == "d":
	if operation == "A" or operation == "a":
		print("Resultado = ", add)
		if add % 2 == 0:
			print("Par")
		else:
			print("Impar")
		if add >= 0:
			print("Numero positivo")
		else:
			print("Numero negativo")
		if round(add) == add:
			print("É inteiro")
		else:
			print("É decimal")

	if operation == "S" or operation == "s":
		print("Resultado = ", sub)
		if sub % 2 == 0:
			print("Par")
		else:
			print("Impar")
		if sub >= 0:
			print("Numero positivo")
		else:
			print("Numero negativo")
		if round(sub) == sub:
			print("É inteiro")
		else:
			print("É decimal")

	elif operation == "M" or operation == "m":
		print("Resultado = ", mult)
		if mult % 2 == 0:
			print("Par")
		else:
			print("Impar")
		if mult >= 0:
			print("Numero positivo")
		else:
			print("Numero negativo")
		if round(mult) == mult:
			print("É inteiro")
		else:
			print("É decimal")

	elif operation == "D" or operation == "d":
		print("Resultado = ", div)
		if div % 2 == 0:
			print("Par")
		else:
			print("Impar")
		if div >= 0:
			print("Numero positivo")
		else:
			print("Numero negativo")
		if round(div) == div:
			print("É inteiro")
		else:
			print("É decimal")
=======
# --------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Tiago Ferreira Aranha                     1715310047
# Ulisses Antonio Antonino da Costa         1515090555
# Rodrigo Duarte de Souza                   1115140049
# Victor Hugo de Oliveira Carreira          1715310063
#
#QUESTAO_24
#Faça um Programa que leia 2 números e em seguida pergunte ao usuário
# qual operação ele deseja realizar. O resultado
#da operação deve ser acompanhado de uma frase que diga se o número é:
#par ou ímpar;
#positivo ou negativo;
#inteiro ou decimal.
x=float(input("n1: "))
y=float(input("n2: "))

op=str(input("escolha a operacao:? (mais, menos, vezes, divisao): "))
if op == 'mais':
    res=x+y
elif op == 'menos':
    res=x-y
elif op== 'vezes':
    res=x*y
elif op== 'divisao':
    res=x/y
else:
    print("operacao invalida!!")




print("resultado", res)
if (res % 2 == 0):
    print("o numero eh par")
else:
    print("o numero eh impar")
if res >0:
    print("positivo")
else:
    print("negativo")
if res==int:
    print("Inteiro")
else:
    print("decimal")
>>>>>>> 04461ffcd8d5832b2f4ad858704ee67e9db29a85
