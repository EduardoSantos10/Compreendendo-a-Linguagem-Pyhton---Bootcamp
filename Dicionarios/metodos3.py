# {}.SETDEFAULT: Adiciona um valor que não existe no dicionário
contatos = {
    "eduardo@gmail.com": {"nome": "Eduardo", "telefone": "2222-4444"},
}

contatos.setdefault("idade", 23)
print(contatos)


# {}.UPDATE: Ele atualiza o dicionario com chaves que não existem
contatos = {
    "eduardo@gmail.com": {"nome": "Eduardo", "telefone": "2222-4444"},
}

contatos.update({"eduardo@gmail.com": {"nome": "Edu"}})
print(contatos)

contatos.update({"eduardo@gmail.com": {"nome": "Santos", "telefone": "4002-8922"}})
print(contatos)


# {}.VALUES: Retorna todos os valores dos dicionários
info = {
    "dudu@gmail.com": {"nome": "Dudis", "numero": "4444-6666"},
    "silva@gmail.com": {"nome": "Dudu", "numero": "5555-7777"},
}

print(info.values())


# IN: Ele faz uma verificação se uma chave existe ou não em um dicionario
resultado = "dudu@gmail.com" in info
print(resultado)

resultado = "megumi@gmail.com" in info
print(resultado)

resultado = "idade" in info["dudu@gmail.com"]
print(resultado)


# DEL: Ele faz a remoção de valores
info = {
    "dudu@gmail.com": {"nome": "Dudis", "numero": "4444-6666"},
    "silva@gmail.com": {"nome": "Dudu", "numero": "5555-7777"},
}

del info["dudu@gmail.com"]["numero"]
del info["silva@gmail.com"]
print(info)