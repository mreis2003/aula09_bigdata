lista_catalogo = []

for i in range(3):
    print(f'\nlivro{i+1}')
    livro = {}

    livro['título'] = input('informe o nome do livro: ')
    livro['autor'] = input('informe o autor do livro: ')
    livro['ano'] = int(input('informe o ano de publicação: '))
    livro['genero'] = input('informe o gênero: ')
    livro['autor'] = input('informe o número de páginas: ')

    lista_catalogo.append(livro)

# print(lista_catalogo)
for elemento in lista_catalogo: # 3 vezes
    #print(elemento)
    if elemento['ano'] >= 2020:
        print(f'elemento')





