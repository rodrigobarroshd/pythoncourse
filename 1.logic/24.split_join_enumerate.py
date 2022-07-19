
# Split, Join, Enumerate em Python

# Split - Dividir uma string
# Join - Juntar uma lista
# Enumerate - Enumerar elementos da lista # iteráveis


string = "o Bahia é o Mundo, BBMP"
lista1 = string.split(' ')  #  ['O', 'Bahia', 'é', 'o', 'Mundo,', 'BBMP']
lista2 = string.split(',')  #  ['O Bahia é o Mundo', ' BBMP']
print(lista1)
print(lista2)

# for valor in lista1:
    # print(f'A palavra {valor} apareceu {lista1.count(valor)}x na frase...')

palavra = ''
contagem = 0
for valor in lista1:
    qtd_vezes = lista1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x)')

lista = string.split(' ')
for indice, valor in enumerate(lista):
    print(indice, valor) 
