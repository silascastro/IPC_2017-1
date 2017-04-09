#---------------------------------------------------------------------------
#Introdução a Programação de Computadores - IPC
#Universidade do Estado do Amazonas - UEA
#
#Ulisses Antonio Da Costa                1515090555
#Thiago ferreira Aranha 		 1715310047 
#vitor simões Azevedo			 1715310025	 			  
#victor hugo de oliveira carreira	 1715310063
#Reinaldo vargas 			 1715310054

#---------------------------------------------------------------------------------------------------

#A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
#Faça um programa capaz de gerar a série até o n−ésimo termo

prev_number = 0
next_number = 1
fibonacci = 0
count = 1

n = int( input('Digite a quantidade de números da sequência fibonacci desejados: '))

while count <= n:
    if n == 1:
        print(prev_number, end = ' ')
    else:
        print(next_number, end = ' ')
        fibonacci = prev_number + next_number
        prev_number = next_number
        next_number = fibonacci
    count += 1
