# Exemplo com IF

saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando Saque")
    
if saldo < saque:
    print("Saldo Insuficiente")