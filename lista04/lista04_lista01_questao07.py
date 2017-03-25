a = float(input('Digite um numero: '))
b = float(input('Digite um numero: '))
c = float(input('Digite um numero: '))

lower = a
if b < lower:
	lower = b 
if c < lower:
	lower = c
higher = a
if b > higher:
	higher = b
if c > higher:
	higher = c

print('O menor é: %d' %lower)
print('O maior é: %d' %higher)
