## Operador E
saldo = 1000
saque = 200
limite = 100

r = saldo >= saque and saque <= limite # Para o op "E" ser TRUE, todas a comparações precisam ser verdadeiras
print(r) # Demonstração

# verdadeiro E verdadeiro -> TRUE
# verdadeiro E falso -> FALSE

########################################################################################################################

## Operador OU

r = saldo >= saque or saque <= limite # Para o op "OU" ser TRUE, basta apenas que uma comparação seja verdadeira
print(r)

# verdadeiro OU falsa -> TRUE
# falsa OU falsa -> FALSE

########################################################################################################################

## Operador Negação

contatos_emergencia = []

not 1000 > 1500 # Ele está comparando que 1000 é maior que 1500, é falsa, porém, devido a negação, será TRUE

not contatos_emergencia # Como possui uma lista vazia, sem elementos, será TRUE

not "saque 1500" # Como possui valor e está dentro da string, será FALSE

not "" # Não possui valor dentro da string, é TRUE

########################################################################################################################

saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque) # Exemplo executando uma simulação de sistema de conta bancária
print(exp)