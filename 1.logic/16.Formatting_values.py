# Formatando valores com modificadores - Aula 16

# :s - Texto (strings)
# :d - Inteiros (int)
# :f - Números de ponto flutuante (float)
#  :.(NÚMERO)f -  Quantidade de casas decimais (float) ex:  :.2f - 2 casas decimais
# :(CARACTERE) (> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

# > - Esquerda
# < - Direita
# ^ - Centro

num_1 = 1
print(f'{num_1:0>10}')  # 10 Casas decimais para a esquerda

num_2 = 1150
print(f'{num_2:0<10}')  # 10 Casas decimais para a direita

num_3 = 17628
print(f'{num_3:0^10}')  # 10 Casas decimais no centro


# name = "Rodrigo Barros"
# name_formatado = '{:@>40}'.format(name)  # Preencher o nome com @ até chegar 40 caracteres...
# print(name_formatado)

nome = "Rodrigo"
sobrenome = "Barros"
nome_formatado = '{0:*^10} {1:*^10}'.format(nome, sobrenome)  # Nessa situação foi escolhida cada string separadamente
print(nome_formatado)


# More Functions

nome = "Rodrigo Barros"

print(nome.lower())  # tudo minusculo
print(nome.upper())  # tudo maiusculo
print(nome.title())  # Primeiras letras maiusculas
