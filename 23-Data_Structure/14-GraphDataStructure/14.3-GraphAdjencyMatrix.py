'''
Code : Graph using Adjacency Matrix
Graph Implementation using Adjacency Matrix

You are tasked with implementing a graph using the Adjacency Matrix representation in Python. The graph will support adding vertices and undirected edges between them. Your task is to create a class GraphAdjacencyMatrix that represents the graph with the following operations:

Instructions:

add_vertex(index, label): Adds a vertex with the specified label at the given index. If the index is out of bounds (greater than or equal to the number of vertices), print an error message.

add_edge(source, destination, weight): Adds an undirected edge between two vertices with an optional weight (default is 1). The edge is represented in both directions in the adjacency matrix. If the indices are out of bounds, print an error message.

display(): Displays the graph's vertices with their corresponding labels and prints the adjacency matrix.

Parameters:

The graph consists of a fixed number of vertices (num_vertices) and an adjacency matrix (adj_matrix), where each element represents the weight of the edge between two vertices.

Example:

Adding vertices and edges:

graph = GraphAdjacencyMatrix(3)
graph.add_vertex(0, 'A')
graph.add_vertex(1, 'B')
graph.add_vertex(2, 'C')
 
graph.add_edge(0, 1)
graph.add_edge(1, 2)
 
graph.display()
Output:

Vertex Index: 0, label: A
Vertex Index: 1, label: B
Vertex Index: 2, label: C
[0, 1, 0]
[1, 0, 1]
[0, 1, 0]
Edge case when indices are out of bounds:

graph.add_vertex(3, 'D')
graph.add_edge(0, 5)
Output:

Index OOB
'''
class GraphUsingAdjencyMatrix:
    def __init__(self,num_vertices):
        self.num_vertices = num_vertices
        self.vertices = [None]*num_vertices
        self.adj_matrix = [[0]*num_vertices for i in range(num_vertices)]
    
    def add_vertex(self,index,label):
        if (index>=0 and index<self.num_vertices):
            self.vertices[index]= label
        else:
            print("Index OOB")
        

    def add_edge(self,source,destination,weight=1):
        if (0<=source<self.num_vertices and 0<=destination<self.num_vertices):
            self.adj_matrix[source][destination]= weight 
            self.adj_matrix[destination][source]= weight 
        
    def display(self):
        for index,label in enumerate(self.vertices):
            print(f"Vertex Index {index}:{label}")
        
        for row in self.adj_matrix:
            print(row)

graph = GraphUsingAdjencyMatrix(3)
graph.add_vertex(0,'A')
graph.add_vertex(1,'B')
graph.add_vertex(2,'C')
graph.add_edge(0,1)
graph.add_edge(1,2)
print(graph.display())
