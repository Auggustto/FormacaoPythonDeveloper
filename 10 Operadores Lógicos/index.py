"""
O que são?
São operadores utilizados em conjunto com os operadores de comparação, para montar uma expressão lógica. Quando um operador de comparação é utilizado, o resultado retornado é um booleano, dessa forma podemos combinar operadores de comparação com os operadores lógicos, exemplo:
op_comparacao + op_logico + op_comparacao… N …

"""
# AND = para ser True tudo tem que ser True
# OR = para ser True apenas um tem que ser True


# Tabela de operadores logicos
print(True and True, "| True")
print(True and False, "| False")
print(True or True, "| True")
print(True or False, "| True")

saldo = 1000
saque = 250
limite = 200
conta_especial = True

expressao = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(expressao)

expressao2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(expressao2)
