import tkinter as tk
from tkinter import messagebox
import random

# Generar un número aleatorio entre 0 y 100
number = random.randint(0, 100)

# Inicializar vidas
lives = 5

# Lista de números primos entre 0 y 100
primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# Diccionario de pistas
diccionario_pistas = {
    1: ["El número está al principio de la secuencia numérica."],
    50: ["El número es justo la mitad de 100."],
    75: ["El número es un cuarto menos de 100."],
    100: ["El número es el máximo en el rango dado."]
}

# Función para obtener una pista
def obtener_pista(numero_seleccionado):
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

# Función para manejar la lógica del juego
def adivinar_numero():
    global lives
    try:
        b = int(entry_numero.get())
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce un número válido.")
        return

    if number == b:
        messagebox.showinfo("¡Felicidades!", f"¡Adivinaste el número! El número era {b}.")
        root.destroy()
    else:
        lives -= 1
        if lives == 0:
            messagebox.showinfo("Fin del Juego", f"Lo siento, has perdido. El número era {number}.")
            root.destroy()
        else:
            pista = tk.messagebox.askyesno("Pista", "¿Quiere una pista?")
            if pista:
                pista_generada = obtener_pista(number)
                messagebox.showinfo("Pista", pista_generada)
            label_vidas.config(text=f"Vidas restantes: {lives}")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Adivinador de Número")

# Etiquetas y campos de entrada
label_instruccion = tk.Label(root, text="Adivina el número entre 0 y 100")
label_instruccion.pack()

entry_numero = tk.Entry(root)
entry_numero.pack()

btn_adivinar = tk.Button(root, text="Adivinar", command=adivinar_numero)
btn_adivinar.pack()

label_vidas = tk.Label(root, text=f"Vidas restantes: {lives}")
label_vidas.pack()

# Iniciar el bucle principal de la interfaz
root.mainloop()

