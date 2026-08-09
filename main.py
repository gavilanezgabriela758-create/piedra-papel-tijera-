import random

def mostrar_menu():
    """Muestra las opciones disponibles para el jugador."""
    print("\n" + "="*35)
    print("  JUEGO: PIEDRA, PAPEL O TIJERA")
    print("="*35)
    print("Opciones válidas: piedra, papel, tijera")
    print("Escribe 'salir' para finalizar el juego.\n")

def determinar_ganador(usuario, computadora):
    """
    Aplica estructuras condicionales para evaluar quién gana la ronda.
    Retorna: 'empate', 'usuario' o 'computadora'.
    """
    if usuario == computadora:
        return "empate"
    
    # Reglas de victoria para el usuario
    if (usuario == "piedra" and computadora == "tijera") or \
       (usuario == "papel" and computadora == "piedra") or \
       (usuario == "tijera" and computadora == "papel"):
        return "usuario"
    else:
        return "computadora"

def iniciar_juego():
    """Función principal que controla el bucle del juego y el marcador."""
    opciones = ["piedra", "papel", "tijera"]
    
    # Variables para llevar el marcador de victorias
    puntos_usuario = 0
    puntos_computadora = 0
    empates = 0

    # Estructura repetitiva (bucle principal) para jugar múltiples rondas
    while True:
        mostrar_menu()
        
        # Captura y normalización de la entrada del usuario
        eleccion = input("Tu elección: ").strip().lower()

        # Condicional para finalizar la ejecución del bucle
        if eleccion == "salir":
            print("\n¡Gracias por jugar!")
            break

        # Validación de entrada
        if eleccion not in opciones:
            print("❌ Opción no válida. Inténtalo de nuevo.")
            continue

        # Elección aleatoria de la máquina
        computadora = random.choice(opciones)
        print(f"\n👉 Tú elegiste: {eleccion.capitalize()}")
        print(f"🤖 La computadora eligió: {computadora.capitalize()}")

        # Determinación del resultado de la ronda mediante condicionales
        resultado = determinar_ganador(eleccion, computadora)

        if resultado == "empate":
            print("🤝 ¡Es un empate!")
            empates += 1
        elif resultado == "usuario":
            print("🎉 ¡Ganaste esta ronda!")
            puntos_usuario += 1
        else:
            print("💻 La computadora gana esta ronda.")
            puntos_computadora += 1

        # Muestra del marcador actualizado
        print(f"\n📊 MARCADOR -> Usuario: {puntos_usuario} | Computadora: {puntos_computadora} | Empates: {empates}")

# Punto de entrada del programa
if __name__ == "__main__":
    iniciar_juego()
