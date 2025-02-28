'''
Eventual Safe States


Asked in Companies:
De Shaw
Apple
Sharechat
Shipsy



Description:
You are given a directed graph of n nodes labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].

A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).

Your task is to return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.


Input Parameters:

graph (List[List[int]]): Adjacency list representing the directed graph.

Output:

List[int]: A list of safe nodes sorted in ascending order.



Example:

Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
 
Input: graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
Output: [4]

'''

def eventualSafeNodes(graph):
    """
    Function to find all the safe nodes in a directed graph.
    
    :param graph: List[List[int]] -> Adjacency list representing the directed graph
    :return: List[int] -> List of all safe nodes sorted in ascending order
    """
    def dfs(node):
        """
        Helper function for DFS that marks nodes as safe or unsafe.
        """
        if status[node] == 1:  # If already visited and is safe
            return True
        if status[node] == 2:  # If already visited and is unsafe
            return False
        
        status[node] = 2  # Mark as unsafe
        for neighbor in graph[node]:
            if not dfs(neighbor):
                return False
        
        status[node] = 1  # Mark as safe
        return True
    
    n = len(graph)
    status = [0] * n  # 0 = unvisited, 1 = safe, 2 = unsafe
    result = []
    
    for i in range(n):
        if dfs(i):
            result.append(i)
    
    return sorted(result)
 
print(eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]])) 
