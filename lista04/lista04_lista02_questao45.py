nums = (input().split())
A,B,C = nums
A = float(A)
B = float(B)
C = float(C)

if A >= B+C:
	print("Não forma triangulo")
else:
    if (A**2) == (B**2)+(C**2):
        print("Triangulo retângulo")
    if (A**2) > (B**2)+(C**2):
        print("Triangulo obtusangulo")
    if (A**2) < (B**2)+(C**2):
        print("Triangulo acutangulo")
if A == B and A == C and B == C:
        print("Triangulo equilatero")
else:
    if A == B or B == C or C == A:
        print("Triangulo isósceles")
