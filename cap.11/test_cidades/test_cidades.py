from cidadepais import get_formatted_cidadepais

def get_formatted_cidadepais (cidade, pais, populacao=''):
    if populacao:
        cidadepais = f'{cidade}, {pais} - population {populacao}'
    else:
        cidadepais = f'{cidade}, {pais}
    return cidadepais.title()

def test_cidadepais():
    formatted_cidpais = get_formatted_cidadepais('santiago', 'chile')
    assert formatted_cidpais == 'Santiago, Chile'

def test_cidadepais_populacao():
    formatted_cidpais = get_formatted_cidadepais('santiago', 'chile', populacao=5000000)
    assert formatted_cidpais == 'Santiago, Chile - population 5000000'

