curso = "Curso de Python"
frutas = ["limao", "uva", "laranja"]
saques = [1500, 100]

# Iremos utilizar operadores associativos p/ verificar se os objetos estão nas listas.

pergunta1 = "Python" in curso # Nesse caso, "Python" está presente no curso
print(pergunta1)

pergunta2 = "maca" not in frutas # "Maçã" não está presente na lista de frutas
print(pergunta2)

pergunta3 = 200 in saques # "200" não está presente na lista de saques
print(pergunta3)