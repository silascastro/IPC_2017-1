
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
#
#Ulisses Antonio Da Costa                1515090555
#Thiago ferreira Aranha 		 1715310047 
#vitor simões Azevedo			 1715310025	 			  
#victor hugo de oliveira carreira	 1715310063
#Reinaldo vargas 			 1715310054

#---------------------------------------------------------------------------------------------------

#A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
#Faça um programa capaz de gerar a série até o n−ésimo termo

previous = 1
next = 1
fibonacci = 0

while fibonacci < 55:

    fibonacci = previous
    previous = next
    next = fibonacci + previous

    print(fibonacci, end="...")
