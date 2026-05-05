            ### DICIONARIOS ANINHADOS ###
            
# Podem armazenar qualquer tipo de objeto Python como valor, desde que a chave para esse valor seja imnutavél.

# EXEMPLO DE DECLARAÇÃO DE DICIONARIOS ANINHADOS:
contatos = {
    "eduardo@gmail.com": {"nome": "Eduardo", "telefone": "2222-4444"},
    "santos@gmail.com": {"nome": "Santos", "telefone": "6666-8888"},
}

print(contatos["eduardo@gmail.com"]["telefone"]) # Acessando o dado telefone

# Basta colocar entre colchetes a primeira chave e depois digitar o dado que eu quero acessar


            ### ITERAR DICIONÁRIOS ###
            
# A forma mais comum para percorrer os dados de um dicionário
# é utilizando o comando 'for'

for chave in contatos:
    print(chave, contatos[chave])
    
for chave, valor in contatos.items():
    print(chave, valor)