# O que São 
# São operadores utilizados para verificar se um objeto está presente em uma sequência .

curso = "Curso de Python"
frutas = ["laranja", "uva", "limão"]
saques = [1500, 100]

v1 = "Python" in curso 
print(f'A palavra python esta na frase {v1}')

v2 = "Maça" in frutas
print(f'O Maçã existe nesta lista {v2}')

v3 = 200 in saques
print(f'O valor 200 esta dentro da lista? {v3}')