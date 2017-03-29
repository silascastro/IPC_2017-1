#----------------------------------------------------------------------------------------------------------------------#
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
#
# Adham Lucas da Silva Oliveira         1715310059
# Alexandre Marques Uchôa               1715310028
# André Luís Laborda Neves              1515070006
# Carlos Eduardo Tapudima de Oliveira	  1715310030
# Diego Reis Figueira                   1515070169
#
# Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule
#o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100,50,20,
#10,5,2.As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.
#----------------------------------------------------------------------------------------------------------------------#
N = float(input())

if 0 <= N <= 1000000.00:
  A = N//100
  N = N - (A * 100)

  B = N//50
  N = N - (B * 50)

  C = N//20
  N = N - (C * 20)

  D = N//10
  N = N - (D * 10)

  E = N//5
  N = N - (E *5)

  F = N//2
  N = N - (F * 2)

  G = N//1
  N = N - (G * 1)

  H = N//0.50
  N = N - (H * 0.50)

  I = N//0.25
  N = N - (I * 0.25)

  J = N//0.10
  N = N - (J * 0.10)

  K = N//0.05
  N = N - (K * 0.05)

  L = N//0.01
  N = N - (L * 0.01)

print('NOTAS:')
print('%.0f nota(s) de R$ 100.00' % A)
print('%.0f nota(s) de R$ 50.00' % B)
print('%.0f nota(s) de R$ 20.00' % C)
print('%.0f nota(s) de R$ 10.00' % D)
print('%.0f nota(s) de R$ 5.00' % E)
print('%.0f nota(s) de R$ 2.00' % F)
print('MOEDAS:')
print('%.0f moeda(s) de R$ 1.00' % G)
print('%.0f moeda(s) de R$ 0.50' % H)
print('%.0f moeda(s) de R$ 0.25' % I)
print('%.0f moeda(s) de R$ 0.10' % J)
print('%.0f moeda(s) de R$ 0.05' % K)
print('%.0f moeda(s) de R$ 0.01' % L)



