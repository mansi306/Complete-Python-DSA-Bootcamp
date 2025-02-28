class GraphAdjencyList:
    def __init__(self):
        self.v = []
        self.adj_list = {}
    
    def add_vertex(self,vertex):
        if vertex not in self.v:
            self.v.append(vertex)
            self.adj_list[vertex] = []
        else:
            print(f"{vertex} is already exists ")
    
    def add_edges(self,source,destination,weight=1):
        if source in self.v and destination in self.v :
            self.adj_list[source].append((destination,weight))
            self.adj_list[destination].append((source,weight))
        else:
            print("both vertices are not found ")
    
    def display(self):
        for vertex in self.v :
            print(f"vertex:{vertex}")
        
        for vertex,neighbor in self.adj_list.items():
            print(f"{vertex}:{neighbor}")


graph = GraphAdjencyList()
# graph.add_vertex('A')
# graph.add_vertex('B')
# graph.add_vertex('C')
# graph.add_vertex('D')
# graph.add_vertex('E')
# graph.add_edges('A','B')
# graph.add_edges('A','D')
# graph.add_edges('B','D')
# graph.add_edges('B','C')
# print(graph.display())
graph.add_vertex(0)
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_edges(0,2)
graph.add_edges(2,3)
graph.add_edges(2,1)
graph.add_edges(3,1)
print(graph.display())
