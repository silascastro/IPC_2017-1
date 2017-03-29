nums = (input().split())
a,b,c,d = nums
a = float(a)
b = float(b)
c = float(c)
d = float(d)

if b > c and d > a:
	if c+d > a+b:
		if c > 0 and d > 0:
			if a % 2 == 0:
				print("Variaveis aceitas")
else:
	print("Variaveis invalidas")
