# IF ELIF ELSE

# and, or, not
# in, not in

# (True    and    False) = False
# comparacao1 and comparacao2

name = input('Whats your name? ')
age = input('Whats your age? ')

age = int(age)

# Limite para pegarr empréstimo

age_more = 20 # So much young
age_less = 30 # So much old

if age >= age_less and age <= age_more:
    print(f'{name} pode pegar o empréstimo.')
else:
    print(f'{name} não pdoe pegar o empréstimo. ')