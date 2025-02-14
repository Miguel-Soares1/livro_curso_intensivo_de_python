idade = int(input('insira sua idade: '))
while idade < 3:
    print('preço do ingresso: gratuito')
    break
while idade >= 3 and idade <= 12:
    print('preço do ingresso: 10 R$')
    break
while idade > 12:
    print('preço do', 'ingresso: 15 R$')
    break