'''
Number of Complete Components
Asked in Companies:

Justpay
Morgan stanley
Google
Microsoft



Description

You are given an undirected graph with n vertices, numbered from 0 to n - 1. The graph is represented by a 2D integer array edges, where edges[i] = [ai, bi] denotes that there is an undirected edge between vertices ai and bi.

Your task is to find how many complete connected components the graph contains.

A connected component is a subgraph where:

There is a path between any two vertices within the subgraph.

No vertex in the subgraph shares an edge with a vertex outside of the subgraph.

A connected component is said to be complete if there is an edge between every pair of vertices in the connected component.



Input:

n: An integer representing the number of vertices in the graph.

edges: A 2D list representing the edges between vertices.

Output:

Return the number of complete connected components in the graph.



Examples:

Input:
n = 6
edges = [[0, 1], [0, 2], [1, 2], [3, 4]]
 
Output:
1
 
Explanation:
- The graph has two connected components: 
  1. {0, 1, 2} which forms a complete connected component.
  2. {3, 4} which is not complete as there is no edge between node 3 and node 4.
- Hence, the number of complete connected components is 1.
 
 
Input:
n = 4
edges = [[0, 1], [2, 3]]
 
Output:
0
 
Explanation:
- There are two connected components: {0, 1} and {2, 3}, but neither is complete.
- Hence, the output is 0.
'''

from collections import defaultdict, deque
def count_complete_components(n, edges):
    # Core logic for the learner to implement
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    visited = [False] * n
    complete_count = 0
    
    def is_complete_component(vertices):
        # A complete graph with k vertices has k*(k-1)/2 edges
        k = len(vertices)
        required_edges = k * (k - 1) // 2
        actual_edges = 0
        
        for u in vertices:
            actual_edges += len(adj[u])
        
        # Since each edge is counted twice in undirected graph
        actual_edges = actual_edges // 2
        
        return actual_edges == required_edges
    
    for i in range(n):
        if not visited[i]:
            # BFS to find all vertices in the current connected component
            queue = deque()
            queue.append(i)
            visited[i] = True
            component = []
            
            while queue:
                node = queue.popleft()
                component.append(node)
                
                for neighbor in adj[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
            
            # Check if the component is complete
            if is_complete_component(component):
                complete_count += 1
    
    return complete_count


print(count_complete_components(6, [[0, 1], [0, 2], [1, 2], [3, 4]]))