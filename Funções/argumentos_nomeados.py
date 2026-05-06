### EXEMPLOS ###
def salvar_carro(marca, modelo, ano, placa): # Passado argumentos
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

# Chamando as funções, e sempre respeitando os modelos que foram definidis em argumentos
salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(marca="Fiat", modelo="Palio", ano="1999", placa="ABC-1234") # Essa função pode prevenir erros
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano":1999, "placa": "ABC-1234"})
