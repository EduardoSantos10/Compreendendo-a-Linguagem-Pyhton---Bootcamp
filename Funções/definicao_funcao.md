### O que são funções ###

- É um bloco de código identificado por um nome e pode recever uma lista de parâmetros, esses parâmetros podem ou não ter valores padrôes.

- Usar funções torna o código mais legivél e possibilita o reaproveitamento de código.

- Programar baseado em funções, é o mesmo qye dizer que estamos programando de maneira estruturada.


### Retornando Valores ###

- Para retornar um valor, utilizamos a palavra reservada 'return'.

- Toda função Python retorna 'None' por padrão.

- Diferente de outras linguagens de programação, em Python uma função pode retornar mais de um valor.


### Argumentos Nomeados ###

- Funções também podem ser chamadas usando argumentos nomeados da forma chave=valor.


### Args e Kwargs ###

- Podemos combinar parâmetros obrigatórios com args e kwargs.

- Quando esse são definidos ()*args e **kwargs), o método recebe os valores como tupla e dicionário respectivamente.


### Parâmetros Especiais ###

- Argumentos pode ser passados para uma função Python tanto por posição quanto explicitamente pelo nome.

- Para uma legibilidade e desempenho, faz sentido restringir a maneira pelo qual argumentos possam ser passados, assim um desenvolvedor precisa antes apenas olhar para a definição da função para determinar se os itens são passados por posição e nome, ou por nome.


### Objetos de Primeira Classe ###

- Em Python tudo é objeto, dessa forma funções também são objetos oque as tornam objetos de primeira classe.

- Com isso podemos atribuir funções a variavéis, passá-las como parâmetro para funções, usá-las como valores de estruturas de dados (listas, tuplas, dicionários, etc) e usar como valor de retorno para uma função (closures).


### Escopo Local e Escopo Global ###

- Python trabalha com o escopo local e global, dentro do bloco da função o escopo é local.

- Portanto alterações ali feitas em objetos imutáveis serão perdidas quando o método terminar de ser executado.

- Para usar objetos globais utilizamos a palavra-chave global, que informa ao interpretador que a variável que está sendo manipulada no escopo local é global.

- Essa não é uma boa prática e deve ser evitada.