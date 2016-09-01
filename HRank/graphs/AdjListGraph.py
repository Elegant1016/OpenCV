'''
Author : Santosh Kumar
Graph implementation of using the Adjacency List
'''

class Vertex:
    def __init__(self, name, ):
        self.name = name
        self.visited = False
        self.adj = list()

    def __str__(self):
        return str(self.name) + ' connectedTo: ' + str([str(x) for x in self.adj])

    def __len__(self):
        return len(self.adj)

    def getVertexName(self):
        return self.name


class Edge:
    def __init__(self, dest, cost):
        self.Vertex = dest
        self.cost = cost

    def __str__(self):
        return (self.Vertex.name) + "("+ (self.cost)+")"

class Graph:
    def __init__(self):
        self.vertexMap = dict()

    def addEdge(self, sourceName, destName, cost):
        v = self.getVertex(sourceName)
        w = self.getVertex(destName)

        edge = Edge(w, cost)
        v.adj.append(edge)

    def getVertex(self, vertexName ):
        v = self.vertexMap.get(vertexName)
        if v == None:
            v = Vertex(vertexName)
            self.vertexMap[vertexName] = v
        return v

    def printPath(self, dest):
        pass

    def dfs(self, graph, startVertex):
        sv = self.vertexMap.get(startVertex)
        stack = [sv]
        while stack:
            tempVertex = stack.pop()
            print(tempVertex)
            if tempVertex.visited == False:
                tempVertex.visited = True
                for x in tempVertex.adj:
                    stack.append(str(x))


if __name__ =="__main__":
    g = Graph()
    g.addEdge( "0", "1", "2")
    g.addEdge( "0", "3", "1")
    g.addEdge( "1", "4", "10")
    g.addEdge( "1", "3", "3")
    g.addEdge( "2", "0", "4")
    g.addEdge( "2", "5", "5")
    g.addEdge( "3", "4", "2")
    g.addEdge( "3", "6", "4")
    g.addEdge( "3", "5", "8")
    g.addEdge( "3", "2", "2")
    g.addEdge( "4", "6", "6")
    g.addEdge( "6", "5", "1")


    for v in g.vertexMap:
        print(g.vertexMap.get(v))

    g.dfs(g, "0")  # {'E', 'D', 'F', 'A', 'C', 'B'}