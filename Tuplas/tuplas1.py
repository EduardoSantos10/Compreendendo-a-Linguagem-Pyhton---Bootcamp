# EXEMPLO DE CRIAÇÃO DE TUPLAS
frutas = ("laranja", "pera", "uva",) # Ao criar uma tupla, coloque uma vírgula no final, para interpretar corretamente

letras = tuple("python") # Tuplas também utilizam parenteses

numeros = tuple([1, 2, 3, 4,])

pais = ("Brasil",)


# COMO ACESSAR UMA TUPLA DIRETAMENTE
frutas = ("maçã", "laranja", "uva", "pera",)

print(frutas[0])
print(frutas[2])


# COMO ACESSAR O INDICE NEGATIVO
frutas = ("maçã", "laranja", "uva", "pera",)

print(frutas[-1])
print(frutas[-2])


# TUPLAS MATRIZES
matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
) # Matriz de tuplas

print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])

# FATIAMENTO

# -> Segue a mesma ideia, porém ele utiliza patenteses