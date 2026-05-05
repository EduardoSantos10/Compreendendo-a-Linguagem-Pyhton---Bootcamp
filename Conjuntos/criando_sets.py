# EXEMPLOS DE SETS 01:
numeros = set([1, 2, 3, 1, 3, 4]) # Nesse caso ele irá eliminar os números que se repetem
print(numeros)

frutas = set("abacaxi") # Nesse caso ele irá eliminar as letras que repetem
print(frutas)

carros = set(("palio", "gol", "celta", "palio")) # Aqui ele irá eliminar as palavras que se repetem
print(carros)


# ACESSANDO OS DADOS:
numeros = {1, 2, 3, 2} # Desse jeito eu não consigo acessar os valores da lista de Python

numeros = list(numeros) # Preciso converter eles em lista

print(numeros[0])


# PERCORRER ESTE SET:
carros = {"gol", "celta", "palio"} # Eu consigo percorrer o set

for carro in carros:
    print(carro)
    
    
# FUNÇÃO ENUMERATE:
carros = {"gol", "celta", "palio"}

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")