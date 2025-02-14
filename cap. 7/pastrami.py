pedidos_sanduiches = ['carne', 'frango', 'atum', 'vegetariano', 'pastrami' , 'pastrami', 'pastrami']
sanduiches_finalizados = []

print('a lanchonete esta sem pastrami')
while 'pastrami' in pedidos_sanduiches:
    pedidos_sanduiches.remove('pastrami')

san_active = True
while pedidos_sanduiches:
    pedido = pedidos_sanduiches.pop()
    print(f'o sanduiche de {pedido} foi finalizado.')
    sanduiches_finalizados.append(pedido)
    if not pedidos_sanduiches:
        san_active = False
    for sanduiche in sanduiches_finalizados:
        print(f'sanduiches prontos: {sanduiche}')