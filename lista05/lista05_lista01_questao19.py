#----------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Evandro Padilha Barroso Filho     1715310009 
# Gabriel Barroso da Silva Lima     1715310011
# Frederico Victor Alfaia Rodrigues 1515200030 
# Felipe Eduardo Silva de Almeida   1715310031 
# Felipe Guerreiro De Mello         1315120052 
# Silas castro de Mendonça          1715310066
#
#19.Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
#
#----------------------------------------------------------------
#Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
n_numbers = float(input("Digite o tamanho de um conjunto (números de 0-10000): "))

while n_numbers < 0 or n_numbers > 10000:
    print("Número inválido, digite novamente")
    n_numbers = float(input("Digite o tamanho de um conjunto (números de 0-10000): "))

counter = 1
sum = 0
lowest = 0
higher = n_numbers
position = 0

while counter <= n_numbers:
    position = counter
    sum = sum + position
    counter = counter + 1

print("O menor numero é: ", lowest)
print("O maior numero é: ", higher)
print("A soma é: ", sum)

