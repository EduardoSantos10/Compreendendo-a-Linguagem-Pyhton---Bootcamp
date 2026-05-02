# Exemplo 01:
# range(stop) -> range object
# range(start, stop[, step]) -> range object
# list(range(4))


# Exemplo 02:
for numero in range(0, 11): # range vai percorrer e imprimir uma lista com 10 numeros
    print(numero, end=" ")
    
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

print()
    

# Exemplo 03 com a tabuada do 5:
for numero in range(0, 51, 5):
    print(numero, end=" ")
    
print()

# 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50