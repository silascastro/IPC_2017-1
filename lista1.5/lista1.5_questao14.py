print ('---------------------Subtração de 2 números---------------------')
try:
    a = input ('Digite o ano atual: ')
    a = int(a)
    b = input ('Digite o ano de nascimento: ')
    b = int(b)
    c = a - b
    d = c * 12
    e = c * 365
    f = c * 48
    print ('A soma: ',a,'  - ',b,' é igual a : ',c,' que é a idade da pessoa em anos')
    print(' A multiplicação ',c,' * ',12,' é igual a : ',d,' que é a idade da pessoa em meses')
    print(' A multiplicação ',c,' * ',365,' é igual a : ',e,' que é a idade da pessoa em dias')
    print('A multiplicação ',c,' * ',48,' é igual a: ',f,' que é a idade da pessoa em semanas')
except ValueError:
    print('Somente números são aceitos, tente novamente!')

