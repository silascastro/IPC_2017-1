classes = int(input("Informe o número de turmas "))

c = 0
sum = 0

while c < classes:
    students = int(input("Quantidades de alunos da turma: "))
    if students <= 40:
        sum = sum + students
        c = c + 1
    else:
        print("As turmas não podem ter mais de 40 alunos!")

average = sum/ c

print("A média de alunos por tuma é = ",int(average))
