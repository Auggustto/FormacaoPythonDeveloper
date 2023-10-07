"""
    Fatiamento de string.
    Fatiamento de strings é uma técnica utilizada para retornar substrings 
    (partes da string original), informando inicio (start), fim (stop)
    e passo (step): [start: stop[, step]].
"""

def fatiamento() -> str:

    nome = "Leonardo Augusto de Aindrade"

    print("Retorna o caracter na posição 1 do índice, no caso a primeira letra: \n", nome[0])
    print("Retorna o caracter na posição 9: \n", nome[:9])
    print("Retorna o caracter na posição 10 até o final: \n", nome[10:])
    print("Retorna o caracter na posição 10 até 16: \n", nome[10:16])
    print("Retorna o caracter na posição 10 até 16 porém pulando 2 em 2: \n", nome[10:16:2])
    print("Retorna uma copia da string inteira: \n", nome[:])
    print("Cria o espelhamento da string de forma invertida: \n", nome[::-1])

fatiamento()