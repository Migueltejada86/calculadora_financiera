from main import interes_simple, interes_compuesto, cuota_prestamo, valor_futuro_aportes

def leer_float(mensaje):
    while True:
        valor = input(mensaje)
        try:
            return float(valor)
        except ValueError:
            print("⚠️ Valor inválido. Ingresá un número válido (ej: 1000 o 0.05).")

def leer_int(mensaje):
    while True:
        valor = input(mensaje)
        try:
            return int(valor)
        except ValueError:
            print("⚠️ Valor inválido. Ingresá un número entero válido.")

def menu():
    print("=== Calculadora Financiera ===")
    print("1. Interés Simple")
    print("2. Interés Compuesto")
    print("3. Cuota de Préstamo")
    print("4. Valor Futuro con Aportes")
    print("0. Salir")

while True:
    menu()
    opcion = input("Elegí una opción (0-4): ")

    if opcion == "0":
        print("¡Hasta luego!")
        break

    if opcion not in ["1", "2", "3", "4"]:
        print("⚠️ Opción inválida. Volvé a intentar.\n")
        continue

    capital = leer_float("Ingresá el capital / monto / aporte: ")
    tasa = leer_float("Ingresá la tasa (ej: 0.05 para 5%): ")
    tiempo = leer_int("Ingresá el tiempo (meses o años según el caso): ")

    if opcion == "1":
        resultado = interes_simple(capital, tasa, tiempo)
    elif opcion == "2":
        resultado = interes_compuesto(capital, tasa, tiempo)
    elif opcion == "3":
        resultado = cuota_prestamo(capital, tasa, tiempo)
    elif opcion == "4":
        resultado = valor_futuro_aportes(capital, tasa, tiempo)

    print(f"\n✅ Resultado: {round(resultado, 2)}\n")
    input("Presioná Enter para continuar...\n")
