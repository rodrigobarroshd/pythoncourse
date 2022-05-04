# Create variables for a person's name, age, height and weight OK 

# create variable with current year OK

# get the person's year of birth (based on age and current year) OK

# obtain the person's IMC to 2 decimal places (weight and height of the person)

# display a text with all values on the screen using F-strings (with the braces)



name = ('Rodrigo')
age = (20)
height = (1.73)
weight = (61)

imc = weight /(height ** 2)
current_year = (2022)

print(f'name have {age} years old and {height} height')
print(f'Your year of birth is {(current_year - age)}')
print(f'Your IMC is {imc:.2f}')
