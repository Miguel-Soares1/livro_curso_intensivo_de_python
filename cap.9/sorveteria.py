class Restaurante:
    
    def __init__ (self, nome_do_restaurante, tipo_de_cozinha):
        self.nome_do_restaurante = nome_do_restaurante
        self.tipo_de_cozinha = tipo_de_cozinha

    def descrever_restaurante(self):
        print(f'O restaurante {self.nome_do_restaurante.title()} possui uma culinaria {self.tipo_de_cozinha.title()}')

    def abrir_restaurante(self):
        print(f'o {self.nome_do_restaurante.title()} está aberto!')

class BarracaDeSorvete(Restaurante):
    def __init__ (self, nome_do_restaurante, tipo_de_cozinha):
        super().__init__ (nome_do_restaurante, tipo_de_cozinha)
        self.sabores = ['morango', 'baunilha', 'chocolate', 'coco']

    def sabores_disponiveis(self):
        print(f'Os sabores disponíveis sao: {self.sabores}')
        
info_restaurante = BarracaDeSorvete('restaurante do miguel', 'brasileira')
info_restaurante.abrir_restaurante()
info_restaurante.descrever_restaurante()
info_restaurante.sabores_disponiveis()
