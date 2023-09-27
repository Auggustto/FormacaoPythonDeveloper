import sys

# opcao = int(input("Informe uma opção: \n [1] Sacar \n [2] Extrato:"))

# if opcao == 1:
#     valor = float(input("Informe a quantia para saque:"))

# elif opcao == 2:
#     print("Carregando extrato..")

# else:
#     sys.exit("Opção invalida!")

maior_idade = 18

idade = int(input("Informe a sua idade:"))

if idade >= 18:
    print('Você tem mais de {} anos, pode dirigir'.format(maior_idade))
else:
    print('Você não é maior de {}, portanto você não pode dirigir.'.format(maior_idade))
