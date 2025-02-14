carro = 'subaru'
print('carro é == subaru? eu prevejo que sim')
print(carro == 'subaru')

print('\ncarro é == audi? eu prevejo que nao')
print(carro == 'audi')

nome = 'miguel'
print('\nnome é != a joao? eu prevejo que nao')
print(nome != 'joao')

print('\nnome é != a miguel? eu prevejo que sim')
print(nome != 'miguel')

pet = 'Cachorro'
print('\no pet é == cachorro? eu prevejo que sim')
print(pet.lower() == 'cachorro')

print('\no pet é == gato? eu prevejo que nao')
print(pet.lower() == 'gato')

idade = int(input('insira sua idade'))
if idade < 16:
    print('você nao pode votar')

elif idade == 16:
    print('você pode votar opcionalmente')

elif idade ==17:
    print('voce pode votar opcionalmente')

else:
    print('voce deve votar obrigatoriamente')


    

