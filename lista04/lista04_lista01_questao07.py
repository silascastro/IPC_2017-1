n1 = float(input('Digite um numero: '))
n2 = float(input('Digite um numero: '))
n3 = float(input('Digite um numero: '))

lower = n1
if n2 < lower:
	lower = n2 
if n3 < lower:
	lower = n3
higher = n1
if n2 > higher:
	higher = n2
if n3 > higher:
	higher = n3

print('O menor é: %d' %lower)
print('O maior é: %d' %higher)
