import math
radio = float(input("Introduce el radio de la circunferencia: "))

circunferencia = 2 * math.pi * radio
print(f"La longitud de la circunferencia es: {round(circunferencia, 2)}cm")

area = math.pi * (radio ** 2)
print(f"El area del circulo es: {round(area, 2)}cm2")