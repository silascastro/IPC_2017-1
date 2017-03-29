n1, n2, n3, n4 = input().split()

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

n1 = n1 * 2
n2 = n2 * 3
n3 = n3 * 4
n4 = n4 * 1

Media = (n1 + n2 + n3 + n4)/10
if Media >= 5.0 and Media <= 6.9:
    n5 = float(input())
print("Media: %.1f" %Media)

if Media >= 7.0:
    print("Aluno aprovado.")

if Media < 5.0:
        print("Aluno reprovado.")

if Media >= 5.0 and Media <= 6.9:
    print("Aluno em exame.")


    print("Nota do exame:",n5)
    Media2 = (n5 + Media)/2

    if Media2 >= 5.0:
        print("Aluno aprovado.")
        print("Media final: %.1f" %Media2)
    else:
        print("Aluno reprovado.")
        print("Media final: %.1f" %Media2)