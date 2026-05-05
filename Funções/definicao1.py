### EXEMPLOS ###
def exibir_mensagem(): # Defini uma função que irá exibir uma mensagem, e os dois pontos eu estou abrindo a minha função
    print("Olá mundo!")
    

def exibir_mensagem_2(nome): # Nesse caso, passei um argumento
    print(f"Seja bem vindo {nome}!")
    

def exibir_mensagem_3(nome="Anonimo"): # Se eu não passar um valor como argumento quando está repetido, ele tende a dar erro
    print(f"Seja bem vindo {nome}!")
    
    
# Chamando essas funções
exibir_mensagem()
exibir_mensagem_2(nome="Eduardo") # Aqui eu posso passar o valor do argumento
exibir_mensagem_3()
exibir_mensagem_3(nome="Santos")