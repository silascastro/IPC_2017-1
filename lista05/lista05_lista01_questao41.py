#---------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
# Adham Lucas da Silva Oliveira           1715310059
# Alexandre Marques Uchôa                 1715310028
# André Luís Laborda Neves                1515070006
# Carlos Eduardo Tapudima de Oliveira	  1715310030
# Aracille de Souza Barbosa               1315120206
# Dayana Picanço Marquez                  1715310058
#
# Faça um programa que receba o valor de uma dívida e mostre uma tabela com
# os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
# Os juros e a quantidade de parcelas seguem a tabela abaixo:

# Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
# 1       0
# 3       10
# 6       15
# 9       20
# 12      25
#----------------------------------------------------------------------------

dept = float(input('Digíte o valor da sua dívida: '))
count = 1
percent_profits = 0
profit = 0
num_parcels = 1
parcel = 0

print(' Valor da Dívida | Quantidade de Parcelas | Valor dos Juros | Valor da Parcela ')
print('-------------------------------------------------------------------------------')

while count <= 5:
    if ( count == 1 ):

        parcel = dept
        print("%.2f" % dept, '         | ', "%.0f" % num_parcels, '                  | ',
              "%.2f" % profit, '        | ', "%.2f" % parcel)
        num_parcels = 3
        percent_profits = 0.10

    else:

        profit = dept * percent_profits
        parcel = ( dept / num_parcels ) + profit
        print("%.2f" % dept, '         | ', "%.0f" % num_parcels, '                  | ',
              "%.2f" % profit, '        | ', "%.2f" % parcel)
        num_parcels += 3
        percent_profits += 0.05
    count +=1
