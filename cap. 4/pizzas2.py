pizzas = ['frango', 'pepperoni', 'portuguesa']
friend_pizzas = pizzas [:]

pizzas.append('abacaxi')
friend_pizzas.append('abacate')

print('minhas pizzas favoritas sao:')
for pizza in pizzas:
    print(pizza)

print ('minhas pizzas favoritas sao:')
for friendpizza in friend_pizzas:
    print(friendpizza)
