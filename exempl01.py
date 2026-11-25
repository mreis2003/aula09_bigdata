produto1 = {}  # Dicionário vazio

produto = {
    'nome' : 'Notebook',
    'preço': 3500.80,
    'marca': 'lenovo'
}

# type(produto)
print(produto) # todas as chaves e valores

print(produto['nome']) # chave nome
print(produto['preço']) # chave preço

# Slterando o valor
produto['marca']) = 'Positivo'
print(produto)['marca]']

# Adicionando Chaves
produto['tela'] = '18'
print(produto)

# deletando uma chave
del produto['marca']
print(produto)

print(produto.keys()) # chaves
print(produto.values()) # Valores
print(produto.items()) # Valores