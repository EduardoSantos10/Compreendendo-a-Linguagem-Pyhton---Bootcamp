# Exemplo 01:
texto = input("Informe um texto: ")
VOGAIS = 'AEIOU'

for letra in texto: # Vou percorrer letra a letra do que foi atribuido em texto
    if letra.upper() in VOGAIS: # UPPER = Transforma em maiusculo | Depois vou verificar se as letras estão nas vogais = AEIOU
        print(letra, end="") # Aqui irei printar as letras que estão em vogais
        
print() # Quebra de linha



# Exemplo 02 com ELSE:

texto = input("Informe um texto: ")
VOGAIS = 'AEIOU'

for letra in texto: # Vou percorrer letra a letra do que foi atribuido em texto
    if letra.upper() in VOGAIS: # UPPER = Transforma em maiusculo | Depois vou verificar se as letras estão nas vogais = AEIOU
        print(letra, end="") # Aqui irei printar as letras que estão em vogais
else:   
    print() # Quebra de linha
    print("Executa no final do laço")
