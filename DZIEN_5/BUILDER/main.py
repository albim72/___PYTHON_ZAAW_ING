from builder import Builder
from director import Director
from conrete_builder1 import ConcreteBuilder1

director = Director()
builder = ConcreteBuilder1()
director.builder = builder

print("Produkt podstawowy")
director.build_minimal_variable_product()
builder.product.list_parts()
print("\n")

print("Produkt pełny")
director.build_full_variable_product()
builder.product.list_parts()
print("\n")


print("Produkt użytkownika")
builder.product_part_a()
builder.product_part_c()
builder.product.list_parts()
print("\n")
