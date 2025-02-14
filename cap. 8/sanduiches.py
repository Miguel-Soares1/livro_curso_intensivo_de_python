def lista_items(*items):
        """exibe um resumo de uma lista de itens, com um parametro que
        colete todos os itens fornecidos na chamada da função"""
        print('\nvoce pediu os seguinte itens: ')
        for item in items:
                print(f'- {item.title()}')

lista_items('pepperoni')
lista_items('queijo', 'frango')
lista_items('batata', 'carne', 'ovo')
