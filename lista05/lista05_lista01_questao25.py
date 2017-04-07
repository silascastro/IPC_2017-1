n_person = int(input("Digite o número de pessoas da turma: "))

cont = 0
sum_age = 0

while cont < n_person :
    age = int(input("Digite a idade: "))
    sum_age = sum_age + age
    cont += 1

average_age = sum_age / n_person

if 0 < average_age <= 25 :
    print ('A Turma é jovem')

if 26 <= average_age <= 60 :
    print ('A Turma é adulta')

if average_age > 60 :
    print ('A turma é velha')