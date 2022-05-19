# While em Python 

# utilizado para realizar ações enquanto uma 
# condição for verdadeira.


# while True:  # Loop infinito
#     nome = input('Qual seu nome? ')
#     print(f'Olá {nome} !')

# print('Não será executada.')
    
    
# x = int(input('coloque um numerro'))  # loop até chegar no número 100
# while x <= 100:
#     print(x)
#     x = x + 1
        
# print('Acabou...')



# x = 0 # Coluna
# while x < 10:
#     y = 0 # linha
    
#     while y < 5:
#         print(f'({x}, {y})')
#         y += 1
        
#     x += 1 # x = x + 1
    
# print( 'Acabou!' )



while True:
    print()
    num1 = input("Digite um número: ")
    num2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')
    
    if not num1.isnumeric() or not num2.isnumeric():
        print('Você precisa digitar um número idiota.')
        continue        
    
    num1 = int(num1)
    num2 = int(num2)
    # + - / *
    if operador == '+':
        print(num1 + num2)
    elif operador == '-':
        print(num1 - num2)
    elif operador == '/':
        print(num1 / num2)
    elif operador == '*':
        print(num1 * num2)
    else:
        print('Não existe resultado...')