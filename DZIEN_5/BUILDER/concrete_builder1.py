from builder import Builder
from prod1 import  Product1


class ConcreteBuilder1(Builder):

    def __init__(self) -> None:
        self.reset()

    def reset(self):
        self._product = Product1()

    @property
    def product(self) -> Product1:
        product = self._product
        self.reset()
        return product

    def product_part_a(self) -> None:
        self._product.add("PartA1")

    def product_part_b(self) -> None:
        self._product.add("PartB1")

    def product_part_c(self) -> None:
        self._product.add("PartC1")
