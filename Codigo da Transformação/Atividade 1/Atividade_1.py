from datetime import datetime # Importa a classe datetime do módulo datetime para trabalhar com datas e horas
data_atual = datetime.now() # Obtém a data e hora atual
hora_atual = data_atual.strftime("%H:%M:%S") # Formata a hora atual no formato HH:MM:SS

nome = input("Digite seu nome: ") # Solicita ao usuário que digite seu nome e armazena a entrada na variável 'nome'
print(f"Seja bem-vindo(a), {nome}! Hoje é {data_atual.strftime('%d/%m/%Y')} e são {hora_atual} horas.") # Exibe uma mensagem de boas-vindas ao usuário, incluindo a data atual formatada como DD/MM/AAAA e a hora atual formatada como HH:MM:SS