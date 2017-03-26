a, b, c, d = input().split()
A = float(a)
B = float(b)
C = float(c)
D = float(d)

if(B > C and D > C and C+D > A+B and C > 0 or D > 0 and (A/2) == 0):
    print('Valores aceitos')
else:
    print('Valores nao aceitos')
