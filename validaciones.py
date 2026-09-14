def validar_nombre(nombre):
    if not nombre.strip():
        return False
    return True

def validar_nota(nota):
    return 0 <= nota <= 5

def validar_codigo(codigo):
    return codigo.isdigit()

from validaciones import validar_nota

print(validar_nota(4.5))
print(validar_nota(7))

try:
    nota = float(input("Digite la nota: "))

    if nota < 0 or nota > 5:
        print("La nota debe estar entre 0 y 5.")
    else:
        print("Nota válida.")

except ValueError:
    print("Error: debe ingresar un número.")