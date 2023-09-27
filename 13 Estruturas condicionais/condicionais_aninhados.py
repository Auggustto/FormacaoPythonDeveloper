conta_normal = False
conta_universitaria = True

saldo = 2000
cheque_especial = 450
saque = 2500

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Não foi possivel realizar o saque, saldo insuficiente.")
        
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")

# elif conta_universitaria:
# 	if saldo >= saque:
# 		print("Saque realizado com sucesso!")
# else:
# 	print("Saldo insuficiente!")
