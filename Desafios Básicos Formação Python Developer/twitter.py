"""
DESAFIO
O microblog Twitter é conhecido por limitar as postagens em 140 caracteres. 
Conferir se um texto vai caber em um tuíte é sua tarefa.
"""

T = input("Enter your twitter: \n")

print("TWEET" if len(T) <= 140 else "MUTE")

