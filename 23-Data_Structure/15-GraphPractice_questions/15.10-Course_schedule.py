'''
Course Schedule

Asked in Companies

Uber
Apple
Paytm

Description:

You are required to take 'N' courses labeled from 1 to N to complete your B.Tech degree. However, some courses may have prerequisites. A prerequisite for a course can be represented as a pair [A, B], which means you must take course B before taking course A.

Your task is to determine if it is possible to complete all the courses given the prerequisites. If there are no cyclic dependencies in the course structure, it is possible to finish all the courses; otherwise, it is not.

The problem essentially checks if a directed graph (where courses represent nodes and prerequisites represent edges) is acyclic. If there is no cycle, you can finish the courses, otherwise you cannot.



Input:

N: An integer representing the total number of courses.

prerequisites: A list of pairs, where each pair [A, B] indicates that course B is a prerequisite of course A.

Output:

Return True if it is possible to finish all the courses, otherwise return False.

Example:

Input:
N = 4
prerequisites = [[1, 2], [2, 3], [3, 4]]
 
Output:
True
Explanation:
You can take course 4 first, then course 3, then course 2, and finally course 1.
 
 
Input:
N = 3
prerequisites = [[1, 2], [2, 3], [3, 1]]
 
Output:
False
Explanation:
There is a cycle between courses 1, 2, and 3. Thus, it is impossible to finish all courses.

'''

def can_finish_courses(N, prerequisites):

    from collections import deque, defaultdict
 
    # Step 1: Build graph and indegree array
    graph = defaultdict(list)
    indegree = [0] * (N + 1)
    
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1
 
    # Step 2: Initialize queue with courses having no prerequisites (indegree = 0)
    queue = deque([i for i in range(1, N + 1) if indegree[i] == 0])
    
    visited_courses = 0
    
    # Step 3: Process nodes using Kahn's algorithm (BFS)
    while queue:
        current = queue.popleft()
        visited_courses += 1
        
        # For each neighboring course, reduce the indegree
        for neighbor in graph[current]:
            indegree[neighbor] -= 1
            
            # If indegree becomes 0, add to queue
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    # If we visited all courses, we can finish them all
    return visited_courses == N

N = 4
prerequisites = [[1, 2], [2, 3], [3, 4]]
print(can_finish_courses(N,prerequisites))