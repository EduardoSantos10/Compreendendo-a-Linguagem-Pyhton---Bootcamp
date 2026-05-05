# METODO UNION: Pode unificar os valores de dois sets
conjunto_a = {1, 2}
conjunto_b = {3, 4}

print(conjunto_a.union(conjunto_b))


# METODO INTERSECTION: Pontos onde os valores são iguais
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.intersection(conjunto_b))


# METODO DIFFERENCE: Valores que eu tenho em um conjunto e não tenho no outro
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))


# METODO SYMMETRIC_DIFFERENCE: Ele iŕa retornar os valores diferentes do conjunto todo
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.symmetric_difference(conjunto_b))


# METODO ISSUBSET: Ele avalia se um elemento de A pertence a B
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

print(conjunto_a.issubset(conjunto_b))
print(conjunto_b.issubset(conjunto_a))


# METODO ISSUPERSET: Ele avaliar o oposto agora, se os elementos de B pertencem a A
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

print(conjunto_a.issuperset(conjunto_b))
print(conjunto_b.issuperset(conjunto_a))


# METODO ISDISJOINT: Ele avalia se os conjuntos de tocam com os valores
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1 ,0}

print(conjunto_a.isdisjoint(conjunto_b))
print(conjunto_a.isdisjoint(conjunto_c))


# METODO ADD: Posso inserir o valor no conjunto, desde que ele não exista anteriormente
sorteio = {1, 23}

print(sorteio.add(25))
print(sorteio.add(42))
print(sorteio.add(25))


# METODO CLEAR: Ele limpa o seu set
sorteio = {1, 23}

# Sorteio -> {1, 23}
# sorteio.clear()
# sorteio


# METODO COPY
sorteio = {1, 23}

# sorteio -> {1, 23}
# sorteio.copy()
# sorteio -> {1, 23}


# METODO DISCARD: Ele descarta um número do conjunto
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

numeros #{1, 2, 3, 4, 5, 6, 7, 8, 9}
numeros.discard(1)
numeros.discard(45) # Mas não tem 45
numeros # {2, 3, 4, 5, 6, 7, 8, 9, 0}


# METODO POP: Ele elimina parametros em sequencia
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)
print(numeros.pop())
print(numeros.pop())
print(numeros)


# METODO REMOVE: Remove um valor
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)
print(numeros.remove(1))
print(numeros)


# METODO LEN: Ele conta quantos valores tem no conjunto
numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

print(len(numeros))


# METODO IN: Verificar se um elemento está dentro do conjunto
numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

print(1 in numeros)
print(10 in numeros)