'''
Number of Operations to make Graph Connected

Description:
You are given a network of n computers numbered from 0 to n - 1 connected by ethernet cables. Each connection is represented as an edge between two nodes. You can extract certain cables and place them between any pair of disconnected computers to make them directly connected.

Parameters:

n (int): The number of computers.

connections (List[List[int]]): A list of connections where each connection is represented by a pair [ai, bi] indicating a direct connection between computers ai and bi.

Return Values:

int: The minimum number of operations required to make all computers connected. If it is not possible, return -1.

Example:

Input: n = 5, connections = [[0,1],[1,2],[2,3],[3,4]] 
Output: 0
Explanation: All computers are already connected.
 
 
Input: n = 6, connections = [[0,1],[0,2],[1,2],[3,4]] 
Output: -1 
Explanation: It is impossible to connect all computers.

'''

from collections import deque, defaultdict
 
def minOperationsToConnectComputers(n, connections):
    """
    Returns the minimum number of operations required to connect all computers in the network.
    If it is not possible, return -1.
    """
    if len(connections) < n - 1:
        return -1
    
    # Build the graph
    graph = defaultdict(list)
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)
    
    # Helper function for BFS to find all nodes in a component
    def bfs(start_node, visited):
        queue = deque([start_node])
        visited.add(start_node)
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
 
    visited = set()
    num_components = 0
    
    # Perform BFS from each unvisited node to count connected components
    for i in range(n):
        if i not in visited:
            bfs(i, visited)
            num_components += 1
 
    # The number of operations needed is the number of components minus one
    return num_components - 1

n = 6
connections = [[0,1],[0,2],[1,2],[3,4]] 
print(minOperationsToConnectComputers(n,connections))