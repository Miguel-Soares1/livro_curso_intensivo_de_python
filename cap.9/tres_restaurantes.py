class Restaurantes:
    
    def __init__ (self, nome_do_restaurante, tipo_de_cozinha):
        self.nome_do_restaurante = nome_do_restaurante
        self.tipo_de_cozinha = tipo_de_cozinha

    def descrever_restaurante(self):
        print(f'O restaurante {self.nome_do_restaurante.title()} possui uma culinaria {self.tipo_de_cozinha.title()}')

    def abrir_restaurante(self):
        print(f'o {self.nome_do_restaurante.title()} está aberto!')

restaurante = Restaurantes('restaurante do miguel', 'brasileira')
restaurante2 = Restaurantes('restaurante do joao', 'chinesa')
restaurante3 = Restaurantes('restaurante do pedro', 'japonesa')

restaurante.abrir_restaurante()
restaurante.descrever_restaurante()
print('\n')

restaurante2.abrir_restaurante()
restaurante2.descrever_restaurante()
print('\n')

restaurante3.abrir_restaurante()
restaurante3.descrever_restaurante()
