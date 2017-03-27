
value = input().split()

a, b, c = value
pi = 3.14159

triangle = (float(a) * float(c))/2
circule = pi * (float(c)* float(c))
trapezius = float(c) *(float(a) + float(b)) / 2
square = float(b) * float(b)
rectangle = float(a) * float(b)


print("TRIANGULO: %0.3f"%triangle)
print("CIRCULO: %0.3f"%circule)
print("TRAPEZIO: %0.3f"%trapezius)
print("QUADRADO: %0.3f"%square)
print("RETANGULO: %0.3f"%rectangle)
