from builder import Builder

class Director:
    def __init__(self)->None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self,builder):
        self._builder = builder

    def build_minimal_variable_product(self) -> None:
        self.builder.product_part_a()

    def build_full_variable_product(self) -> None:
        self.builder.product_part_a()
        self.builder.product_part_b()
        self.builder.product_part_c()
