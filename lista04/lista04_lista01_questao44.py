a,b = raw_input().split()
a = int(a)
b = int(b)

num1 = a % b
num2 = b % a

if num1 == 0 or num2 == 0:
    print ("Sao Multiplos")
else:
    print ("Nao sao Multiplos")