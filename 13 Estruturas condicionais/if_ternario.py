saldo = 200
saque = 200

status = "Sucesso" if saldo >= saque else "Falha"
print(f'O status do pagamento é {status}')