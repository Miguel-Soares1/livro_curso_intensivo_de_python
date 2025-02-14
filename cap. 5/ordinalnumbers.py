#crie uma lista que armazene numeros de 1 a 9 em ordenancia e em ingles.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for numero in numeros:
    if numero == 1:
        print('1st')
    elif numero == 2:
        print('2nd')
    elif numero == 3:
        print('3rd')
    else:
        print(f'{numero}th')
        #ou print(numero + 'th')