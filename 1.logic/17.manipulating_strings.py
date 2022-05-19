# Manipulando strings - Aula 6

# Strings indices
# Fatiamento de strings [inicio:fim:passo]
# Funções built-in len, abs, type, print, etc...

# Essas funções podem ser usadas diretamente em cada tipo.



# positivos      [012345678]
texto          = "Python s2"
# negativos     -[987654321]
print(texto[2])  # Acessa o indice 2 (letra t da string Python s2)
print(texto[-2]) # Acessa o indice 2 negativo (letra s da string Python s2)

novo_texto = texto[2:6] # Acessa o indice 2 até o 6
print(novo_texto)