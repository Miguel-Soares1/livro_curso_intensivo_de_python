fav_lang = {
    'miguel': 'python',
    'everaldo': 'rust',
    'joao': 'java',
    'matheus': 'javascript',
}
nomes = {
    'miguel','everaldo','joao','matheus'
}
for nome in fav_lang.keys():
    if nome in nomes:
        print(f'obrigado por participar {nome.title()}!\n')
    if 'pedro' not in fav_lang.keys():
        print('pedro, voce deveria participar da nossa enquete!')