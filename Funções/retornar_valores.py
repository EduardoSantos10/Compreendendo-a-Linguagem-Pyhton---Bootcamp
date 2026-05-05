### EXEMPLOS ###
def calcular_total(numeros): # Abri a função e passei o argumento número
    return sum(numeros) # Nesse caso, a operação será uma soma


def retornar_antecessor_e_sucessor(numero):
    antecessor = numero - 1 # Aqui ele realiza uma subtração com o numero em parâmetro
    sucessor = numero + 1 # Aqui ele realiza uma soma com o numero em parâmetro
    
    return antecessor, sucessor # Aqui eu passei o que eu quero como retorno


print(calcular_total([10, 20, 34]))
print(retornar_antecessor_e_sucessor(10))