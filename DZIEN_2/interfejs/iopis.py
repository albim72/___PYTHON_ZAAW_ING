from abc import ABCMeta, abstractmethod

class IOpis(metaclass=ABCMeta):
    @abstractmethod
    def info(self,id,wpis):
        raise NotImplementedError(f"obowiązkowo zaimplementuj metodę info")
