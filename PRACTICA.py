# ==========================================
# SISTEMA DE TORNEO DE FÚTBOL
# ==========================================

equipos = {}
jugadores_registrados = set()


def registrar_equipo():
    nombre = input("Ingrese el nombre del equipo: ").strip().upper()

    if nombre in equipos:
        print("El equipo ya está registrado.")
    else:
        equipos[nombre] = []
        print("Equipo registrado correctamente.")


def registrar_jugador():
    equipo = input("Ingrese el nombre del equipo al que pertenece el jugador: ").strip().upper()

    if equipo not in equipos:
        print("El equipo no existe. Registre primero el equipo.")
        return

    jugador = input("Ingrese el nombre del jugador: ").strip().upper()

    if jugador in jugadores_registrados:
        print("El jugador ya está registrado.")
    else:
        equipos[equipo].append(jugador)
        jugadores_registrados.add(jugador)
        print("Jugador registrado correctamente en el equipo.")


def mostrar_torneo():
    print("\n=== TORNEO DE FÚTBOL ===")

    if not equipos:
        print("No hay equipos registrados.")
        return

    for equipo, jugadores in equipos.items():
        print(f"\nEquipo: {equipo}")

        if not jugadores:
            print("  Sin jugadores registrados")
        else:
            for j in jugadores:
                print(f"  - {j}")


def menu():
    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Registrar equipo")
        print("2. Registrar jugador")
        print("3. Mostrar torneo")
        print("4. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_equipo()
        elif opcion == "2":
            registrar_jugador()
        elif opcion == "3":
            mostrar_torneo()
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida")


menu()