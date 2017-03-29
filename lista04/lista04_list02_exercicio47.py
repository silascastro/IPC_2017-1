hora_inicial = float(input('informe a hora inicial'))
minuto_inicial = int(input('informe o minuto inicial'))
hora_final= int(input('informe a hora final'))
minuto_final= int(input('informe o minuto final'))

calculando_time = (hora_inicial + hora_final)
minutoscalc = (minuto_inicial + minuto_final)

print('O jogo durou:', calculando_time, 'horas', 'e', minutoscalc, 'minutos')