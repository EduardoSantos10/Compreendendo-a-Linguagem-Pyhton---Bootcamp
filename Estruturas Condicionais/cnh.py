MAIOR_IDADE = 18
IDADE_ESPECIAL = 16

idade = int(input("Informe a sua idade: "))

if idade >= MAIOR_IDADE:
    print("Você tem autorização para dirigir!")
if idade < MAIOR_IDADE:
    print("Você não tem autorização para dirigir!")
    
    
################################################################################


idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Você tem autorização para dirigir!")
else:
    print("Você não pode dirigir!")
    

################################################################################

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Você pode tirar a sua CNH e pode dirigir!")
elif idade == IDADE_ESPECIAL:
    print("Você pode tirar a sua CNH, mas ainda não pode dirigir!")
else:
    print("Você não tem autorização para dirigir!")
