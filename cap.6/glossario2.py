glossario = {}
glossario['capitulo 1'] = 'python'
glossario['capitulo 2'] = 'dados'
glossario['capitulo 3'] = 'lists'
glossario['capitulo 4'] = 'range'
glossario['capitulo 5'] = 'boolean'

for key, value in glossario.items():
    print(f'eu aprendi {value} no {key} do livro\n')

glossario['capitulo 1'] = 'vs code'
glossario['capitulo 2'] = 'zen do python'
glossario['capitulo 3'] = 'sort'
glossario['capitulo 4'] = 'tupla'
glossario['capitulo 5'] = 'if-elif-else'

for key, value in glossario.items():
    print(f'eu aprendi {value} no {key} do livro\n')