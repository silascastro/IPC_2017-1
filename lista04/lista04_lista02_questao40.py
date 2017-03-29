# ------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
#Prof. Jucimar Jr
# Aracille de souza Barbosa - 1315120206
#
# --------------------------------------------------------------------------------------------------------------------
n1= float(input("Informe a 1º nota: "))
n2= float(input("Informe a 2º nota: "))
n3= float(input("Informe a 3º nota: "))
n4= float(input("Informe a 4º nota: "))
n1p=n1*2
n2p=n2*3
n3p=n3*4
n4p=n4*1
media= ((n1p+n2p+n3p+n4p)/4)
print("Média: %.1f" %media)
if media>= 7.0:
    print("Aluno aprovado")
elif media< 5.0:
    print("Aluno reprovado")
elif 5<=media<=6.9:
    print("Aluno em exame")
if 5<=media<=6.9:
    exame=float(input("Nota do exame:"))
    media2=((media+exame)/2)
    print("Média do exame: %.1f" %media2)
    if media2 >=5:
        print("aprovado!")
    else:
        print("Reprovado no Exame")
