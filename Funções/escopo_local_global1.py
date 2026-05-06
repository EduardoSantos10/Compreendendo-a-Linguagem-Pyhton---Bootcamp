### EXEMPLO DE ESCOPO GLOBAL ###
salario = 2000 # Variavél declarada em escopo global

def salario_bonus(bonus):
    global salario # Uso da palavra reservada global
    salario += bonus
    return salario

salario_com_bonus = salario_bonus(500)
print(salario_com_bonus)