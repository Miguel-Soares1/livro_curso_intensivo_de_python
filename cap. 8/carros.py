def make_car (marca, modelo, **carro_info):
    carro_info['fabricante'] = marca
    carro_info['modelo'] = modelo
    return carro_info

carro = make_car('subaru', 'outback', cor='azul', pacote_de_reboque=True)

print(carro)