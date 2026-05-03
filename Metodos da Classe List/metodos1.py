# METODO 01: APPEND
lista = []

lista.append(1) # Estou adicionando um numero
lista.append("Eduardo") # Adicionando uma string
lista.append([40, 20, 60]) # Adicionando uma lista de valores

print(lista)


# METODO 02: CLEAR
sequencia = [2, "Santos", [1, 2, 3]] # Estou atribuindo uma lista de valores na minha variavel

sequencia.clear() # Estou limpando a variavel com o metodo 'clear()'

print(sequencia) # Agora irei printar uma variavel vazia


# METODO 03: COPY
marcas = [1, "Adidas", [50, 70, 90]] # Declarei a minha lista de valores

l2 = marcas.copy() # EStou fazendo a copia da lista 'marcas' para 'l2'

print(marcas)

print(id(l2), id(marcas)) # Irei mostrar o id de cada listae ambos mostrara que são diferentes

l2[0] = 6 # Realizei uma alteração de parametro

print(l2)
print(marcas)


# METODO 04: COUNT
cores = ["azul", "verde", "lilas", "prata", "azul", "azul", "verde", "lilas", "prata", "prata"]

cores.count("azul") # Conta quantas vezes aparece na lista
cores.count("verde")
cores.count("lilas")
cores.count("prata")

print(cores.count("azul"))
print(cores.count("verde"))
print(cores.count("lilas"))
print(cores.count("prata"))


# METODO 05: EXTEND
linguagens = ["python", "js", "c"] # Declarei uma lista com valores

print(linguagens) # Imprimo está lista

linguagens.extend(["java", "csharp"]) # Adicionei valores novos a lista

print(linguagens)


# METODO 06: INDEX
tenis = ["tesla", "suede", "air max", "dunk low", "campus"] # Declarei uma lista de valores

print(tenis.index("air max")) # Quero saber o index deste valor
print(tenis.index("campus"))


# METODO 07: POP
techs = ["google", "amazon", "apple", "ms", "adobe"] # Declarei uma lista de valores

print(techs.pop()) # Imprimi os valores de acordo com o ultimo que foi colocado, de trás para frente
print(techs.pop())
print(techs.pop())
print(techs.pop())
print(techs.pop(0)) # Aqui ele muda a sequencia, ele imprimi o valor de acordo com o parametro passado


# METODO 08: REMOVE
times = ["sccp", "spo", "pal", "san", "fla"] # Declarei uma lista de valores

times.remove("sccp") # Remove um valor da lista

print(times)


# METODO 09: REVERSE
techs = ["google", "amazon", "apple", "ms", "adobe"]

techs.reverse() # Ele inverte a ordem da lista

print(techs)


# METODO 10: SORT
techs = ["google", "amazon", "apple", "ms", "adobe"]
techs.sort() # Ele organiza por ordem alfabética
print(techs)

techs.sort(reverse=True) # Inverte a ordem alfabética, do último ao primeiro
print(techs)

techs.sort(key=lambda x: len(x)) # Ele vai ordenar por ordem do tamanho das palavras
print(techs)

techs.sort(key=lambda x: len(x), reverse=True) # Agora ele inverte o ordem do maior para o menor
print(techs)


# METODO 11: LEN
techs = ["google", "amazon", "apple", "ms", "adobe"]

print(len(techs)) # Ele vai imprimir quantos valores tem a lista


# METODO 12: SORTED
techs = ["google", "amazon", "apple", "ms", "adobe"]

sorted(techs, key=lambda x: len(x)) # Ele ordenar por ordem de tamanho das pronúncias
print(techs)

sorted(techs, key=lambda x: len(x), reverse=True) # Ele inverte a ordem
