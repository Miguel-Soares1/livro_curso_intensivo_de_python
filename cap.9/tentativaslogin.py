class User:
    def __init__ (self, primeiro_nome, sobrenome, idade, cidade, cor_favorita, sexo):
        self.primeiro_nome = primeiro_nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.cidade = cidade
        self.cor_favorita = cor_favorita
        self.sexo = sexo
        self.tentativas_de_login = 0

    def descrever_user(self):
        print(f'Nome: {self.primeiro_nome.title()} Sobrenome: {self.sobrenome.title()}\nIdade: {self.idade}\nCidade: {self.cidade.title()}\n Cor favorita: {self.cor_favorita.title()}\n Sexo: {self.sexo.title()}')
        
    def cumprimentar_user(self):
        if self.sexo == 'masculino':
            print(f'Olá {self.primeiro_nome.title()}, seja bem vindo!')
        else:
            print(f'Olá {self.primeiro_nome.title()}, seja bem vinda!')

    def exibir_tentativas_de_login(self):
        print(f'voce tentou logar na sua conta {self.tentativas_de_login} vezes')
    
    def increment_tentativas_de_login(self, tentativas):
        self.tentativas_de_login += tentativas

    def resetar_tentativas_de_login(self,):
        self.tentativas_de_login = 0


user1 = User ('miguel', 'soares', 19, 'teresopolis', 'preto', 'masculino')
  
user1.descrever_user()
user1.cumprimentar_user()
user1.increment_tentativas_de_login(1)
user1.exibir_tentativas_de_login()
user1.resetar_tentativas_de_login()
user1.exibir_tentativas_de_login()
user1.increment_tentativas_de_login(3)
user1.increment_tentativas_de_login(2)
user1.increment_tentativas_de_login(9)
user1.exibir_tentativas_de_login()
user1.resetar_tentativas_de_login()
user1.exibir_tentativas_de_login()