'''
Number of Unreachable Nodes
Asken in Companies:

Directi

Amazon

Synopsys



Description:

You are given an undirected graph with n nodes, numbered from 0 to n - 1. The graph is represented by a 2D integer array edges, where edges[i] = [ai, bi] denotes an undirected edge between the nodes ai and bi.

Your task is to return the number of pairs of different nodes that are unreachable from each other. A pair (i, j) is considered unreachable if there is no path from node i to node j.



Input:

n: An integer representing the number of nodes.

edges: A 2D list of integer pairs representing the edges between nodes.

Output:

Return the number of unreachable pairs of nodes.



Example:

Input:
n = 5
edges = [[0, 1], [0, 2], [3, 4]]
 
Output:
6
 
Explanation:
- The graph has two connected components: {0, 1, 2} and {3, 4}.
- Unreachable pairs are: (0, 3), (0, 4), (1, 3), (1, 4), (2, 3), (2, 4).
- Hence, the output is 6.
 
 
Input:
n = 7
edges = [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]]
 
Output:
14
 
Explanation:
- The graph has two connected components: {0, 2, 4, 5} and {1, 6}.
- Unreachable pairs are: (0, 1), (0, 6), (2, 1), (2, 6), (4, 1), (4, 6), (5, 1), (5, 6).
- Hence, the output is 14.



'''

from collections import defaultdict, deque
def count_unreachable_pairs(n, edges):
    graph = defaultdict(list)
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False]*n 
    component = []
    for node in range(n):
        if not visited[node]:
            queue = deque([node])
            visited[node]=True 
            component_size = 0 
            while queue:
                current_node = queue.popleft()
                component_size+=1
                for neighbor in graph[current_node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True 
                        queue.append(neighbor)
            component.append(component_size)
    total_pairs = 0 
    total_nodes = 0 
    for size in component:
        total_pairs += total_nodes * size
        total_nodes += size
    
    return total_pairs

n = 7
edges = [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]]
print(count_unreachable_pairs(n,edges))
