import math

a = float(input("Cateto a: "))
b = float(input("Cateto b: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"La hipotenusa del triangulo mide: {round(c, 2)} cm")