# EXEMPLO 01:
carros = ["gol", "celta", "palio"] # Declarei uma lista de variaveis

for carro in carros: # A variavel 'carro' vai percorrer a lista 'carros'
    print(carro) # Vou printar a busca que foi feita na variavel
    
    
# EXEMPLO 02: FUNÇÃO ENUMERATE

carros = ["gol", "celta", "palio"] # Declarei a lista de valores

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}") # Ele vai informar o indice dos valores da lista