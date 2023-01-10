from prostokat import Prostokat
from trojkat import Trojkat

pr = Prostokat(5.5,6.7)
pr2 = Prostokat(4.4,4.4)
tr = Trojkat(4.4,8)

print(f'pole figury {pr.__class__.__name__} -> {pr.policz_pole():.2f} cm2')
print(f'pole figury {pr2.__class__.__name__} -> {pr2.policz_pole():.2f} cm2')
print(f'pole figury {tr.__class__.__name__} -> {tr.policz_pole():.2f} cm2')
