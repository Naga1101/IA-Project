import datetime
import json
from entrega import *

dataAtual = datetime.datetime.now()

#meioTransporte 
meioTransportes = {
    'bicicleta': (5, 10),
    'mota': (20, 35),
    'carro': (100, 50)
}

class estafeta:
    def __init__(self, nome, conjuntoEntregas, listaAvaliacoes, meioTransporte, localizacao):
        self.nome = nome
        self.conjuntoEntregas = conjuntoEntregas
        self.listaAvaliacoes = listaAvaliacoes
        self.ranking = sum(listaAvaliacoes)/len(listaAvaliacoes)
        self.pesoAtual = self.total_peso_entregas()
        self.meioTransporte = meioTransporte
        self.localizacao= localizacao
        
    def total_peso_entregas(self):
        total_peso = sum(entrega.peso for entrega in self.conjuntoEntregas)
        return total_peso
    
    def remove_entrega(self, entrega):
        if entrega in self.conjuntoEntregas:
            self.conjuntoEntregas.remove(entrega)
    
    def atualiza_ranking(self):
        self.ranking = sum(self.listaAvaliacoes)/len(self.listaAvaliacoes)
        
      
def load_Estafetas(filename):
    estafetas = []
    with open(filename, 'r') as file:
        data = json.load(file)
        for estafeta_data in data:
            nome, entregas_data, listaAvaliacoes, meioTransporte, localizacao = estafeta_data

            if entregas_data is not None:
                entregas = [Entrega(*entrega_data) for entrega_data in entregas_data]
            else:
                entregas = []

            estafeta_obj = estafeta(nome, entregas, listaAvaliacoes, meioTransporte, localizacao)
            estafetas.append(estafeta_obj)

    return estafetas