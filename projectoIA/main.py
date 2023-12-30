from funcoesAux import *
from estafeta import *
from Grafo import Graph
import osmnx as ox


def main():
    data_filename = 'Dados.json'  # Replace with your actual file name
    estafetas_loaded = load_Estafetas(data_filename)

    g = Graph()
    g.parse_file('teste.csv')
    # start_node_name = "Rua José Antunes Guimarães"
    # end_node_name = "Rua Manuel Fernandes Franqueira"
    # g.calculate_all_heuristics(start_node_name, end_node_name)

    saida = -1
    while saida != 0:
        print("1-Imprimir Grafo")
        print("2-Desenhar Grafo")
        print("3-Imprimir  nodos de Grafo")
        print("4-Imprimir arestas de Grafo")
        print("5-DFS")
        print("6-BFS")
        print("7-A*")
        print("8-Gulosa")
        print("9-Comparar Algoritmos")
        print("10-Estafetas")
        print("11-Adicionar Encomenda")
        print("0-Saír")

        saida = int(input("introduza a sua opcao-> "))
        if saida == 0:
            print("saindo.......")
        elif saida == 1:
            print(g.m_graph)
            l = input("prima enter para continuar")
        elif saida == 2:
            g.desenha()
        elif saida == 3:
            print(g.m_graph.keys())
            l = input("prima enter para continuar")
        elif saida == 4:
            print(g.imprime_aresta())
            l = input("prima enter para continuar")
        elif saida == 5:
            #inicio = input("Nodo inicial->")
            #fim = input("Nodo final->")
            #print(g.procura_DFS(inicio, fim, path=[], visited=set()))
            print("1-Realizar Entregas")
            print("2-Adicionar Entrega")
            inp = int(input("introduza a sua opcao-> "))
            if inp == 1: 
                path = iniciarEntregasDFS(g, estafetas_loaded)
                print(path)
            else:
                entregaNova, dist = adiciona_entrega(g, "DFS")
                atribui_estafeta(entregaNova, estafetas_loaded, dist)
            l = input("prima enter para continuar")
        elif saida == 6:
            #inicio = input("Nodo inicial->")
            #fim = input("Nodo final->")
            #print(g.procura_BFS(inicio, fim))
            path = iniciarEntregasBFS(g, estafetas_loaded)
            print(path)
            l = input("prima enter para continuar")
        elif saida == 7:
            #inicio = input("Nodo inicial->")
            #fim = input("Nodo final->")
            #print(g.procura_aStar(inicio, fim))
            path = iniciarEntregaAstar(g, estafetas_loaded)
            print(path)
            l = input("prima enter para continuar")
        elif saida == 8:
            # inicio = input("Nodo inicial->")
            # fim = input("Nodo final->")
            # print(g.greedy(inicio, fim))
            path = iniciarEntregaGreedy(g, estafetas_loaded)
            print(path)
            l = input("prima enter para continuar")
        elif saida == 9:
            compareAlgorithms(g, estafetas_loaded)
        elif saida == 10:
            for estafeta_obj in estafetas_loaded:
                print(f"Nome: {estafeta_obj.nome}")
                for entrega_obj in estafeta_obj.conjuntoEntregas:
                    print(f"  {entrega_obj}")
                heuristics_dict = calcula_heuristica_entregas(estafeta_obj, g)
                print(heuristics_dict)
                print(f"Carga atual: {estafeta_obj.pesoAtual}")
                print(f"Ranking: {estafeta_obj.ranking}")
                print(f"Meio de Transporte: {estafeta_obj.meioTransporte}")
                print(f"Localizacao: {estafeta_obj.localizacao}")
                reply = input("pretende desenhar um dos grafos(sim ou nao):")
                if reply == "sim":
                    g.desenha()
                print("\n")
        elif saida == 11:
            entregaNova, dist = adiciona_entrega(g, "DFS")
            atribui_estafeta(entregaNova, estafetas_loaded, dist)
            l = input("prima enter para continuar")
        else:
            print("opcao invalida")
            l = input("prima enter para continuar")


if __name__ == "__main__":
    main()
