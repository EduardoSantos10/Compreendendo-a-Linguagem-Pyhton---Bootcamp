# {}.ITEMS: Retorna os valores das chaves
contatos = {
    "eduardo@gmail.com": {"nome": "Eduardo", "telefone": "2222-4444"},
}

print(contatos.items())


# {}.KEYS: Retorna só as chaves do dicionário
contatos = {
    "eduardo@gmail.com": {"nome": "Eduardo", "telefone": "2222-4444"},
}

print(contatos.keys())


# {}.POP: Remove e sobrescreve um valor padrão
contatos = {
    "eduardo@gmail.com": {"nome": "Eduardo", "telefone": "2222-4444"},
}

resultado = contatos.pop("eduardo@gmail.com")
print(resultado)

resultado = contatos.pop("eduardo@gmail.com", "nao econtrado")
print(resultado)


# {}.POPITEM: Ele vai removendo os itens em sequencia
contatos = {
    "eduardo@gmail.com": {"nome": "Eduardo", "telefone": "2222-4444"},
}

print(contatos.popitem())