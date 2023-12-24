# Classe nodo para definiçao dos nodos
# cada nodo tem um nome, um id e coordenadas
class Node:
    def __init__(self, name, coord, id=-1):
        self.m_id = id
        self.m_name = str(name)
        self.m_coord = coord


    def __str__(self):
        return "node " + self.m_name

    def setId(self, id):
        self.m_id = id

    def getId(self):
        return self.m_id

    def getName(self):
        return self.m_name

    def getCoord(self):
        return self.m_coord

    def __eq__(self, other):
        return self.m_name == other.m_name

    def __hash__(self):
        return hash(self.m_name)