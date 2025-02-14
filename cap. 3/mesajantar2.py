convidados = ['p1', 'p2', 'p3']

print('uma mesa para 6 lugares está vazia!')

convidados.insert(0, 'p4')
convidados.insert(2, 'p5')
convidados.append('p6')

print('a mesa de 6 lugares esta ocupada. apenas uma mesa de 3 lugares esta disponivel')

popped_convidados = convidados.pop(5)
print(f'{popped_convidados} lamentamos nao podermos convida-lo')

popped_convidados2 = convidados.pop(4)
print(f'{popped_convidados2} lamentamos nao podermos convida-lo')

popped_convidados3 = convidados.pop(3)
print(f'{popped_convidados3} lamentamos nao podermos convida-lo')

popped_convidados4 = convidados.pop(2)
print(f'{popped_convidados4} lamentamos nao podermos convida-lo')

print(popped_convidados, popped_convidados2, popped_convidados3, popped_convidados4)
print(f'{convidados} voces ainda estao convidados!')

del convidados[0]
del convidados[0]
print(f'{convidados}')