lugares =['italia', 'japao', 'frança', 'espanha', 'grecia']
print(lugares)
#sorted exibe a lista em ordem alfabetica, mas nao armazena, ao dar print(lugares) a ordem volta ao normal
print(sorted(lugares))
print(lugares)
#reverse exibe em ordem alfabetica invertida
print(sorted(lugares, reverse= True))
print(lugares)
#reverse inverte a ordem da lista e armazena
lugares.reverse()
print(lugares)
lugares.reverse()
print(lugares)
#o sort armazena a lista em ordem alfabetica, e diferente do sorted, a lista nao volta a ordem anterior
lugares.sort()
print(lugares)
lugares.sort(reverse= True)
print(lugares)