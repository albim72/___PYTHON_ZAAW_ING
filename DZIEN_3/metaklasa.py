class MojaMeta(type):
    def __new__(cls, clsnazwa, supercls, attribs):
        print(f'nazwa klasy: {clsnazwa}')
        print(f'klasy dziedziczone: {supercls}')
        print(f'zbiór atrybutów: {attribs}')
        return type.__new__(cls, clsnazwa, supercls, attribs)

class DrugaMeta(type):
    pass


class Zwyczajna:
    pass

class Pierwsza(metaclass=MojaMeta):
    def msg(self,i):
        return f'wiadomość: {i}'

class Specjalna(Zwyczajna):
    pass

class Druga(Pierwsza):
    pass

class Trzecia(Specjalna,Druga):
    pass

z = Zwyczajna()
s = Specjalna()
p = Pierwsza()
