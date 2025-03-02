import random

numero_secreto = random.randint(1, 10)
intento = 0

while intento != numero_secreto:
    intento = int(input("Adivina un número del 1 al 10: "))
    if intento < numero_secreto:
        print("Muy bajo ⬇️")
    elif intento > numero_secreto:
        print("Muy alto ⬆️")
    else:
        print("¡Correcto! 🎉")