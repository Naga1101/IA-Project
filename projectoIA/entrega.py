import random

from funcoesAux import *
from Grafo import *

codigosIndisponiveis = [123, 929, 100, 99, 1, 237, 127, 898, 567, 23, 58, 7, 696, 604, 603, 400]


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


def adiciona_entrega(g):
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

    inicio = 'Rua da Universidade'
    res = g.procura_DFS(inicio, eR, path=[], visited=set())
    _, distDFS, _ = res
    res = g.procura_BFS(inicio, eR)
    _, distBFS, _ = res
    res = g.procura_custo_uniforme(inicio, eR)
    _, distCU, _ = res
    g.calculate_all_heuristics(inicio, eR)
    res = g.greedy(inicio, eR)
    _, distGRE, _ = res
    res = g.procura_aStar(inicio, eR)
    _, distAS, _ = res


    distancias = [('A-Star', distAS),('DFS', distDFS),('BFS', distBFS),('Custo Uniforme', distCU),('Greedy', distGRE)]

    menor_distancia = min(distancias, key=lambda x: x[1])[1]
    algoritmos_menores = [(algo, dist) for algo, dist in distancias if dist == menor_distancia]

    entregaNova = Entrega(eC, eR, eF, eV, eP, eD)

    if len(algoritmos_menores) == 1:
        algoritmoSelec, _ = algoritmos_menores[0]
        print("O algoritmo que calculou a menor distância para a entrega", entregaNova, "foi o", algoritmoSelec)
    else:
        print("Os algoritmos que calcularam a menor distância para a entrega", entregaNova, "foram:")
        for algoritmo, dist in algoritmos_menores:
            print(algoritmo, dist)

    return entregaNova, menor_distancia


def getPrecoPorEntrega(self, entrega, estafeta):  # calcula o preço de uma entrega
    if entrega is not None and estafeta is not None:
        self.preco = (entrega.volume * 0.2) + (entrega.peso * 0.3) + (poeEmHoras(entrega.prazo) / 0.3)
        if estafeta.meioTransporte == 'carro': self.preco * 1.5
        if estafeta.meioTransporte == 'mota': self.preco * 1.3
        if estafeta.meioTransporte == 'bicicleta': self.preco * 1.1
    return self.preco


def terminarEntrega(entrega, estafeta):
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


def organizaLista(g, partida,
                  listaEntregas):  # coloca em primeiro da lista a encomenda mais próxima de onde o estafeta se encontra
    posLista = 0
    posProx = 0
    maisProx = None
    distProx = -1
    coordPart = g.get_node_by_name(partida).getCoord()
    for entrega in listaEntregas:
        coordEntr = g.get_node_by_name(entrega.rua).getCoord()
        dist = int(round(math.sqrt((coordEntr[1] - coordPart[1]) ** 2 + (coordEntr[0] - coordPart[0]) ** 2)))
        if distProx < 0 or dist < distProx:
            distProx = dist
            maisProx = entrega
            posProx = posLista  # no caso de ser o primeiro diz que a posição é 0
        posLista += 1
    aux = listaEntregas[0]
    listaEntregas[0] = maisProx
    listaEntregas[posProx] = aux
    return listaEntregas


def iniciarEntregasDFS(g, estafetas_loaded):
    caminho_final = {}

    perc_algoritmo = {}
    for estafeta in estafetas_loaded:
        distTotal = 0
        atual = 'Rua da Universidade'  # centro de distribuição

        caminho_estafeta = []
        path_algoritmo = []

        while estafeta.conjuntoEntregas:
            print(estafeta.nome)
            entrega = estafeta.conjuntoEntregas[0]
            path, custo, total_path = g.procura_DFS(atual, entrega.rua, path=[], visited=set())
            path_algoritmo.append(total_path)

            if (path, custo) is None:
                print("Não foi possivel realizar a entrega")
                print(entrega.rua)
                estafeta.conjuntoEntregas.pop(0)
            else:
                caminho, dist = (path, custo)
                total = (path, custo)
                distTotal += dist
                caminho_estafeta.append(total)
                terminarEntrega(entrega, estafeta)
                atual = entrega.rua

        perc_algoritmo[estafeta.nome] = path_algoritmo
        caminho_final[estafeta.nome] = caminho_estafeta

        print("O estafeta", estafeta.nome, "percorreu um total de", (distTotal / 10), "decâmetros")

    return caminho_final, perc_algoritmo


def iniciarEntregasBFS(g, estafetas_loaded):
    caminho_final = {}

    perc_algoritmo = {}
    for estafeta in estafetas_loaded:
        distTotal = 0
        atual = 'Rua da Universidade'  # centro de distribuição
        # for entrega in estafeta.conjuntoEntregas:
        caminho_estafeta = []
        path_algoritmo = []
        while estafeta.conjuntoEntregas:
            entrega = estafeta.conjuntoEntregas[0]
            # g.procuraDFS(atual, entrega.rua, path=[], visited=set())
            path, custo, total_path = g.procura_BFS(atual, entrega.rua)
            path_algoritmo.append(total_path)
            if (path, custo) is None:
                print("Não foi possivel realizar a entrega")
                print(entrega.rua)
                estafeta.conjuntoEntregas.pop(0)
            else:
                caminho, dist = (path, custo)
                total = (path, custo)
                distTotal += dist
                caminho_estafeta.append(total)
                terminarEntrega(entrega, estafeta)
                atual = entrega.rua

        perc_algoritmo[estafeta.nome] = path_algoritmo
        caminho_final[estafeta.nome] = caminho_estafeta

        print("O estafeta", estafeta.nome, "percorreu um total de", (distTotal / 10), "decâmetros")

    return caminho_final, perc_algoritmo


def iniciarEntregasCustoUniforme(g, estafetas_loaded):
    caminho_final = {}

    perc_algoritmo = {}
    for estafeta in estafetas_loaded:
        distTotal = 0
        atual = 'Rua da Universidade'  # centro de distribuição
        # for entrega in estafeta.conjuntoEntregas:
        caminho_estafeta = []
        path_algoritmo = []
        while estafeta.conjuntoEntregas:
            entrega = estafeta.conjuntoEntregas[0]
            path, custo, total_path = g.procura_custo_uniforme(atual, entrega.rua)
            path_algoritmo.append(total_path)
            if (path, custo) is None:
                print("Não foi possivel realizar a entrega")
                print(entrega.rua)
                estafeta.conjuntoEntregas.pop(0)
            else:
                caminho, dist = (path, custo)
                total = (path, custo)
                distTotal += dist
                caminho_estafeta.append(total)
                terminarEntrega(entrega, estafeta)
                atual = entrega.rua

        perc_algoritmo[estafeta.nome] = path_algoritmo
        caminho_final[estafeta.nome] = caminho_estafeta

        print("O estafeta", estafeta.nome, "percorreu um total de", (distTotal / 10), "decâmetros")

    return caminho_final, perc_algoritmo


def iniciarEntregaGreedy(g, estafetas_loaded):
    caminho_final = {}
    perc_algoritmo = {}

    for estafeta in estafetas_loaded:
        atual = 'Rua da Universidade'  # centro de distribuição
        caminho_estafeta = []
        path_algoritmo = []

        while estafeta.conjuntoEntregas:
            listaEntregas = organizaLista(g, atual, estafeta.conjuntoEntregas)
            entrega = listaEntregas[0]
            g.calculate_all_heuristics(atual, entrega.rua)
            path, custo, total_path = g.greedy(atual, entrega.rua)
            path_algoritmo.append(total_path)

            if (path, custo) is None:
                print("Não foi possivel realizar a entrega")
                estafeta.conjuntoEntregas = listaEntregas
                estafeta.conjuntoEntregas.pop(0)
            else:
                total = (path, custo)
                caminho_estafeta.append(total)
                terminarEntrega(entrega, estafeta)
                atual = entrega.rua

        perc_algoritmo[estafeta.nome] = path_algoritmo
        caminho_final[estafeta.nome] = caminho_estafeta

    return caminho_final, perc_algoritmo


def iniciarEntregaAstar(g, estafetas_loaded):
    caminho_final = {}
    perc_algoritmo = {}

    for estafeta in estafetas_loaded:
        atual = 'Rua da Universidade'  # centro de distribuição
        caminho_estafeta = []
        path_algoritmo = []

        while estafeta.conjuntoEntregas:
            listaEntregas = organizaLista(g, atual, estafeta.conjuntoEntregas)
            entrega = listaEntregas[0]
            g.calculate_all_heuristics(atual, entrega.rua)
            path, custo, total_path = g.procura_aStar(atual, entrega.rua)
            path_algoritmo.append(total_path)

            if (path, custo) is None:
                print("Não foi possivel realizar a entrega")
                estafeta.conjuntoEntregas = listaEntregas
                estafeta.conjuntoEntregas.pop(0)
            else:
                total = (path, custo)
                caminho_estafeta.append(total)
                terminarEntrega(entrega, estafeta)
                atual = entrega.rua

        perc_algoritmo[estafeta.nome] = path_algoritmo
        caminho_final[estafeta.nome] = caminho_estafeta

    return caminho_final, perc_algoritmo
