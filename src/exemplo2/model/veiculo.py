from dataclasses import dataclass
from typing import Optional


class Veiculo:
    def __init__(self, id=None, marca="", modelo="", chassi="", placa="", cor=""):
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.chassi = chassi
        self.placa = placa
        self.cor = cor
