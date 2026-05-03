# MÉTODOS 01: Maiúscula, Minúscula e Título
curso = "pYtHon"

print(curso.upper()) # Metodo para deixar a palavra maiúscula

print(curso.lower()) # Metodo para deixar a palavra minúscula

print(curso.title()) # Metodo para transformar a palavra em título

####################################################################

# MÉTODOS 02: Eliminando espaços em branco
faculdade = "    Python  "

print(faculdade.strip()) # Remove os espaços da esquerda e da direita

print(faculdade.lstrip()) # Remove os espaços da esquerda

print(faculdade.rstrip()) # Remove os espaços da direita

####################################################################

# MÉTODOS 03: Junções e centralizações
tecnico = "Python"

print(tecnico.center(10, "#")) # Este método irá centralizar a frase no centro da pronúncia
# O número 10 irá preencher com quantos caractecer você quer na frase

print(".".join(tecnico)) # Através do metodos join, estamos inserindo os pontos finais na fase 'tecnico'
