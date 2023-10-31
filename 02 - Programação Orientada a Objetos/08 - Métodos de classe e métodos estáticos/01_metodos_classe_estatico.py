class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    """
        @classmethod -> transforma em um metodo de classe.
        Por convenção o self é alterado para cls.
        
        Ao printar o cls do metodo ele retorna o nome da classe (Pessoa), então com isso
        não precisamos passar o nome da classe no return e sim cls.
    """
    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade =  2023 - ano
        return cls(nome, idade)

    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18


p = Pessoa.criar_de_data_nascimento(1998, 3, 18, "Leonardo")
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(p.idade))
# print(Pessoa.e_maior_idade(8))
