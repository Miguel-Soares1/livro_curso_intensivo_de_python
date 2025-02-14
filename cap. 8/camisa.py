def fazer_camisa(tamanho = 'g', texto = 'eu amo python'):
    print(f'\ntamanho da camisa: {tamanho.title()}')
    print(f'texto da camisa: {texto.title()}')

#8.3 
#fazer_camisa('m', 'curso intensivo de python')
#fazer_camisa(tamanho = 'm', texto = 'curso intensivo de python')

fazer_camisa()
fazer_camisa(tamanho = 'm')
fazer_camisa(tamanho = 'p', texto = 'curso intensivo de python')