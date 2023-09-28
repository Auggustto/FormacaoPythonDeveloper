### String 1 ###

def EditandoFormatos() -> str:

    nome = "Leonardo"

    print("Deixando tudo maiusculo:", nome.upper())
    print("Deixando tudo minusculo:", nome.lower())
    print("Usando o metodo Title, onde somente a primeira letra fica maiuscula:", nome.title())

# EditandoFormatos()

def DeletandoEspacos() -> str:

    nome = "   Leonardo     "

    print("Removendo os espaços do lado direito:", nome.rstrip() + ".")
    print("Removendo os espaços do lado esquerdo:", nome.lstrip() + ".")
    print("Removendo os espaços :", nome.strip() + ".")

# DeletandoEspacos()

def center() -> str:

    nome = "python"

    print("Centralizando:", nome.center(14))
    print("Concatenando e centralizando:", nome.center(14, "#"))
    print("Usando o metodo Join para dividir a string com um caracter:", "-".join(nome))

center()