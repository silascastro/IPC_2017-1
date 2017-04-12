a = int(input())
count = 1
s = 0
final = a
while count <= final:
    s = s + (count/a)
    count += 1
    a -= 1
print (s)