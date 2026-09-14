from estudiantes import (
    agregar_estudiante,
    mostrar_estudiantes,
    buscar_estudiante
)
from notas import (
    agregar_nota,
    calcular_promedio,
    estado_estudiante
)

def mostrar_menu():
    print("\n====================================")
    print("    SISTEMA DE GESTIÓN ACADÉMICA    ")
    print("====================================")
    print("1. Registrar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Buscar estudiante")
    print("4. Registrar nota")
    print("5. Consultar promedio")
    print("6. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-6): ")

        if opcion == "1":
            codigo = input("Ingrese el código del estudiante: ")
            nombre = input("Ingrese el nombre del estudiante: ")
            agregar_estudiante(codigo, nombre)
            print("Estudiante registrado exitosamente.")

        elif opcion == "2":
            print("\n--- Lista de Estudiantes ---")
            mostrar_estudiantes()

        elif opcion == "3":
            codigo = input("Ingrese el código a buscar: ")
            estudiante = buscar_estudiante(codigo)
            if estudiante:
                print(f"Encontrado: {estudiante['codigo']} - {estudiante['nombre']}")
            else:
                print("Estudiante no encontrado.")

        elif opcion == "4":
            codigo = input("Ingrese el código del estudiante: ")
            estudiante = buscar_estudiante(codigo)
            if estudiante:
                try:
                    nota = float(input("Ingrese la nota (0 a 5): "))
                    if agregar_nota(estudiante, nota):
                        print("Nota registrada con éxito.")
                    else:
                        print("Nota fuera del rango permitido (0-5).")
                except ValueError:
                    print("Error: Debe ingresar un valor numérico.")
            else:
                print("Estudiante no encontrado.")

        elif opcion == "5":
            codigo = input("Ingrese el código del estudiante: ")
            estudiante = buscar_estudiante(codigo)
            if estudiante:
                prom = calcular_promedio(estudiante)
                est = estado_estudiante(estudiante)
                print(f"Promedio: {prom:.2f} | Estado: {est}")
            else:
                print("Estudiante no encontrado.")

        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()