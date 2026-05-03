# FILTRO VERSÃO 01:
numeros = [1, 30, 21, 2, 9, 65, 34] # Declaro uma lista com valores
pares = [] # Declaro uma lista para armazenar valores pares

for numero in numeros: # Declaro uma variavel para percorrer a minha lista
    if numero % 2 == 0: # Coloco uma condição para verificar se ele é par
        pares.append(numero) # Função para mostrar os números pares
        

###############################################################################

# FILTRO VERSÃO 02:
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]


###############################################################################

# MODIFICANDO VALORES VERSÃO 01:
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)
    
###############################################################################

# MODIFICANDO VALORES VERSÃO 02:
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero ** 2 for numero in numeros]