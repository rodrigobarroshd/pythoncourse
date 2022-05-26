
# For in em Python
# Iterando strings com FOR
# Função range(start=0, stop, step=1)

# texto = 'Python'


# for n in range(0, 20, 3):  # Vai do 0 ao 20 pulando de 3 em 3...
#     print(n)
    

##################################################

texto = 'Python'
nova_string = ''

for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
        break
    else:
        nova_string += letra
        
print(nova_string)