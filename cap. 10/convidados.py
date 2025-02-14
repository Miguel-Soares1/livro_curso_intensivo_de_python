"""escreva um programa que solicite ao usuario o seu nome. quando responder, escreva o nome 
dele em um arquivo chamado convidados.txt"""
from pathlib import Path
nome = input('insira seu nome: ')
path = Path('convidados.txt')
path.write_text(nome)
