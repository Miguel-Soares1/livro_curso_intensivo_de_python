def mostrar_mensagens(mensagens, mensagens_enviadas):
    while mensagens:
        mensagem = mensagens.pop()
        print(mensagem.title())
        mensagens_enviadas.append(mensagem)

def mostrar_mensagens2(mensagens_enviadas):
    for mensagem_enviada in mensagens_enviadas:
        print(f'mensagens enviadas: {mensagem_enviada.title()}')

mensagens= ['ola', 'bom dia', 'como vai']
mensagens_enviadas = []

#remover a fatia e a ultima linha do codigo para 8.10
mostrar_mensagens(mensagens[:], mensagens_enviadas)
mostrar_mensagens2(mensagens_enviadas)
#8.10 transfere mensagens para mensagens_enviadas, 8.11 cria uma copia de mensagens 
#e envia ela para mensagens_enviadas
mostrar_mensagens(mensagens, mensagens_enviadas)

