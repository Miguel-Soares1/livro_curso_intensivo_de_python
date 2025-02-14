class Restaurante:
    
    def __init__ (self, nome_do_restaurante, tipo_de_cozinha):
        self.nome_do_restaurante = nome_do_restaurante
        self.tipo_de_cozinha = tipo_de_cozinha

    def descrever_restaurante(self):
        print(f'O restaurante {self.nome_do_restaurante.title()} possui uma culinaria {self.tipo_de_cozinha.title()}')

    def abrir_restaurante(self):
        print(f'o {self.nome_do_restaurante.title()} está aberto!')

restaurante = Restaurante('restaurante do miguel', 'brasileira')
restaurante.abrir_restaurante()
restaurante.descrever_restaurante()