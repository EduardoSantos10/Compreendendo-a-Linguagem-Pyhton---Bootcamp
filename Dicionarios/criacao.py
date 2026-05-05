# EXEMPLO DE DECLARAÇÃO DE DICIONARIO:
pessoa = {"nome": "Eduardo", "Idade": 23} # Declaro ele em chaves, e eu defino com chaves e valores

pessoa = dict(nome="Eduardo", idade=23) # Posso declara usando dict

pessoa["telefone"] = "3333-1234" # Nesse caso seria quando eu já tenho um dicionario criado e estou adicionando um novo valor nele

print(pessoa) # Imprimindo os valores

# Dicionario é criado com valores imutavéis, então eles não podem ser criado como lista


### COMO POSSO ACESSAR ESSES DADOS ###
dados = {"nome": "Eduardo", "Idade": 23, "telefone": "3333-1234"}

print(dados["nome"]) # Acessando os dados
print(dados["Idade"])
print(dados["telefone"])



### SUBSCREVENDO DADOS ###
dados["nome"] = "Santos"
dados["Idade"] = 24
dados["telefone"] = "8888-9999"

print(dados)
