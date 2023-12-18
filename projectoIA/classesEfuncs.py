import datetime
from Dados import *
from Grafo import *
from Nodo import *

class estafeta:
    def __init__(self, nome, conjuntoEntregas, listaAvaliacoes, meioTransporte, localizacao):
        self.nome = nome
        self.conjuntoEntregas = conjuntoEntregas
        self.ranking = sum(listaAvaliacoes)/len(listaAvaliacoes)
        self.meioTransporte = meioTransporte
        self.localizacao= localizacao

class entrega:
    def __init__(self, codigo, rua, freguesia, volume, peso, prazo):
        self.codigo = codigo
        self.rua = rua
        self.freguesia = freguesia
        self.volume = volume
        self.peso = peso
        self.prazo = prazo

def getPrecoPorEntrega(self, entrega, estafeta): #calcula o preço de uma entrega
    if entrega is not None and estafeta is not None:
        self.preco = (entrega.volume * 0.2) + (entrega.peso * 0.3) + (poeEmHoras(entrega.prazo) / 0.3)
        if estafeta.meioTransporte == 'carro' : self.preco * 1.5
        if estafeta.meioTransporte == 'mota' : self.preco * 1.3
        if estafeta.meioTransporte == 'bicicleta' : self.preco * 1.1
    return self.preco


def poeEmHoras(prazo): #calcula em horas o tempo limite para a entrega
    return abs(dataActual - prazo).total_seconds() / 3600.0


def terminarEntrega(self, entrega, estafeta): #terminada a entrega, remove a mesma da lista de entregas dos estafeta, caso nao tenha cumprido o prazo é penalizado no ranking, caso tenha receberá a avaliação do cliente
    if estafeta.nome == 'Miguel' and estafeta.localizacao == entrega.rua:
        if dataActual > entrega.prazo : listaAvalsMiguel.append(0)
        else : avaliacaoDoCliente = input("Como avalia a sua experiência?")
        print("")
        listaAvalsMiguel.append(avaliacaoDoCliente)
        entregasMiguel.remove(entrega)
    elif estafeta.nome == 'Maria' and estafeta.localizacao == entrega.rua:
        if dataActual > entrega.prazo : listaAvalsMaria.append(0)
        else : avaliacaoDoCliente = input("Como avalia a sua experiência?")
        print("")
        listaAvalsMaria.append(avaliacaoDoCliente)
        entregasMaria.remove(entrega)
    elif estafeta.nome == 'Fernando' and estafeta.localizacao == entrega.rua:
        if dataActual > entrega.prazo : listaAvalsFernando.append(0)
        else : avaliacaoDoCliente = input("Como avalia a sua experiência?")
        print("")
        listaAvalsFernando.append(avaliacaoDoCliente)
        entregasFernando.remove(entrega)
    elif estafeta.nome == 'Pedro' and estafeta.localizacao == entrega.rua:
        if dataActual > entrega.prazo : listaAvalsPedro.append(0)
        else : avaliacaoDoCliente = input("Como avalia a sua experiência?")
        print("")
        listaAvalsPedro.append(avaliacaoDoCliente)
        entregasPedro.remove(entrega)
    elif estafeta.nome == 'Luis' and estafeta.localizacao == entrega.rua:
        if dataActual > entrega.prazo : listaAvalsLuis.append(0)
        else : avaliacaoDoCliente = input("Como avalia a sua experiência?")
        print("")
        listaAvalsLuis.append(avaliacaoDoCliente)
        entregasLuis.remove(entrega)
    elif estafeta.nome == 'Carlos' and estafeta.localizacao == entrega.rua:
        if dataActual > entrega.prazo : listaAvalsCarlos.append(0)
        else : avaliacaoDoCliente = input("Como avalia a sua experiência?")
        print("")
        listaAvalsCarlos.append(avaliacaoDoCliente)
        entregasCarlos.remove(entrega)
    elif estafeta.nome == 'Manuel' and estafeta.localizacao == entrega.rua:
        if dataActual > entrega.prazo : listaAvalsManuel.append(0)
        else: avaliacaoDoCliente = input("Como avalia a sua experiência?")
        print("")
        listaAvalsManuel.append(avaliacaoDoCliente)
        entregasManuel.remove(entrega)


def calculaSpeedConsoantePeso (self, entregas, meioTransporte):
    soma = sum(entregas.peso)
    if meioTransporte == 'bicicleta' and soma < 5 : return (10-(soma*0.6))
    elif meioTransporte == 'mota' and soma < 20 : return (20-(soma*0.5))
    elif meioTransporte == 'carro' and soma < 100 : return (100-(soma*0.1))
    else : print("Excede o peso maximo")

def fazEntregas (self, estafeta, metodoProcura): #sabendo o metodo, vai percorrendo a lista de entregas, calcula a melhor rota para cada uma e fá-la, até chegar ao fim.
    while estafeta.conjuntoEntregas != None:
        if metodoProcura == 'DFS':
            x = self.procura_DFS(estafeta.localizacao, estafeta.conjuntoEntregas.first.rua, path=[], visited=set())
            print(x)
            estafeta.localizacao = entrega.first.rua
            terminarEntrega(estafeta.conjuntoEntregas.first, estafeta)
        elif metodoProcura == 'BFS':
            x = self.procura_BFS(estafeta.localizacao, estafeta.conjuntoEntregas.first.rua, path=[], visited=set())
            print(x)
            estafeta.localizacao = entrega.first.rua
            terminarEntrega(estafeta.conjuntoEntregas.first, estafeta)
        elif metodoProcura == 'A*':
            x = self.procura_aStar(estafeta.localizacao, estafeta.conjuntoEntregas.first.rua)
            print(x)
            estafeta.localizacao = entrega.first.rua
            terminarEntrega(estafeta.conjuntoEntregas.first, estafeta)
        elif metodoProcura == 'greedy':
            x = self.greedy(estafeta.localizacao, estafeta.conjuntoEntregas.first.rua)
            print(x)
            estafeta.localizacao = entrega.first.rua
            terminarEntrega(estafeta.conjuntoEntregas.first, estafeta)



