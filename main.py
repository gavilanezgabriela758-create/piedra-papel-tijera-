import random

def jugar():
    opciones = ["piedra", "papel", "tijera"]
    
    print("--- ¡Bienvenido a Piedra, Papel o Tijera! ---")
    
    usuario = input("Elige piedra, papel o tijera: ").lower().strip()
    
    if usuario not in opciones:
        print("Opción no válida. Inténtalo de nuevo.")
        return

    computadora = random.choice(opciones)
    print(f"\nLa computadora eligió: {computadora}")
    print(f"Tú elegiste: {usuario}\n")

    if usuario == computadora:
        print("¡Es un empate!")
    elif (usuario == "piedra" and computadora == "tijera") or \
         (usuario == "papel" and computadora == "piedra") or \
         (usuario == "tijera" and computadora == "papel"):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")

if __name__ == "__main__":
    jugar()
