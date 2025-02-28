'''
Graph using Edge List
Graph Implementation using Edge List

You are given a task to implement a simple graph using the Edge List representation in Python. The graph will support adding vertices and edges between them. Your task is to create a class GraphUsingEdgeList that represents the graph with the following operations:

Instructions:

add_vertex(vertex): Adds a vertex to the graph. If the vertex already exists, print a message indicating it already exists.

add_edge(source, destination, weight): Adds an edge between two vertices with an optional weight (default is 1). If either vertex is not found in the graph, print a message.

display(): Displays the list of vertices and edges in the graph. Each edge is printed in the form source ---> destination.

Parameters:

The graph consists of a list of vertices (V) and a list of edges (edges). Each edge is a tuple consisting of (source, destination, weight).

You need to implement the three functions as described.

Example:

Adding vertices and edges

graph = GraphUsingEdgeList()
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
 
graph.add_edge(1, 2)
graph.add_edge(2, 3)
 
graph.display()
Output:

Vertices:
Vertex: 1
Vertex: 2
Vertex: 3
Edges:
1 ---> 2
2 ---> 3
Edge case when vertices do not exist:

graph.add_edge(4, 5)
Output:

One or both the vertices are not found
'''




class GraphUsingEdgeList:
    #  creating constructor 
    def __init__(self):
        self.v = []
        self.edges = []
    
    def add_vertex(self,vertex):
        if vertex not in self.v:
            self.v.append(vertex)
        else:
            print(f"{vertex} is already Exist")
    
    def add_edges(self,source,destination,weight=1):
        if source in self.v and destination in self.v :
            edge = (source,destination,weight)
            self.edges.append(edge)
        else:
            print("One or two vertices are not found ")
    
    def display(self):
        print("vertices")
        for vertex in self.v:
            print(f"vertex : {vertex}")
        
        for source,destination,weight in self.edges:
            print(f"Source : {source} ---> Destination : {destination}")


graph = GraphUsingEdgeList()
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)
graph.add_edges(1,4)
graph.add_edges(4,3)
graph.add_edges(3,2)
graph.add_edges(2,1)
print(graph.display())
