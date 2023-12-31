from funcoesAux import *
from estafeta import *
from Grafo import Graph

def main():
    data_filename = 'Dados.json'
    estafetas_loaded = load_Estafetas(data_filename)

    g = Graph()
    g.parse_file('teste.csv')

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
        print("12-Listar Ranking")
        print("0-Saír")

        saida = int(input("introduza a sua opcao-> "))
        if saida == 0:
            print("saindo.......")

        elif saida == 1:
            print(g.m_graph)
            input("prima enter para continuar")

        elif saida == 2:
            g.desenha()
        elif saida == 3:
            print(g.m_graph.keys())
            input("prima enter para continuar")

        elif saida == 4:
            print(g.imprime_aresta())
            input("prima enter para continuar")

        elif saida == 5:
            print("1-Realizar Entregas")
            print("2-Adicionar Entrega")
            inp = int(input("introduza a sua opcao-> "))
            if inp == 1:
                path, total_path = iniciarEntregasDFS(g, estafetas_loaded)
                printPaths(path)
                opcao = input("Pretende ver o caminho percorrido pelo algoritmo? S/N\n")
                if opcao == "S":
                    printPathsTotal(total_path)
            else:
                entregaNova, dist = adiciona_entrega(g, "DFS")
                atribui_estafeta(entregaNova, estafetas_loaded, dist)
            input("prima enter para continuar")

        elif saida == 6:
            path, total_path = iniciarEntregasBFS(g, estafetas_loaded)

            printPaths(path)
            opcao = input("Pretende ver o caminho percorrido pelo algoritmo? S/N\n")
            if opcao == "S":
                printPathsTotal(total_path)
            input("prima enter para continuar")

        elif saida == 7:
            path, total_path = iniciarEntregaAstar(g, estafetas_loaded)
            printPaths(path)
            opcao = input("Pretende ver o caminho percorrido pelo algoritmo? S/N\n")
            if opcao == "S":
                printPathsTotal(total_path)

            #path = iniciarEntregaAstar(g, estafetas_loaded)
            #print(path)
            input("prima enter para continuar")

        elif saida == 8:
            path, total_path = iniciarEntregaGreedy(g, estafetas_loaded)
            printPaths(path)
            opcao = input("Pretende ver o caminho percorrido pelo algoritmo? S/N\n")
            if opcao == "S":
                printPathsTotal(total_path)
            input("prima enter para continuar")

        elif saida == 9:
            DFS_Path, BFS_Path, Greedy_path, aStar_path = compareAlgorithms(g, estafetas_loaded)
            opcao = input("Pretende ver o caminho obtido pelos algoritmos? S/N\n")
            if opcao == "S":
                print("Caminho obtido pelo algoritmo DFS")
                printPathsTotal(DFS_Path)
                print("Caminho obtido pelo algoritmo BFS")
                printPathsTotal(BFS_Path)
                print("Caminho obtido pelo algoritmo Greedy")
                printPathsTotal(Greedy_path)
                print("Caminho obtido pelo algoritmo aStar")
                printPathsTotal(aStar_path)

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
            input("prima enter para continuar")

        elif saida == 12:
            listarRanking(estafetas_loaded)
            input("prima enter para continuar")
        else:
            print("opcao invalida")
            input("prima enter para continuar")


if __name__ == "__main__":
    main()
