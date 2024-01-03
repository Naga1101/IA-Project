from funcoesAux import *
from estafeta import *
from Grafo import Graph

def main():
    data_filename = 'Dados.json'
    estafetas_loaded = load_Estafetas(data_filename)

    g = Graph()
    g.parse_file('dados.csv')

    saida = -1
    while saida != 0:
        print("1-Menu Grafos")
        print("2-Realizar Entrega")
        print("3-Testes")
        print("4-Adicionar Encomenda")
        print("0-Saír")

        saida = int(input("introduza a sua opcao-> "))
        if saida == 0:
            print("saindo.......")
            break

        if saida == 1:
            print()
            grafO = -1
            while grafO != 0:
                print("1-Imprimir Grafo")
                print("2-Desenhar Grafo")
                print("3-Imprimir  nodos de Grafo")
                print("4-Imprimir arestas de Grafo")
                print("0-Voltar atrás")
                grafO = int(input("introduza a sua opcao-> "))  
                if grafO == 1:
                    print(g.m_graph)
                    input("prima enter para continuar")
                elif grafO == 2:
                    g.desenha()
                elif grafO == 3:
                    print(g.m_graph.keys())
                    input("prima enter para continuar")
                elif grafO == 4:
                    print(g.imprime_aresta())
                    input("prima enter para continuar")
                elif grafO == 0:
                    print()
                else:
                    print("opcao invalida")
                    input("prima enter para continuar")

        elif saida == 2:
            print()
            realEntr = -1
            while realEntr != 0:
                print("1-DFS")
                print("2-BFS")
                print("3-Custo Uniforme")
                print("4-A*")
                print("5-Gulosa")
                print("0-Voltar atrás")
                realEntr = int(input("introduza a sua opcao-> "))  
                if realEntr == 1:
                    path, total_path = iniciarEntregasDFS(g, estafetas_loaded)
                    printPaths(path)
                    opcao = input("Pretende ver o caminho percorrido pelo algoritmo? S/N\n")
                    if opcao == "S":
                        printPathsTotal(total_path)
                    input("prima enter para continuar")
                elif realEntr == 2:
                    path, total_path = iniciarEntregasBFS(g, estafetas_loaded)

                    printPaths(path)
                    opcao = input("Pretende ver o caminho percorrido pelo algoritmo? S/N\n")
                    if opcao == "S":
                        printPathsTotal(total_path)
                    input("prima enter para continuar")
                elif realEntr == 3:
                    path, total_path = iniciarEntregasCustoUniforme(g, estafetas_loaded)
                    printPaths(path)
                    opcao = input("Pretende ver o caminho percorrido pelo algoritmo? S/N\n")
                    if opcao == "S":
                        printPathsTotal(total_path)
                    input("prima enter para continuar")
                elif realEntr == 4:
                    path, total_path = iniciarEntregaAstar(g, estafetas_loaded)
                    printPaths(path)
                    opcao = input("Pretende ver o caminho percorrido pelo algoritmo? S/N\n")
                    if opcao == "S":
                        printPathsTotal(total_path)
                    input("prima enter para continuar")
                elif realEntr == 5:
                    path, total_path = iniciarEntregaGreedy(g, estafetas_loaded)
                    printPaths(path)
                    opcao = input("Pretende ver o caminho percorrido pelo algoritmo? S/N\n")
                    if opcao == "S":
                        printPathsTotal(total_path)
                    input("prima enter para continuar")  
                elif realEntr == 0:
                    print()
                else:
                    print("opcao invalida")
                    input("prima enter para continuar")

        elif saida == 3:
            print()
            testesInp = -1
            while testesInp != 0:
                print("1-Comparar Algoritmos")
                print("2-Listar Ranking")
                print("3-Imprimir Estafetas")
                print("0-Voltar atrás")
                testesInp = int(input("introduza a sua opcao-> "))  
                if testesInp == 1:
                    DFS_Path, BFS_Path, Greedy_path, aStar_path, UC_path = compareAlgorithms(g, estafetas_loaded)
                    opcao = input("Pretende ver o caminho obtido pelos algoritmos? S/N\n")
                    if opcao == "S":
                        print("Caminho obtido pelo algoritmo DFS")
                        printPathsTotal(DFS_Path)
                        print("Caminho obtido pelo algoritmo BFS")
                        printPathsTotal(BFS_Path)
                        print("Caminho obtido pelo algoritmo Uniform Cost")
                        printPathsTotal(UC_path)
                        print("Caminho obtido pelo algoritmo Greedy")
                        printPathsTotal(Greedy_path)
                        print("Caminho obtido pelo algoritmo aStar")
                        printPathsTotal(aStar_path)
                elif testesInp == 2:
                    print()
                    print("Lista de estafetas baseado no ranking:")
                    listarRanking(estafetas_loaded)
                    print()
                    print("Lista de veículos baseado no ranking:")
                    rankingVeiculos(estafetas_loaded)
                    print()
                    input("prima enter para continuar")
                elif testesInp == 3:
                    for estafeta_obj in estafetas_loaded:
                        print(f"Nome: {estafeta_obj.nome}")
                        for entrega_obj in estafeta_obj.conjuntoEntregas:
                            print(f"  {entrega_obj}")
                        heuristics_dict = calcula_heuristica_entregas(estafeta_obj, g)
                        #print(heuristics_dict)
                        print(f"Carga atual: {estafeta_obj.pesoAtual}")
                        print(f"Ranking: {estafeta_obj.ranking}")
                        print(f"Meio de Transporte: {estafeta_obj.meioTransporte}")
                        reply = input("pretende desenhar um dos grafos(sim ou nao):")
                        if reply == "sim":
                            print(f"Localizacao: {estafeta_obj.localizacao}")
                            g.desenha()
                        print("\n")
                elif testesInp == 0:
                    print()
                else:
                    print("opcao invalida")
                    input("prima enter para continuar")

        elif saida == 4:
            entregaNova, dist = adiciona_entrega(g)
            atribui_estafeta(entregaNova, estafetas_loaded, dist)
            input("prima enter para continuar")

        else:
            print("opcao invalida")
            input("prima enter para continuar")

if __name__ == "__main__":
    main()
