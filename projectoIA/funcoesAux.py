import datetime

from entrega import Entrega
from estafeta import *
from entrega import *
from Grafo import *
from Nodo import *
import copy

dataAtual = datetime.datetime.now()


def atribui_estafeta(entrega, estafetas_loaded, distancia):  ## distancia 40 por enquanto
    estafeta_mais_rapido = None
    maiorVelocidade = 0
    pegadaEcológica = 3
    for estafeta in estafetas_loaded:
        veiculo = estafeta.meioTransporte
        _, _, custoEcol = meioTransportes[veiculo]
        if custoEcol < pegadaEcológica:
            velocidade = calculaSpeedConsoantePeso(entrega, estafeta, distancia)
            if velocidade > 0:
                if velocidade > maiorVelocidade or estafeta_mais_rapido == None or custoEcol < pegadaEcológica:
                    maiorVelocidade = velocidade
                    estafeta_mais_rapido = estafeta
                    pegadaEcológica = custoEcol

    if estafeta_mais_rapido != None:
        print(f"Nome: {estafeta_mais_rapido.nome} | Veiculo: {estafeta_mais_rapido.meioTransporte}")
        estafeta_mais_rapido.conjuntoEntregas.append(entrega)
        for entrega_obj in estafeta_mais_rapido.conjuntoEntregas:
            print(f"  {entrega_obj}")
    else:
        print("Encomenda não chega dentro do prazo pretendido em nenhum estafeta!")


def poeEmHoras(prazo):  # calcula em horas o tempo limite para a entrega
    return abs(dataAtual - prazo).total_seconds() / 3600.0


def chega_a_tempo(prazo, velocidade, distancia,
                  estafeta):  # velocidade km\h ex 20km\h ---> 20km em 1 hora se distanca for 40 e tempoEntrega = 1 retorna -1
    tempoLimite = poeEmHoras(prazo)
    tempoChegar = distancia / velocidade

    if tempoChegar < tempoLimite:
        print("A entrega chega dentro do prazo com o estafeta", estafeta.nome, "e veículo", estafeta.meioTransporte)
        return velocidade

    print("A entrega não chega a tempo com o estafeta", estafeta.nome, "e veículo", estafeta.meioTransporte)
    return -1


def calculaSpeedConsoantePeso(entrega, estafeta, distancia):  # calcula velocidade em km\h
    veiculo = estafeta.meioTransporte
    pesoMax, velocidadeMax, _ = meioTransportes[veiculo]
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


def listarRanking(listaEstafetas):
    sorted_list = sorted(listaEstafetas, key=lambda x: x.ranking, reverse=True)
    for i, estafeta in enumerate(sorted_list, start=1):
        print(f"{i}:{estafeta.nome}: {estafeta.ranking}")
        
def rankingVeiculos(listaEstafetas):
    mediaBicicleta = 0
    estBicl = 0
    mediaMota = 0
    estMota = 0
    mediaCarro = 0
    estCarro = 0
    
    for estafeta in listaEstafetas:
        veiculo = estafeta.meioTransporte
        if veiculo == 'bicicleta':
            estBicl += 1
            mediaBicicleta += (estafeta.ranking + 1) 
        elif veiculo == 'mota':
            estMota += 1
            mediaMota += (estafeta.ranking - 0.5)
        else:
            estCarro += 1
            mediaCarro += (estafeta.ranking - 1)
    
    mediaBicicleta = mediaBicicleta/estBicl
    if mediaBicicleta > 5: mediaBicicleta = 5
    if mediaBicicleta < 0: mediaBicicleta = 0
    mediaMota = mediaMota/estMota
    if mediaMota > 5: mediaMota = 5
    if mediaMota < 0: mediaMota = 0
    mediaCarro = mediaCarro/estCarro
    if mediaCarro > 5: mediaCarro = 5
    if mediaCarro < 0: mediaCarro = 0
    
    data = [('Bicicleta', mediaBicicleta),('Mota', mediaMota),('Carro', mediaCarro)]
    medias = sorted(data, key=lambda x: x[1], reverse=True)
    for rank, (vehicle, media) in enumerate(medias, start=1):
        print(f"{rank}: {vehicle} : {media}")
    
    


def copy_estafeta(estafeta):
    return copy.deepcopy(estafeta)


def compareAlgorithms(g, listaEstafetas):
    # results = custo caminhos, path = caminho
    DFS_results = {}
    DFS_path = {}
    BFS_results = {}
    BFS_path = {}
    UC_results = {}
    UC_path = {}
    Greedy_results = {}
    Greedy_path = {}
    aStar_results = {}
    aStar_path = {}
    for estafeta in listaEstafetas:
        distDFS = 0
        atual = 'Rua da Universidade'  # centro de distribuição
        entregas_DFS = estafeta.conjuntoEntregas.copy()
        caminho_estafeta = []

        while entregas_DFS:
            entrega = entregas_DFS[0]
            res = g.procura_DFS(atual, entrega.rua, path=[], visited=set())

            if res is None:
                entregas_DFS.pop(0)
            else:
                caminho, dist, resto = res
                distDFS += dist
                atual = entrega.rua
                caminho_estafeta.append(caminho)
                entregas_DFS.pop(0)

        DFS_results[estafeta.nome] = distDFS / 10
        DFS_path[estafeta.nome] = caminho_estafeta
    print("DFS Results:", DFS_results)

    for estafeta in listaEstafetas:
        distBFS = 0
        atual = 'Rua da Universidade'  # centro de distribuição
        entregas_BFS = estafeta.conjuntoEntregas.copy()
        caminho_estafeta = []
        while entregas_BFS:
            entrega = entregas_BFS[0]
            res = g.procura_BFS(atual, entrega.rua)
            if res is None:
                entregas_BFS.pop(0)
            else:
                caminho, dist, _ = res
                distBFS += dist
                atual = entrega.rua
                caminho_estafeta.append(caminho)
                entregas_BFS.pop(0)

        BFS_path[estafeta.nome] = caminho_estafeta
        BFS_results[estafeta.nome] = distBFS / 10

    print("BFS Results:", BFS_results)

    for estafeta in listaEstafetas:
        distUC = 0
        atual = 'Rua da Universidade'  # centro de distribuição
        entregas_UC = estafeta.conjuntoEntregas.copy()
        caminho_estafeta = []

        while entregas_UC:
            entrega = entregas_UC[0]
            res = g.procura_custo_uniforme(atual, entrega.rua)

            if res is None:
                entregas_UC.pop(0)
            else:
                caminho, dist, resto = res
                distUC += dist
                atual = entrega.rua
                caminho_estafeta.append(caminho)
                entregas_UC.pop(0)

        UC_results[estafeta.nome] = distUC / 10
        UC_path[estafeta.nome] = caminho_estafeta
    print("Uniform Cost Results:", UC_results)

    for estafeta in listaEstafetas:
        dist_greedy = 0
        atual = 'Rua da Universidade'  # centro de distribuição
        estafeta_Greedy = copy_estafeta(estafeta)
        caminho_estafeta = []
        while estafeta_Greedy.conjuntoEntregas:
            listaEntregas = organizaLista(g, atual, estafeta_Greedy.conjuntoEntregas)
            entrega = listaEntregas[0]
            g.calculate_all_heuristics(atual, entrega.rua)
            res = g.greedy(atual, entrega.rua)
            if res is None:
                pass
                # print("Não foi possivel realizar a entrega")
            else:
                caminho, dist, _ = res
                # terminarEntrega(entrega, estafeta)
                dist_greedy += dist
                atual = entrega.rua
                caminho_estafeta.append(caminho)
                estafeta_Greedy.remove_entrega(entrega)
        Greedy_path[estafeta.nome] = caminho_estafeta
        Greedy_results[estafeta.nome] = dist_greedy / 10

    print("Greedy Results:", Greedy_results)

    for estafeta in listaEstafetas:
        dist_aStar = 0
        atual = 'Rua da Universidade'  # centro de distribuição
        estafeta_aStar = copy_estafeta(estafeta)
        caminho_estafeta = []
        while estafeta_aStar.conjuntoEntregas:
            listaEntregas = organizaLista(g, atual, estafeta_aStar.conjuntoEntregas)
            entrega = listaEntregas[0]
            g.calculate_all_heuristics(atual, entrega.rua)
            res = g.procura_aStar(atual, entrega.rua)
            if res is None:
                pass
                # print("Não foi possivel realizar a entrega")
            else:
                caminho, dist, _ = res
                dist_aStar += dist
                atual = entrega.rua
                caminho_estafeta.append(caminho)
                estafeta_aStar.remove_entrega(entrega)
        aStar_path[estafeta.nome] = caminho_estafeta
        aStar_results[estafeta.nome] = dist_aStar / 10

    print("aStar Results:", aStar_results)

    return DFS_path, BFS_path, Greedy_path, aStar_path, UC_path


def printPaths(caminho_final):
    for estafeta, paths in caminho_final.items():
        print(f"Estafeta: {estafeta}")
        custo_total = 0

        for n_entrega, (caminho, custo) in enumerate(paths, start=1):
            custo_total += custo
            print(f"Caminho para entrega {n_entrega}: {caminho} - Custo: {custo / 10}")

        print(f"Distancia percorrida por {estafeta}: {custo_total / 10}\n")


def printPathsTotal(caminho_final):
    for estafeta, paths in caminho_final.items():
        print(f"Estafeta: {estafeta}")

        for n_entrega, caminho in enumerate(paths, start=1):
            print(f"Caminho para entrega {n_entrega}: {caminho}")
        print()
