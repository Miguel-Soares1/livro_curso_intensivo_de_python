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

class Admin(User):
    def __init__(self, primeiro_nome, sobrenome, idade, cidade, cor_favorita, sexo):
        super().__init__(primeiro_nome, sobrenome, idade, cidade, cor_favorita, sexo)
        self.previlegios = ['pode adicionar post', 'pode deletar post', 'pode banir user']

    def mostrar_previlegios(self):
        for previlegio in self.previlegios:
            print(f'os previlegios do admin sao: {previlegio}')

class Previlegios(Admin):
    def __init__(self, mostrar_previlegios):
        self.mostrar_previlegios = mostrar_previlegios

                