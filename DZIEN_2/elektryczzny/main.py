from oldresistor import OldResistor
from resistor import Resistor

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
