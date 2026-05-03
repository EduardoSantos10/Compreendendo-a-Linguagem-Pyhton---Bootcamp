# OLD STYLE %
nome = "Eduardo"
idade = 23
profissao = "Programador"
linguagem = "Python"

print("Olá, meu nome é %s e tenho %d anos, atualmente eu trabalho como %s com enfase na linguagem %s." % (nome, idade, profissao, linguagem))

# %s -> Para formatos em String
# %d -> Para números inteiros
# %f -> Para pontos flutuantes


# Metodo Format
print("Olá, meu nome é {} e tenho {} anos, atualmente eu trabalho como {} com enfase na linguagem {}.".format(nome, idade, profissao, linguagem))

# {}.format -> Com este metodo pode-se inserir strings na pronúncia.
# {} -> pode entrar no lugar das variaveis no meio do texto.


# Método f'string'
print(f"Olá, meu nome é {nome} e tenho {idade} anos, atualmente trabalho como {profissao} com ensafe na linguagem {linguagem}.")
# Com o método f'string' -> eu posso colocar a var entre colchetes {nome} e iniciar a frase com f"Ola meu nome é".


# Formatar strings com f-string e numeros grandes
PI = 3.14159

print(f"Valor de PI: {PI:.2f}") # Imprimir mensagem com número reduzido

print(f"Valor de PI: {PI:10.2f}") # Imprimir mensagem com 10 espaços
