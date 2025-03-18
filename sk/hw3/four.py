import math

cath_1 = 9
cath_2 = 23

hypotenuse = round(math.sqrt((cath_1 ** 2) + (cath_2 ** 2)), 2)
square = (cath_1 * cath_2) / 2

print(f"Гипотенуза: {hypotenuse}")
print(f"Площадь: {square}")
