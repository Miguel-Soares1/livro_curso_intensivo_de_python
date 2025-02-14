def criando_album (artista, album, musicas = None):
    album = {'artista': artista, 'album': album}
    return album   
    
album_formatado = criando_album('led zeppelin', 'led zeppelin IV')
print(album_formatado)

album_formatado = criando_album('kendrick lamar', 'good kid maad city')
print(album_formatado)

def criando_album2 (artista, album, musicas = None):
    album = {'artista': artista, 'album': album}
    if musicas:
        album['musicas'] = musicas
    return album

album_formatado = criando_album2 ('michael jackson', 'thriller', musicas = 9)
print(album_formatado)
   