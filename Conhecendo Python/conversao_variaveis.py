# Convertendo Inteiro p/ Float
preco = 10
print(preco)

# Modos de Conversão Inteiro -> Float
preco = float(preco)
print(preco)

# OU
preco = 10 / 2
print(preco)


###############################################################


# Convertendo Float p/ Inteiro
preco = 10.30
print(preco)

# Modo de conversão Float -> Inteiro
preco = int(preco)
print(preco)

################################################################

# Conversão por Divisão
preco = 10
print(preco)

print(preco / 2)

# Conversão por Divisão Inteira
print(preco // 2) # Eu tenho o valor inteiro da divisão

################################################################


# Convertendo Numérico p/ String
preco = 10.50
idade = 23


# Formula usadas p/ conversão
print(str(preco))

print(str(idade))

# Realizando a concatenação de String e Numérico (Outra forma de conversão)
texto = f"idade {idade} preco {preco}" # O caractere "f" serve para realizar a concatenação da frase com números
print(texto)

################################################################

# Realizando a conversão String p/ Números
preco = "10.50"
idade = "23"

print(float(preco)) # Nesse caso a variavél que era String, passou a ser float

print(int(idade)) # Nesse caso a variavél que era String passou a ser int

################################################################

# Erro de Conversão

# -> Não é possível converter string p/ float