# For / Else em Python

variavel = ['Rodrigo', 'Rjos', 'Jaria']

# for valor in variavel:
#     print(valor) 
#     continue
# print(valor)


comeca_j = False
for valor in variavel:
    if valor.startswith('J'):
        comeca_j = True
    
if comeca_j: 
    print('Existe uma palavra que começa com J.')
else:
    print('Não existe uma palavra que começa com J.')

