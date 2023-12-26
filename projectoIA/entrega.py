import datetime

from funcoesAux import *
from Grafo import *
from Nodo import *
import random

codigosIndisponiveis = [123, 929, 100, 99, 1, 237, 127, 898, 567, 23, 58, 7]


class Entrega:
    def __init__(self, codigo, rua, freguesia, volume, peso, prazo):
        self.codigo = codigo
        self.rua = rua
        self.freguesia = freguesia
        self.volume = volume
        self.peso = peso
        self.prazo = prazo

    def __eq__(self, other):
        if not isinstance(other, Entrega):
            return False
        return self.codigo == other.codigo

    def __str__(self):
        return f"Entrega({self.codigo}, {self.rua}, {self.freguesia}, " \
               f"{self.volume}, {self.peso}, {self.prazo})"


def define_codigo():
    codigoNovo = 0
    while codigoNovo in codigosIndisponiveis or codigoNovo <= 0:
        codigoNovo = random.randint(1, 1000)

    codigosIndisponiveis.append(codigoNovo)
    return codigoNovo


def adiciona_entrega():
    print("Preencha as informações relativas à sua encomenda")
    eC = define_codigo()
    eR = input("Morada: ")
    eF = input("Freguesia: ")
    eV = input("Volume da encomenda: ")
    eP = input("Peso da encomenda: ")
    eD_str = input("Data e hora em que pretende receber a encomenda(a-m-d e h:m): ")

    try:
        eD = datetime.datetime.strptime(eD_str, "%Y-%m-%d %H:%M")
    except ValueError as e:
        print(f"Error: {e}")

    entregaNova = Entrega(eC, eR, eF, eV, eP, eD)
    print(entregaNova)
    return entregaNova
