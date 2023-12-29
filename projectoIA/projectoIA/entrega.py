import datetime
from funcoesAux import *
from Grafo import Graph
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


def adiciona_entrega(g, algoritmo):
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

    if algoritmo == 'DFS':
        inicio = 'Travessa da Avenida de São Miguel'
        res = g.procura_DFS(inicio, eR, path=[], visited=set())
        caminho, dist = res
        
    entregaNova = Entrega(eC, eR, eF, eV, eP, eD)
    print(entregaNova)
    return entregaNova, dist


def terminarEntrega(entrega, estafeta):  #### Feita e a funcionar
    if isinstance(entrega.prazo, str):
        prazo_datetime = datetime.datetime.strptime(entrega.prazo, '%Y-%m-%d %Hh')
    else:
        prazo_datetime = entrega.prazo
    if datetime.datetime.now() > prazo_datetime:
        estafeta.listaAvaliacoes.append(0)
        print("Entrega atrasada! Penalização no ranking.")
    else:
        avaliacaoDoCliente = input("Como avalia a sua experiência? ")
        print("")
        estafeta.listaAvaliacoes.append(int(avaliacaoDoCliente))
    estafeta.remove_entrega(entrega)
    estafeta.setPesoAtual(0)
    estafeta.atualiza_ranking()


def iniciarEntregasDFS(g, estafetas_loaded):
    caminho_final = []
    for estafeta in estafetas_loaded:
        distTotal = 0
        atual = 'Rua da Universidade'  # centro de distribuição
        #for entrega in estafeta.conjuntoEntregas:
        while estafeta.conjuntoEntregas:
            print(estafeta.nome)
            entrega = estafeta.conjuntoEntregas[0]
            res = g.procura_DFS(atual, entrega.rua, path=[], visited=set())
            if res is None:
                print("Não foi possivel realizar a entrega")
                print(entrega.rua)
                estafeta.conjuntoEntregas.pop(0)
            else:
                caminho, dist = res
                #print("Distância percorrida", dist)
                distTotal += dist
                caminho_final.append(caminho)
                terminarEntrega(entrega, estafeta)
                atual = entrega.rua
        
        print("O estafeta", estafeta.nome, "percorreu um total de", (distTotal/10), "decâmetros")

    return caminho_final

def iniciarEntregasBFS(g, estafetas_loaded):
    caminho_final = []
    for estafeta in estafetas_loaded:
        distTotal = 0
        atual = 'Rua da Universidade'  # centro de distribuição
        #for entrega in estafeta.conjuntoEntregas:
        while estafeta.conjuntoEntregas:
            entrega = estafeta.conjuntoEntregas[0]
            # g.procuraDFS(atual, entrega.rua, path=[], visited=set())
            res = g.procura_BFS(atual, entrega.rua)
            if res is None:
                print("Não foi possivel realizar a entrega")
                print(entrega.rua)
                estafeta.conjuntoEntregas.pop(0)
            else:
                caminho, dist = res
                #print("Distância percorrida", dist)
                distTotal += dist
                caminho_final.append(caminho)
                terminarEntrega(entrega, estafeta)
                atual = entrega.rua

        print("O estafeta", estafeta.nome, "percorreu um total de", (distTotal / 10), "decâmetros")

    return caminho_final

def iniciarEntregaGreedy(g, estafetas_loaded):
    # METER ISTO COM WHILE PORQUE SENAO SO FAZ UMA
    caminho_final = []
    for estafeta in estafetas_loaded:
        atual = 'Rua da Universidade'  # centro de distribuição
        while estafeta.conjuntoEntregas:
            entrega = estafeta.conjuntoEntregas[0]
            g.calculate_all_heuristics(atual, entrega.rua)
            res = g.greedy(atual, entrega.rua)
            if res is None:
                print("Não foi possivel realizar a entrega")
                estafeta.conjuntoEntregas.pop(0)
            else:
                caminho_final.append(res)
                terminarEntrega(entrega, estafeta)
                atual = entrega.rua

    return caminho_final

def iniciarEntregaAstar(g, estafetas_loaded):
    caminho_final = []
    for estafeta in estafetas_loaded:
        atual = 'Rua da Universidade'  # centro de distribuição
        while estafeta.conjuntoEntregas:
            entrega = estafeta.conjuntoEntregas[0]
            g.calculate_all_heuristics(atual, entrega.rua)
            res = g.procura_aStar(atual, entrega.rua)
            print(estafeta.nome)
            if res is None:
                print("Não foi possivel realizar a entrega")
                estafeta.conjuntoEntregas.pop(0)
            else:
                caminho_final.append(res)
                terminarEntrega(entrega, estafeta)
                atual = entrega.rua

    return caminho_final
