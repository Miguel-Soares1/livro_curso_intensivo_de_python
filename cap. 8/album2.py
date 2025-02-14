def criando_album (artista, album,):
    album = {'artista': artista, 'album': album}
    return album   
while True:
    print('digite "q" para sair')
    artista = input('digite o nome do artista: ')
    if artista == 'q':
        break
    album = input('digite o nome do album: ')
    if album == 'q':
        break
    print(f'artista: {artista.title()}, album: {album.title()}')
