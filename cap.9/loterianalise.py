from random import sample
lista = ['a', 6, 10, 'q', 't', 'e', 22, 31, 3, 'p', 46, 8, 7, 1, 0]
my_ticket = ['q', 6, 31, 1]
resultado = sample(lista, 4)

if resultado != my_ticket:
    print(resultado)
    print('voce perdeu')
else:
    print(resultado)
    print('voce ganhou')