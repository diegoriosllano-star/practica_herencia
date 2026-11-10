"""
EJERCICIO 2. ESTACIONAMIENTO

Estancia:
- Tiene placa y horas.
- Cobra $20 por hora.
- Genera un ticket con el formato:
  Placa (horas h): $cobro

EstanciaPension:
- Hereda de Estancia.
- Siempre dura 24 horas.
- Tiene tarifa fija de $250.

EstanciaNocturna:
- Hereda de Estancia.
- Cobra lo mismo que una estancia normal más $50.

Reto:
- Si las horas son 0 o menores, debe lanzar:
  ValueError("Las horas deben ser mayores que cero")
"""


class Estancia:
    def __init__(self, placa, horas):
        if horas <= 0:
            raise ValueError("Las horas deben ser mayores que cero")

        self.placa = placa
        self.horas = horas

    def cobrar(self):
        return self.horas * 20

    def ticket(self):
        return f"{self.placa} ({self.horas} h): ${self.cobrar():.2f}"


class EstanciaPension(Estancia):
    def __init__(self, placa):
        super().__init__(placa, 24)

    def cobrar(self):
        return 250


class EstanciaNocturna(Estancia):
    def __init__(self, placa, horas):
        super().__init__(placa, horas)

    def cobrar(self):
        return super().cobrar() + 50