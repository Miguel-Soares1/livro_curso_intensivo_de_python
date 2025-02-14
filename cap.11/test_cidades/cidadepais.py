def get_formatted_cidadepais (cidade, pais, populacao= ''):
    cidadepais = f'{cidade}, {pais} - population {populacao}'
    return cidadepais.title()