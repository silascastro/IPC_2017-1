number1 = int(input("digite um número: "))
number2 = int(input("digite mais um número: "))
number3 = int(input("digite mais um número: "))
number4 = int(input("digite mais um número: "))
number5 = int(input("digite mais um número: "))

while numb1 > numb2 and numb1 > numb3 and numb1 > numb4 and numb1 > numb5:
    print("o maior número é o: ", numb1)
    break
while numb2 > numb1 and numb2 > numb3 and numb2 > numb4 and numb2 > numb5:
    print("o maior número é o: ", numb2)
    break
while numb3 > numb1 and numb3 > numb2 and numb3 > numb4 and numb3 > numb5:
    print("o maior número é o: ", numb3)
    break
while numb4 > numb1 and numb4 > numb2 and numb4 > numb3 and numb4 > numb5:
    print("o maior número é o: ", numb4)
    break
while numb5 > numb1 and numb5 > numb2 and numb5 > numb3 and numb5 > numb4:
    print("o maior número é o: ", numb5)
    break
else:
    print("operação invalida! números iguais")
