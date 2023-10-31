class Foo:
    def __init__(self, x=None):
        self._x = x # _x o que tem _ é um metodo privado e só pode ser acessado pela classe

    """ 
        -> decorator / para retornar um valor é obrigatorio o uso do @property 
        caso contrario retornaria um valor computacional 
        (<bound method Foo.x of <__main__.Foo object at 0x000001A433D234C8>>)
    """
    @property 
    def x(self):
        return self._x or 0

    @x.setter
    def x(self, value):
        self._x += value

    @x.deleter
    def x(self):
        self._x = 0


foo = Foo(10)
print(foo.x)

# del foo.x
# print(foo.x)

# foo.x = 10
# print(foo.x)
