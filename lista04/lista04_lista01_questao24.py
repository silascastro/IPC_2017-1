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
