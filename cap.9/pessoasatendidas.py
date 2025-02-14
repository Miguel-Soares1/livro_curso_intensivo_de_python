class Restaurante:
    
    def __init__ (self, nome_do_restaurante, tipo_de_cozinha):
        self.nome_do_restaurante = nome_do_restaurante
        self.tipo_de_cozinha = tipo_de_cozinha
        self.pessoas_atendidas = 0

    def descrever_restaurante(self):
        print(f'O restaurante {self.nome_do_restaurante.title()} possui uma culinaria {self.tipo_de_cozinha.title()}')

    def abrir_restaurante(self):
        print(f'o {self.nome_do_restaurante.title()} está aberto!')

    def clientes_atendidos(self):
        print(f'{self.pessoas_atendidas} pessoas foram atendidas!')

    def set_pessoas_atendidas (self, pessoas):
        self.pessoas_atendidas = pessoas

    def increment_pessoas_atendidas (self, atendidos):
        self.pessoas_atendidas += atendidos


restaurante = Restaurante('restaurante do miguel', 'brasileira')
restaurante.pessoas_atendidas = 10
restaurante.abrir_restaurante()
restaurante.descrever_restaurante()
restaurante.clientes_atendidos()
restaurante.set_pessoas_atendidas(20)
restaurante.clientes_atendidos()
restaurante.increment_pessoas_atendidas(5)
restaurante.clientes_atendidos()