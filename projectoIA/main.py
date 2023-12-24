from funcoesAux import *
from estafeta import *
from Grafo import Graph

def main():
    data_filename = 'Dados.json'  # Replace with your actual file name
    estafetas_loaded = load_Estafetas(data_filename)
    
    entregaTeste1 = Entrega(127, 'rua Rui Tijjy', 'Cepoes', 4, 9, '2023-8-16 17h')
    entregaTeste2 = Entrega(898, 'rua do moina', 'Barrio', 26, 33, '2024-3-30 16h')
    
    g = Graph()

    g.add_edge("centro de distribuicao",(0,0), "rua Diogo Barros", (10,15), 15)
    g.add_edge("rua Diogo Barros",(10,15), "rua da moita", (50,60), 10)
    g.add_edge("rua da moita",(50,60), "rua do chifre", (40,15), 20)
    g.add_edge("rua do chifre",(40,15), "rua sesamo", (25,70), 5)
    g.add_edge("rua sesamo",(25,70), "rua Guilherme Rego", (20,0), 13)
    g.add_edge("rua Guilherme Rego",(20,0), "rua Brandi Love", (69,69), 50)
    g.add_edge("rua Brandi Love",(69,69), "rua Rui Tijjy", (10,50), 24)
    g.add_edge("rua Rui Tijjy",(10,50), "rua Diogo Barros", (10,15), 10)
    g.add_edge("rua Rui Tijjy",(10,50), "rua do moina", (0,60), 18)
    g.add_edge("rua do moina",(0,60), "rua insana", (55,40), 33)
    g.add_edge("rua insana",(55,40), "rua do chifre", (40,15), 8)
    g.add_edge("rua insana",(55,40), "rua do pirex", (80,40), 21)
    g.add_edge("rua do pirex",(80,40), "rua das Lolis", (100,100), 69)

    g.add_heuristica("centro de distribuicao", (0,0), 0)
    g.add_heuristica("rua Diogo Barros", (10,15), 2)
    g.add_heuristica("rua da moita", (50,60), 3)
    g.add_heuristica("rua do chifre", (40,15), 4)
    g.add_heuristica("rua sesamo", (25,70), 5)
    g.add_heuristica("rua Guilherme Rego", (20,0), 6)
    g.add_heuristica("rua Brandi Love", (69,69), 7)
    g.add_heuristica("rua Rui Tijjy", (10,50), 8)
    g.add_heuristica("rua do moina", (0,60), 9)
    g.add_heuristica("rua insana", (55,40), 10)
    g.add_heuristica("rua do pirex", (80,40), 11)
    g.add_heuristica("rua das Lolis", (100,100), 12)

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
        print("9-Estafetas")
        print("10-Adicionar Encomenda")
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
            inicio = input("Nodo inicial->")
            fim = input("Nodo final->")
            print(g.procura_DFS(inicio, fim, path=[], visited=set()))
            l = input("prima enter para continuar")
        elif saida == 6:
            inicio = input("Nodo inicial->")
            fim = input("Nodo final->")
            print(g.procura_BFS(inicio, fim))
            l = input("prima enter para continuar")
        elif saida == 7:
            inicio = input("Nodo inicial->")
            fim = input("Nodo final->")
            print(g.procura_aStar(inicio, fim))
            l = input("prima enter para continuar")
        elif saida == 8:
            inicio = input("Nodo inicial->")
            fim = input("Nodo final->")
            print(g.greedy(inicio, fim))
            l = input("prima enter para continuar")
        elif saida == 9:
            for estafeta_obj in estafetas_loaded:
                print(f"Nome: {estafeta_obj.nome}")
                for entrega_obj in estafeta_obj.conjuntoEntregas:
                    print(f"  {entrega_obj}")
                print(f"Carga atual: {estafeta_obj.pesoAtual}")
                print(f"Ranking: {estafeta_obj.ranking}")
                print(f"Meio de Transporte: {estafeta_obj.meioTransporte}")
                print(f"Localizacao: {estafeta_obj.localizacao}")
                print("\n")
                if estafeta_obj.nome == "Luis":
                    terminarEntrega(entregaTeste1, estafeta_obj)
                    terminarEntrega(entregaTeste2, estafeta_obj)
                    print(f"Ranking: {estafeta_obj.listaAvaliacoes} e {estafeta_obj.ranking}")
                    if estafeta_obj.conjuntoEntregas == []:
                        print("Foram concluidas todas as entregas")
                    for entrega_obj in estafeta_obj.conjuntoEntregas:
                        print(f"  {entrega_obj}")
                    print("\n")
        elif saida == 10:
            entregaNova = adiciona_entrega()
            atribui_estafeta(entregaNova, estafetas_loaded)
            l = input("prima enter para continuar")
            
        else:
            print("opcao invalida")
            l = input("prima enter para continuar")


if __name__ == "__main__":
    main()
