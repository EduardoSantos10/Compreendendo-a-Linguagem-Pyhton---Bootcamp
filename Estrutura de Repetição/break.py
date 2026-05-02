while True:
    numero = int(input("Informe um número: "))
    
    if numero == 10:
        break # Para o código no momento que o programa for verdadeiro
    
    print(numero)
    
    

for numero in range(100):
    if numero == 50:
        break
        
    print(numero, end=" ")