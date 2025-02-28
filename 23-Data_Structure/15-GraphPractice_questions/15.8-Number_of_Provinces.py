'''
Number of Provinces

Asked in Companies:

Quickr
Goldman Sachs
PhonePe
Expedia

Description:
You are given n cities, represented by an n x n matrix isConnected, where isConnected[i][j] = 1 if the i-th city and j-th city are directly connected, and isConnected[i][j] = 0 otherwise. A province is defined as a group of cities that are directly or indirectly connected. Your task is to determine the number of provinces (groups of connected cities).

A province consists of cities that are connected directly or through a series of connections between other cities. No city outside of this group is connected to the cities within the group.

Input Parameters:

isConnected (List[List[int]]): A matrix where isConnected[i][j] = 1 means the i-th city is directly connected to the j-th city, and isConnected[i][j] = 0 means they are not.

Output:

Return the total number of provinces.

Example:

Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Explanation: The first two cities are connected, and the third city forms a separate province.
 
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
Explanation: Each city is its own province, as there are no connections between cities.
'''

def find_circle_num(is_connected):
    """
    Function to find the number of provinces (connected components) in a graph.
    
    :param is_connected: List[List[int]] -> Matrix representing the city connections
    :return: int -> The number of provinces
    """
    def dfs(city, visited, is_connected):
        """
        Helper function to perform DFS on the city and mark all connected cities as visited.
        """
        visited[city] = True
        for neighbor in range(len(is_connected)):
            if is_connected[city][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor, visited, is_connected)
 
    n = len(is_connected)
    visited = [False] * n
    province_count = 0
 
    for city in range(n):
        if not visited[city]:
            # Start a DFS to visit all cities in this province
            dfs(city, visited, is_connected)
            province_count += 1
    
    return province_count
 

print(find_circle_num([[1,1,0],[1,1,0],[0,0,1]])) 
