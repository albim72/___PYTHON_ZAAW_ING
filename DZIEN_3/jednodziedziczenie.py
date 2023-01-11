class MultiBases(type):
    def __new__(cls, clsname, bases, attribs):
        if len(bases) > 1:
            raise TypeError("Możliwe jest tylko jednodziedziczenie klas!")
        return super().__new__(cls, clsname, bases, attribs)

class Base(metaclass=MultiBases):
    pass

class A(Base):
    pass

class B(Base):
    pass

class D(B):
    pass

class F:
    pass

class C(F,D):
    pass
