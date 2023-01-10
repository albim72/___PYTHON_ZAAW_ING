from prostokat import Prostokat
from trojkat import Trojkat

pr = Prostokat(5.5,6.7)
tr = Trojkat(4.4,8)

print(f'pole figury {pr.__class__.__name__} -> {pr.policz_pole():.2f} cm2')
print(f'pole figury {tr.__class__.__name__} -> {tr.policz_pole():.2f} cm2')
