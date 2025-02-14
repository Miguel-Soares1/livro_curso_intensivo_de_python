cidade = {
    'paris': {
        'país': 'frança',
        'população': '2 milhões',
        'fato': 'O nome Paris tem origem na mitologia grega. Ele corresponde ao nome do filho de Príamo e Hécuba, reis de Troia'
},
    'são paulo': {
        'país': 'brasil',
        'população': '12 milhões',
        'fato': 'O nome São Paulo tem origem no latim. Ele corresponde ao nome do filho de São Paulo e João Paulo, reis de São Paulo' 
},
    'lisboa': {
        'país': 'portugal',
        'população': '5 milhões',
        'fato': 'O nome Lisboa tem origem no latim. Ele corresponde ao nome do filho de Lisboa e Luís, reis de Lisboa'
    }
}
for cidade, informacao in cidade.items():
    país = informacao['país']
    populacao = informacao['população']
    fato = informacao['fato']
    print(f'\nA cidade {cidade.title()} esta localizada no pais {país.title()} e tem {populacao} de habitantes')
    print(f'\nAqui esta um fato sobre {cidade.title()}: {fato}')