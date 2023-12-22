import datetime
from estafeta import *
from entrega import *
from Grafo import *
from Nodo import *

dataAtual = datetime.datetime.now()

## Adicionar encomenda

def getPrecoPorEntrega(self, entrega, estafeta): #calcula o preço de uma entrega
    if entrega is not None and estafeta is not None:
        self.preco = (entrega.volume * 0.2) + (entrega.peso * 0.3) + (poeEmHoras(entrega.prazo) / 0.3)
        if estafeta.meioTransporte == 'carro' : self.preco * 1.5
        if estafeta.meioTransporte == 'mota' : self.preco * 1.3
        if estafeta.meioTransporte == 'bicicleta' : self.preco * 1.1
    return self.preco

def poeEmHoras(prazo): #calcula em horas o tempo limite para a entrega
    return abs(dataAtual - prazo).total_seconds() / 3600.0

def atribui_estafeta(entrega, estafetas_loaded):
    estafeta_mais_rapido = None
    maiorVelocidade = 0
    for estafeta in estafetas_loaded:
        velocidade = calculaSpeedConsoantePeso(entrega, estafeta)
        if velocidade > maiorVelocidade or estafeta_mais_rapido == None:
            maiorVelocidade = velocidade
            estafeta_mais_rapido = estafeta
    print(f"Nome: {estafeta_mais_rapido.nome}")
    estafeta_mais_rapido.conjuntoEntregas.append(entrega)
    for entrega_obj in estafeta_mais_rapido.conjuntoEntregas:
                    print(f"  {entrega_obj}")
    
        
def calculaSpeedConsoantePeso (entrega, estafeta):
    veiculo = estafeta.meioTransporte
    pesoMax, velocidadeMax = meioTransportes[veiculo]
    soma = estafeta.pesoAtual + int(entrega.peso)
    if soma < pesoMax:
        if veiculo == 'bicicleta': 
            return (velocidadeMax-(soma*0.6))
        elif veiculo == 'mota': 
            return (velocidadeMax-(soma*0.5))
        elif veiculo == 'carro': 
            return (velocidadeMax-(soma*0.1))
    else: 
        print("Excede o peso maximo")
        return -1

### Terminar Encomenda
def terminarEntrega(entrega, estafeta):  #### Feita e a funcionar
    prazo_datetime = datetime.datetime.strptime(entrega.prazo, '%Y-%m-%d %Hh')
    if datetime.datetime.now() > prazo_datetime:
        estafeta.listaAvaliacoes.append(0)
        print("Entrega atrasada! Penalização no ranking.")
    else:
        avaliacaoDoCliente = input("Como avalia a sua experiência? ")
        print("")
        estafeta.listaAvaliacoes.append(int(avaliacaoDoCliente))
    estafeta.remove_entrega(entrega)
    estafeta.atualiza_ranking()
        
        

def fazEntregas (self, estafeta, metodoProcura): #sabendo o metodo, vai percorrendo a lista de entregas, calcula a melhor rota para cada uma e fá-la, até chegar ao fim.
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