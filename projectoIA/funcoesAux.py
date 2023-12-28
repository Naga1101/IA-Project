import datetime

from entrega import Entrega
from estafeta import estafeta
from entrega import *
from Grafo import *
from Nodo import *
import copy

dataAtual = datetime.datetime.now()


## Adicionar encomenda

def getPrecoPorEntrega(self, entrega, estafeta):  # calcula o preço de uma entrega
    if entrega is not None and estafeta is not None:
        self.preco = (entrega.volume * 0.2) + (entrega.peso * 0.3) + (poeEmHoras(entrega.prazo) / 0.3)
        if estafeta.meioTransporte == 'carro': self.preco * 1.5
        if estafeta.meioTransporte == 'mota': self.preco * 1.3
        if estafeta.meioTransporte == 'bicicleta': self.preco * 1.1
    return self.preco


def atribui_estafeta(entrega, estafetas_loaded, distancia):  ## distancia 40 por enquanto
    estafeta_mais_rapido = None
    maiorVelocidade = 0
    for estafeta in estafetas_loaded:
        velocidade = calculaSpeedConsoantePeso(entrega, estafeta, distancia)
        if velocidade > maiorVelocidade or estafeta_mais_rapido == None:
            maiorVelocidade = velocidade
            estafeta_mais_rapido = estafeta
    print(f"Nome: {estafeta_mais_rapido.nome}")
    estafeta_mais_rapido.conjuntoEntregas.append(entrega)
    for entrega_obj in estafeta_mais_rapido.conjuntoEntregas:
        print(f"  {entrega_obj}")


def poeEmHoras(prazo):  # calcula em horas o tempo limite para a entrega
    return abs(dataAtual - prazo).total_seconds() / 3600.0


def chega_a_tempo(prazo, velocidade, distancia,
                  estafeta):  # velocidade km\h ex 20km\h ---> 20km em 1 hora se distanca for 40 e tempoEntrega = 1 retorna -1
    tempoLimite = poeEmHoras(prazo)
    tempoChegar = distancia / velocidade

    if tempoChegar < tempoLimite:
        print("A entrega chega dentro do prazo com o estafeta", estafeta.nome)
        return velocidade

    print("A entrega não chega a tempo com o estafeta", estafeta.nome)
    return -1


def calculaSpeedConsoantePeso(entrega, estafeta, distancia):  # calcula velocidade em km\h
    veiculo = estafeta.meioTransporte
    pesoMax, velocidadeMax = meioTransportes[veiculo]
    soma = estafeta.pesoAtual + int(entrega.peso)
    if soma < pesoMax:
        if veiculo == 'bicicleta':
            velocidade = (velocidadeMax - (soma * 0.6))
        elif veiculo == 'mota':
            velocidade = (velocidadeMax - (soma * 0.5))
        elif veiculo == 'carro':
            velocidade = (velocidadeMax - (soma * 0.1))

        velocidade = chega_a_tempo(entrega.prazo, velocidade, distancia, estafeta)
        return velocidade
    else:
        print("Excede o peso maximo do estafeta", estafeta.nome)
        return -1


def fazEntregas(self, estafeta,
                metodoProcura):  # sabendo o metodo, vai percorrendo a lista de entregas, calcula a melhor rota para cada uma e fá-la, até chegar ao fim.
    while estafeta.conjuntoEntregas != None:
        if metodoProcura == 'DFS':
            x = self.procura_DFS(estafeta.localizacao, estafeta.conjuntoEntregas.first.rua, path=[], visited=set())
            print(x)
            estafeta.localizacao = Entrega.first.rua
            terminarEntrega(estafeta.conjuntoEntregas.first, estafeta)
        elif metodoProcura == 'BFS':
            x = self.procura_BFS(estafeta.localizacao, estafeta.conjuntoEntregas.first.rua, path=[], visited=set())
            print(x)
            estafeta.localizacao = Entrega.first.rua
            terminarEntrega(estafeta.conjuntoEntregas.first, estafeta)
        elif metodoProcura == 'A*':
            x = self.procura_aStar(estafeta.localizacao, estafeta.conjuntoEntregas.first.rua)
            print(x)
            estafeta.localizacao = Entrega.first.rua
            terminarEntrega(estafeta.conjuntoEntregas.first, estafeta)
        elif metodoProcura == 'greedy':
            x = self.greedy(estafeta.localizacao, estafeta.conjuntoEntregas.first.rua)
            print(x)
            estafeta.localizacao = Entrega.first.rua
            terminarEntrega(estafeta.conjuntoEntregas.first, estafeta)


def listarRanking(listaEstafetas):
    sorted_list = sorted(listaEstafetas, key=lambda x: x.ranking, reverse=True)
    i = 0
    for estafeta in sorted_list:
        print(f"{i}:{estafeta.nome}, ")


def copy_estafeta(estafeta):
    return copy.deepcopy(estafeta)


def compareAlgorithms(g, listaEstafetas):
    DFS_results = {}
    BFS_results = {}
    Greedy_results = {}
    aStar_results = {}
    for estafeta in listaEstafetas:
        distDFS = 0
        atual = 'Rua da Universidade'  # centro de distribuição
        entregas_DFS = estafeta.conjuntoEntregas.copy()
        while entregas_DFS:
            entrega = entregas_DFS[0]
            res = g.procura_DFS(atual, entrega.rua, path=[], visited=set())

            if res is None:
                entregas_DFS.pop(0)
            else:
                caminho, dist = res
                distDFS += dist
                atual = entrega.rua
                entregas_DFS.pop(0)

        DFS_results[estafeta.nome] = distDFS / 10
    print(DFS_results)

    for estafeta in listaEstafetas:
        distBFS = 0
        atual = 'Rua da Universidade'  # centro de distribuição
        entregas_BFS = estafeta.conjuntoEntregas.copy()
        while entregas_BFS:
            entrega = entregas_BFS[0]
            res = g.procura_BFS(atual, entrega.rua)
            if res is None:
                entregas_BFS.pop(0)
            else:
                caminho, dist = res
                distBFS += dist
                atual = entrega.rua
                entregas_BFS.pop(0)

        BFS_results[estafeta.nome] = distBFS / 10

    print(BFS_results)

    for estafeta in listaEstafetas:
        dist_greedy = 0
        atual = 'Rua da Universidade'  # centro de distribuição
        estafeta_Greedy = copy_estafeta(estafeta)
        for entrega in estafeta_Greedy.conjuntoEntregas:
            g.calculate_all_heuristics(atual, entrega.rua)
            res = g.greedy(atual, entrega.rua)
            if res is None:
                pass
                # print("Não foi possivel realizar a entrega")
            else:
                _, dist = res
                # terminarEntrega(entrega, estafeta)
                dist_greedy += dist
                atual = entrega.rua
                estafeta_Greedy.remove_entrega(entrega)

        Greedy_results[estafeta.nome] = dist_greedy / 10

    print(Greedy_results)

    for estafeta in listaEstafetas:
        dist_aStar = 0
        atual = 'Rua da Universidade'  # centro de distribuição
        estafeta_aStar = copy_estafeta(estafeta)
        for entrega in estafeta_aStar.conjuntoEntregas:
            g.calculate_all_heuristics(atual, entrega.rua)
            res = g.procura_aStar(atual, entrega.rua)
            if res is None:
                pass
                # print("Não foi possivel realizar a entrega")
            else:
                _, dist = res
                dist_aStar += dist
                atual = entrega.rua
                estafeta_aStar.remove_entrega(entrega)

        aStar_results[estafeta.nome] = dist_aStar / 10

    print(aStar_results)
