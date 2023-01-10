from oldresistor import OldResistor
from resistor import Resistor
from voltage import VoltageResistance
from bounded import BoundedResistance

print("______________________________________")
print("Klasa OldResistor")

r0 = OldResistor(10.2E2)
print(r0)
print(r0.get_ohms())
r0.set_ohms(9.9E3)
print(r0.get_ohms())

print("______________________________________")
print("Klasa Resistor")

r1 = Resistor(50E3)
r1.ohms = 1.2E2

print(f'układ elektryczny:\noporność: {r1.ohms} om\nnapięcie prądu: {r1.voltage} V'
      f'\nnatężenie prądu: {r1.current} A')

print("______________________________________")
print("Klasa VoltageResistance")

r2 = VoltageResistance(5.4E3)
print(f'natężenie początkowe prądu: {r2.current} A')
r2.voltage = 1.3E2
print(f'napięcie prądu: {r2.voltage} V')
print(f'natężenie prądu: {r2.current} A')

print("______________________________________")
print("Klasa BoundedResistance")
try:
      r3 = BoundedResistance(1E2)
      r3.ohms = 68
      print(f'oporność: {r3.ohms}')
except ValueError as d:
      print(str(d))
except Exception:
      print("wystąpił błąd w kodzie wywołującym")
