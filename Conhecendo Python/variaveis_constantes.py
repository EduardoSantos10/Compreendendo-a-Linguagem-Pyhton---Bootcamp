# Exemplo de Variavéis, com troca de valores -> Quando os valores são mutavéis
idade = 16 # antes era 23

nome = 'Deborah' # antes era Eduardo

print(f'Meu nome é {nome} e tenho {idade} de idade.')

nome1, idade1 = 'Eduardo', 23 #Pode definir os valores na mesma linha

print(nome1, idade1) # Pode printar variaveis juntas em Ṕython


# Use sempre nomes sugestivos
saque_limite_diario = 1000 # Use sempre o padrão snake case (_ underline)

salario_mensal = 1500



# Exemplos para utlização de constantes -> Quando os valores são imutavéis
# Constantes também serve snake case
ESTADOS_BRASILEIROS = [
    'SP',
    'MG',
    'RJ',
]

print(ESTADOS_BRASILEIROS)

AMOUNT = 30.2

DEBUG = True

ABS_PATH = '/home/'