def cidade_pais(cidade, pais):
    locais = f'{cidade.title()}, {pais.title()}'
    return locais

formatado = cidade_pais('rio de janeiro', 'brasil')
print(formatado)

formatado = cidade_pais('dublin', 'irlanda')
print(formatado)

formatado = cidade_pais('lima', 'peru')
print(formatado)