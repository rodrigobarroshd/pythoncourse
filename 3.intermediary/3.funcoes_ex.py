# 1 - Crie uma função que exibe uma saudação com os parâmetros "Saudação" e "Nome".



# def saudacao(msg='olá', nome='usuario'):
#     nome = nome.replace('e', '3')
#     msg = msg.replace('e', '3')
#     return f'{msg} {nome}'
    

# variavel = saudacao()
# print(variavel)



# 2 - Crie uma função que recebe 3 números como parâmetros e exiba a soma entre eles.

def soma(n1, n2, n3):
    return n1 + n2 + n3

somar = soma(8, 2, 14)

if somar:
    print(somar)


























# 3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um percentual (ex. 10%)
# Retorne (return) o valor do primeiro número somado do aumento do percentual do mesmo.

# 4 - Fizz Buzz - Se o parâmetro da função for divisível por 2, retorne fizz, se o parâmetro da função
# for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o número enviado