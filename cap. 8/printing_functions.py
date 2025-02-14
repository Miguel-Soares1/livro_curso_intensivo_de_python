def print_models(unprinted_designs, completed_models):
    """Simula a impressão de cada design, até que não reste nenhum.
     Passa cada design para completed_models apos impressão. """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f'Imprimindo: {current_design.title()}')
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Mostra todos os modelos impressos."""
    print('\nOs seguintes modelos foram imprimidos:')
    for completed_model in completed_models:
        print(completed_model.title())