import pytest
from funcionario import Employee

@pytest.fixture
def __init__ (self, primeiro_nome, sobrenome, salario_anual=5000):
        self.primeiro_nome = primeiro_nome
        self.sobrenome = sobrenome
        self.salario_anual = int(salario_anual)
    
def test_give_default_raise():
    funcionario = Employee('miguel', 'soares', '5000')
    funcionario.give_raise()
    assert funcionario.salario_anual == 10000

def test_give_custom_raise():
    funcionario = Employee('miguel', 'soares', '5000')
    funcionario.give_raise(10000)
    assert funcionario.salario_anual == 15000
    