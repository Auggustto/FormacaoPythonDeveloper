"""
Em Python temos 3 formas de interpolar variáveis em strings, 
a primeira é usando o sinal %, a segunda é utilizando o método 
format e a última é utilizando f strings.
A primeira forma não é atualmente recomendada e seu uso em Python 3 é raro, 
por esse motivo iremos focar nas 2 últimas.

"""

def OldStyle() -> str:
    ### Usando Old Style de % OBS: Esse metodo não e utilizado mais.###

    nome = "Leonardo"
    idade = 25
    profissao = "Progamador"
    linguagem = "Python"

    print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))



def UsandoFormat() -> str:

    ### O metodo format é o mais utilizado atualmente. ###

    nome = "Leonardo"
    idade = 25
    profissao = "Progamador"
    linguagem = "Python"

    pessoas = \
    {
        "nome": "Leonardo",
        "idade": 25,
        "profissao":"Programador",
        "linguagem": "Python"
    }
    
    # O metodo abaixo não e muito recomendados devido a complexibilidade que pode chegar.
    print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))

    # O metodo mais utilizado e limpo é numerando as posições.
    print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}.".format(linguagem, profissao, idade, nome))

    # Outro metodo bastante utilizado é o de informar o nome da vareavel
    print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

    # Usando o metodo kwargs 
    print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(**pessoas)) # Usando kwargs

    # Usando F-string
    print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")



def FormatarStringFstring() -> str:

    PI = 3.14159

    print(f"Valor de PI: {PI:.2f}")
    
    # Insere 10 espaços em branco na frente 
    print(f"Valor de PI: {PI:10.2f}")



    