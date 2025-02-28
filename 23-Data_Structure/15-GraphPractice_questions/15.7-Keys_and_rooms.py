'''
Keys and Rooms
Asked in Companies:

Paypal
Phonepe
Wells Fargo
Morgan Stanley

Description
You are given n rooms labeled from 0 to n - 1. All rooms are locked except for room 0, and each room contains a set of distinct keys. Each key has a number on it, denoting which room it unlocks, and you can collect and use all the keys in each room you visit.
Your goal is to determine whether you can visit all the rooms, starting from room 0.

Input:

rooms: A list of lists where rooms[i] is a list of keys you can collect in room i.

Output:

Return True if you can visit all the rooms, otherwise return False.

Example:

Input:
rooms = [[1], [2], [3], []]
 
Output:
True
 
Explanation:
- You start in room 0 and collect key 1.
- You move to room 1 and collect key 2.
- You move to room 2 and collect key 3.
- You move to room 3, and all rooms are visited.
 
 
Input:
rooms = [[1, 3], [3, 0, 1], [2], [0]]
 
Output:
False
 
Explanation:
- You start in room 0 and collect keys 1 and 3.
- Room 2 is never visited because you do not have its key.
'''

def can_visit_all_rooms(rooms):
    """
    This function checks if all rooms can be visited starting from room 0.
    It uses BFS or DFS to explore all accessible rooms from room 0.
    """
    # Number of rooms
    n = len(rooms)
    
    # Set to keep track of visited rooms
    visited = set()
    
    # Start by visiting room 0
    def dfs(room):
        # Mark the current room as visited
        visited.add(room)
        
        # Explore all keys (rooms) available in the current room
        for key in rooms[room]:
            if key not in visited:
                dfs(key)
    
    # Start DFS from room 0
    dfs(0)
    
    # If we visited all rooms, the length of visited should be equal to n
    return len(visited) == n


rooms = [[1], [2], [3], []]
print(can_visit_all_rooms(rooms))
 