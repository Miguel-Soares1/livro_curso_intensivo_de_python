class User:
    def __init__ (self, primeiro_nome, sobrenome, idade, cidade, cor_favorita, sexo):
        self.primeiro_nome = primeiro_nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.cidade = cidade
        self.cor_favorita = cor_favorita
        self.sexo = sexo

    def descrever_user(self):
        print(f'Nome: {self.primeiro_nome.title()} Sobrenome: {self.sobrenome.title()}\nIdade: {self.idade}\nCidade: {self.cidade.title()}\n Cor favorita: {self.cor_favorita.title()}\n Sexo: {self.sexo.title()}')
        
    def cumprimentar_user(self):
        if self.sexo == 'masculino':
            print(f'Olá {self.primeiro_nome.title()}, seja bem vindo!')
        else:
            print(f'Olá {self.primeiro_nome.title()}, seja bem vinda!')

user1 = User ('miguel', 'soares', 19, 'teresopolis', 'preto', 'masculino')
user2 = User ('everaldo', 'pereira', 53, 'maringa', 'azul', 'masculino')
user3 = User ('julia', 'souza', 27, 'rio de janeiro', 'verde', 'feminino')        

user1.descrever_user()
user1.cumprimentar_user()
print('\n')

user2.descrever_user()
user2.cumprimentar_user()
print('\n')

user3.descrever_user()
user3.cumprimentar_user()