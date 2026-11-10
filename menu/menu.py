from ejercicios.ejercicio1_boletos import (
    Boleto,
    BoletoEstudiante,
    BoletoCortesia,
    BoletoTerceraEdad
)

from ejercicios.ejercicio2_estacionamiento import (
    Estancia,
    EstanciaPension,
    EstanciaNocturna
)


def ejecutar_boletos():
    print("\nEJERCICIO 1. BOLETOS DE CINE\n")

    boletos = [
        Boleto("Andrea", "Sala 2, 18:00"),
        BoletoEstudiante("Bruno", "Sala 2, 18:00"),
        BoletoCortesia("Carla", "Sala 5, 20:30"),
        BoletoTerceraEdad("Diana", "Sala 1, 16:00")
    ]

    for boleto in boletos:
        print(boleto.ticket())


def ejecutar_estacionamiento():
    print("\nEJERCICIO 2. ESTACIONAMIENTO\n")

    estancias = [
        Estancia("ABC-123", 3),
        EstanciaPension("XYZ-789"),
        EstanciaNocturna("JKL-456", 5)
    ]

    for estancia in estancias:
        print(estancia.ticket())


def mostrar_menu():
    print("\nPRÁCTICA DE HERENCIA")
    print("1. Boletos de cine")
    print("2. Estacionamiento")
    print("0. Salir")


def menu():
    opcion = ""

    while opcion != "0":
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ejecutar_boletos()
        elif opcion == "2":
            ejecutar_estacionamiento()
        elif opcion != "0":
            print("Opción no válida.")