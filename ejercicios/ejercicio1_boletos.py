"""
EJERCICIO 1. BOLETOS DE CINE

Boleto:
- Tiene cliente, función y precio base de $90.
- Calcula su precio.
- Genera un ticket con el formato:
  Cliente - Función: $precio

BoletoEstudiante:
- Hereda de Boleto.
- Tiene 30% de descuento.

BoletoCortesia:
- Hereda de Boleto.
- Siempre cuesta $0.

BoletoTerceraEdad:
- Tiene 50% de descuento.
"""


class Boleto:
    def __init__(self, cliente, funcion):
        self.cliente = cliente
        self.funcion = funcion
        self.precio_base = 90

    def calcular_precio(self):
        return self.precio_base

    def ticket(self):
        return f"{self.cliente} - {self.funcion}: ${self.calcular_precio():.2f}"


class BoletoEstudiante(Boleto):
    def __init__(self, cliente, funcion, descuento=0.30):
        super().__init__(cliente, funcion)
        self.descuento = descuento

    def calcular_precio(self):
        precio_normal = super().calcular_precio()
        return precio_normal - (precio_normal * self.descuento)


class BoletoCortesia(Boleto):
    def __init__(self, cliente, funcion):
        super().__init__(cliente, funcion)

    def calcular_precio(self):
        return 0


class BoletoTerceraEdad(BoletoEstudiante):
    def __init__(self, cliente, funcion):
        super().__init__(cliente, funcion, descuento=0.50)


