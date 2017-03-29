#------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr.
#
# Vitor Summer Oliveira Pantaleão 	1715310042
# Vítor Simões Azevedo 			    1715310025
# Wesley da Silva Rocha			    1715310026
# Wilbert Luís Evangelista Marins 	1715310055
# Yuri Leandro de Aquino Silva 		1615100462
#
# Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo, da esquerda para a direita.
# Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.
# Entrada :A entrada contém 3 palavras, uma em cada linha, necessárias para identificar o animal segundo a figura acima, com todas as letras minúsculas.
# Saída   :Imprima o nome do animal correspondente à entrada fornecida.
#------------------------------------------------------------------------------

ent1 = input()
ent2 = input()
ent3 = input()
if(ent1 == "vertebrado"):
	if(ent2 == "ave"):
		if(ent3 == "carnivoro"):
			print ("aguia")
		else:
			print ("pomba")
	else:
		if(ent3 == "onivoro"):
			print ("homem")
		else:
			print ("vaca")
else:
	if(ent2 == "inseto"):
		if(ent3 == "hematofago"):
			print ("pulga")
		else:
			print ("lagarta")
	else:
		if(ent3 == "hematofago"):
			print ("sanguessuga")
		else:
			print ("minhoca")
