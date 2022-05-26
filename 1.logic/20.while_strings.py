
# Índices
#          0123456789...........33
# frase = 'o rato roeu a roupa do rei de roma' # Iterável
# tamanho_frase = len(frase)
# contador = 0
# nova_string = ''

# Iteração
# while contador < tamanho_frase:
#     
#     contador += 1
#     nova_string += frase[contador]
#     print(nova_string)
    
    
######################################################

# while contador < tamanho_frase:
#     letra = frase[contador]
#     if letra == 'r':
#         nova_string += 'R'
#     else:
#         nova_string += letra
#     contador += 1

# print(nova_string)

###################################


frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''

input_usuario = input('Qual letra deseja colocar maiscula: ')

while contador < tamanho_frase:
    letra = frase[contador]
    if letra == input_usuario:
        nova_string += input_usuario.upper()
    else:
        nova_string += letra
    contador += 1

print(nova_string)