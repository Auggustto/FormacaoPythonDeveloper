"""
    Trabalhando com listas 

"""
letras = list("python")
print(letras)

# Acessando valores
frutas = ["laranja", "maça", "uva"]
print(frutas[1]) # Maça

# Indices negativos
print(frutas[-1]) # uva

# Listas aninhadas
matriz = [
    [1,"a",3],
    ["b",5,0],
    [8,7,"t"]
]

# Acessando o primeiro indice da lista
print(matriz[1])

"""
    Acessando o valor da lista dentro da lista
    Para isso devemos informar a posição da lista e a 
    posção do elemento dentro da outra lista.
"""
print(matriz[0][1]) # -> 1

# Acessando atravez dos indices negativos
print(matriz[0][-1]) # -> 3
print(matriz[-1][-1]) # -> t

# Fatiamentos 
