
""""
1 - Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é
par ou ímpar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro.



2 - Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a
saudação apropriada. Ex Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23



3 - Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva
" Seu nome é curto "; se tiver entre 5 e 6 letras, escreva " Seu nome é normal "; maior que 6 
escreva " Seu nome é muito grande ".



"""""


# 1 

number = int(input('Digite um número inteiro: '))

if number%2 :
    print("Ímpar")
else:
    print("Par")
    



# 2 

nome = input('Qual seu nome? ')
horario = input('Que horas são? ')
horario = int(horario)

if horario >= 0 and horario <= 11:
    print('Boa tarde 0-11')
elif horario >= 12 and horario <= 17:
    print('Boa tarde 12-17')
elif horario >= 18 and horario <= 23:
    print('Boa noite 18-23')




# 3 


user = input('Digite seu usuário: ')
len(user) 

if len(user) <= 2:
    print('Seu nome é muito curto')
elif len(user) >= 4 and len(user) <= 15:
    print('Seu nome foi aceito')
elif len(user) > 15:
    print("Seu nome é muito grande")