# Funções - def em Python 

def funcao(msg='olá', nome='usuario'):
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')
    return f'{msg} {nome}'
    

variavel = funcao()
print(variavel)