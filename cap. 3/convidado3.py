#3.9 convidados
#convidados = ['p1', 'p2', 'p3']
#print(len(convidados))
 
#3.10 funçoes (10 idiomas da america do sul)
idiomas = ['espanhol', 'portugues', 'ingles', 'alemao', 'italiano', 'arabe', 'chines', 
           'ucraniano', 'japones', 'holandes']

print('qual sao as linguas mais e menos faladas na america do sul')
print(f'a lingua mais falada na america do sul e {idiomas[0].title()}')
print(f'a lingua menos falada na america do sul é {idiomas[-1].title()}')

#adicionando mais dois idiomas ao final da lista, o append serve para 
#inserir um novo item automaticamente ao final da lista, o insert serve para inserir em uma posição determinada
idiomas.append('guarani')
idiomas.insert(-1, 'francês')
print(idiomas)

#ao inves de usar o del para remover o guarani da lista, eu decidi usar o pop e reaproveita-lo em uma outra lista 
popped_idiomas = idiomas.pop()
print(f'as linguas oficiais na america do sul sao{idiomas}, mas tambem existem idiomas indigenas bastante populares como o {popped_idiomas}')

#manipulando a ordem da lista
print(f'a ordem do idioma mais falado pro menos falado e {idiomas}')
#os metodos sort e sorted tambem invertem a lista com o argumento reverse = true exemplo em mundo.py
print(f'a ordem do idioma menos falado pro mais falado e {idiomas.reverse()}')

print(f'a lista em ordem alfabetica fica assim {(idiomas.sort())}')
#len exibe o tamanho da lista
print(len(idiomas))
