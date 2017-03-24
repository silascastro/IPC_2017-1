group_count = int(input('Quantidade de grupos: '))
problem_count = int(input('Quantidade de questões: '))

groups = []
for i in range(group_count):
    groups.append([])

for i in range(problem_count):
    index = i%len(groups)
    groups[index].append(i+1)

for i in range(len(groups)):
    print('Grupo ' + str(i+1) + ' = ' + str(groups[i]))
