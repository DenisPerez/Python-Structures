class Grafo:
    graph_dict = {}

    visitados = {}
    solucion = []

    def addEdge(self, node, neighbour):
        if node not in self.graph_dict:
            self.graph_dict[node] = [neighbour] ###si el nodo no esta tengo que agregar el elemento a una lista###
        else:
            self.graph_dict[node].append(neighbour) ###Si el nodo ya esta entonces solo agrego el vecino###
        for node in self.graph_dict:
            self.visitados[node] = False

    def show_edges(self):
        print (self.graph_dict)
        for node in self.graph_dict:
            for neighbour in self.graph_dict[node]:
                print("(",node,", ",neighbour,")")


    def find_path(self,start,end,path=[]):
        path = path + [start]
        if start == end:
            return path
        for node in self.graph_dict[start]:
            if node not in path:
                newpath = self.find_path(node,end,path)
                if newpath:
                    return newpath
                return None

    def BFS(self,start):
        visitados = {}
        solucion = []
        for i in self.graph_dict:
            visitados[i] = False
        cola = []
        cola.append(start)
        visitados[start] = True
        while len(cola) != 0:
            start = cola.pop(0)
            for node in self.graph_dict[start]:
                if visitados[node] != True:
                    visitados[node] = True
                    cola.append(node)
            solucion = solucion + [start]
        print(solucion)

    def DFS(self, start):
        print(start)
        self.visitados[start] = True
        for node in self.graph_dict[start]:
            if self.visitados[node] != True:
                self.DFS(node)
        
                
        


g = Grafo()

g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(3,2)
g.addEdge(2,4)
g.addEdge(4,5)
g.addEdge(2,5)
g.addEdge(5,3)
#g.show_edges()
#print(g.find_path(4,1))
#g.BFS(1)
g.DFS(1)