### EXEMPLO ###
def somar(a, b): # Função para realizar uma soma
    return a + b

def exibir_resultado(a, b, funcao): # Função para exibir um resultado
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")
    
exibir_resultado(10, 10, somar) # O resultado da operação
