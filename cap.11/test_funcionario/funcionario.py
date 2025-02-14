#crie uma classe chamada employee e crie um metodo chamado give_raise que recebe um argumento para aumento de salario.
#defina o valor default para o aumento de 5000.
class Employee:
    def __init__ (self, primeiro_nome, sobrenome, salario_anual):
        self.primeiro_nome = primeiro_nome
        self.sobrenome = sobrenome
        self.salario_anual = int(salario_anual)

    def give_raise(self, aumento=5000):
        self.salario_anual += aumento
