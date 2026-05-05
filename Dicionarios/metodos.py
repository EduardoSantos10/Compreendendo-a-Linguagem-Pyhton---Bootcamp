### METODOS DO DICIONARIO ###

# {}CLEAR: Ele limpa a minha lista
contatos = {
    "eduardo@gmail.com": {"nome": "Eduardo", "telefone": "2222-4444"},
    "santos@gmail.com": {"nome": "Santos", "telefone": "6666-8888"},
}

contatos.clear()
print(contatos)


# {}.COPY: Ele tira uma cópia do meu dicionário
contatos = {
    "eduardo@gmail.com": {"nome": "Eduardo", "telefone": "2222-4444"},
}

copia = contatos.copy()
copia["eduardo@gmail.com"] = {"nome": "Edu"} # No dicionário novo, eu posso mudar dados, sem realizar alteração no original

print(copia)


# {}.FROMKEYS: Quando você quer criar as chaves no seu dicionário
dict.fromkeys(["nome", "telefone"]) # Nesse primeiro caso seria quando você criasse as chaves com o valor none

dict.fromkeys(["nome", "telefone"], "vazio") # Nesse segundo caso é quando você quer criar as chaves com o valor padrão


# {}.GET: Ele pode buscar o valor de uma chave em um dicionario
contatos = {
    "eduardo@gmail.com": {"nome": "Eduardo", "telefone": "2222-4444"},
}

contatos.get("chave") # None
contatos.get("eduardo@gmail.com", {})