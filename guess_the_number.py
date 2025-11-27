import random

print("¡Bienvenido al juego de adivina el número!")
numero_secreto = random.randint(1, 100)
intentos = 0

while True:
    intento = input("Adivina el número (entre 1 y 100): ")
    intentos += 1
    try:
        intento = int(intento)
    except ValueError:
        print("Por favor, ingresa un número válido.")
        continue

    if intento < numero_secreto:
        print("Demasiado bajo. Intenta de nuevo.")
    elif intento > numero_secreto:
        print("Demasiado alto. Intenta de nuevo.")
    else:
        print(f"¡Correcto! El número era {numero_secreto}. Lo lograste en {intentos} intentos.")
        break