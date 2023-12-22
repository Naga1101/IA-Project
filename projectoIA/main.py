from funcoesAux import *
from estafeta import *
from Grafo import Graph

def main():
    data_filename = 'Dados.json'  # Replace with your actual file name
    estafetas_loaded = load_Estafetas(data_filename)
    
    entregaTeste1 = Entrega(127, 'rua Rui Tijjy', 'Cepoes', 4, 9, '2023-8-16 17h')
    entregaTeste2 = Entrega(898, 'rua do moina', 'Barrio', 26, 33, '2024-3-30 16h')
    
    g = Graph()

    g.add_edge("centro de distribuicao", "rua Diogo Barros", 15)
    g.add_edge("rua Diogo Barros", "rua da moita", 15)
    g.add_edge("rua da moita", "rua do chifre", 41)
    g.add_edge("rua do chifre", "rua sesamo", 20)
    g.add_edge("rua sesamo", "rua Guilherme Rego", 13)
    g.add_edge("rua Guilherme Rego", "rua Brandi Love", 50)
    g.add_edge("rua Brandi Love", "rua Rui Tijjy", 50)
    g.add_edge("rua Rui Tijjy", "rua Diogo Barros", 90)
    g.add_edge("rua Rui Tijjy", "rua do moina", 35)
    g.add_edge("rua do moina", "rua insana", 27)
    g.add_edge("rua insana", "rua do 1hifre", 25)
    g.add_edge("rua insana", "rua do pirex", 33)
    g.add_edge("rua do pirex", "rua Guilherme Rego", 16)

    g.add_heuristica("centro de distribuicao", 0)
    g.add_heuristica("rua Diogo Barros", 69)
    g.add_heuristica("rua da moita", 55)
    g.add_heuristica("rua do chifre", 125)
    g.add_heuristica("rua sesamo", 30)
    g.add_heuristica("rua Guilherme Rego", 45)
    g.add_heuristica("rua Brandi Love", 143)
    g.add_heuristica("rua Rui Tijjy", 50)
    g.add_heuristica("rua do moina", 18)
    g.add_heuristica("rua insana", 70)
    g.add_heuristica("rua do pirex", 134)
    g.add_heuristica("rua Guilherme Rego", 171)
    1
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
