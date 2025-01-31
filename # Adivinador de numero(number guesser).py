# Adivinador de numero(number guesser)

import random

# Generar un número aleatorio entre 0 y 100
number = random.randint(0, 100)
#print(number)  # Esto puedes eliminarlo si no quieres que se muestre el número

# Inicializar vidas
lives = 5
print("Adivina el número")

# Lista de números primos entre 0 y 100
primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# Función para obtener una pista
def obtener_pista(diccionario_pistas, numero_seleccionado):
    pistas = diccionario_pistas.get(numero_seleccionado, [
        f"El número es par." if numero_seleccionado % 2 == 0 else "El número es impar.",
        f"El número es mayor que {numero_seleccionado - random.randint(1, 20)}.",
        f"El número es menor que {numero_seleccionado + random.randint(1, 20)}.",
        f"La suma de los dígitos del número es {sum(map(int, str(numero_seleccionado)))}.",
        f"El número tiene {len(str(numero_seleccionado))} dígito(s).",
        f"El primer dígito del número es {str(numero_seleccionado)[0]}."
    ])
    if numero_seleccionado in primos:
        pistas.append("Es un número primo.")
    return random.choice(pistas)

# Diccionario de pistas (puedes personalizarlo)
diccionario_pistas = {
    1: ["El número está al principio de la secuencia numérica."],
    50: ["El número es justo la mitad de 100."],
    75: ["El número es un cuarto menos de 100."],
    100: ["El número es el máximo en el rango dado."]
}

# Bucle principal del juego
while lives > 0:
    print("¿Cuál es el número?")
    try:
        b = int(input())
    except ValueError:
        print("Por favor, introduce un número válido.")
        continue
    
    if number == b:
        print(f"¡Felicidades adivinaste el número! El número era {b}.")
        break
    else:
        lives -= 1
        if lives == 0:
            print(f"Lo siento, has perdido. El número era {number}.")
            break

        pista = input("¿Quiere una pista? SI o NO").strip().lower()
        if pista in ("si"):
            pista_generada = obtener_pista(diccionario_pistas, number)
            print(f"Pista: {pista_generada}")
        elif pista in ("no"):
            print("Está bien, ¡buena suerte!")
        
    print(f"Te quedan {lives} vidas.")

