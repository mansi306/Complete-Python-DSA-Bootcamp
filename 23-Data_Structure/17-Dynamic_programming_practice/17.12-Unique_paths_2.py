'''
Unique Paths II

Description:

You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.
Parameters:

grid (List[List[int]]): An m x n grid where grid[i][j] is either 0 (open space) or 1 (obstacle).



Return Values:

int: The number of possible unique paths from the top-left corner to the bottom-right corner avoiding obstacles.

Example:

Input: grid = [[0,0,0],[0,1,0],[0,0,0]] 
Output: 2 
Explanation: There are 2 unique paths from the top-left to the bottom-right corner.
 
Input: grid = [[0,1,0],[0,0,0],[0,0,0]] 
Output: 3
Explanation: There are 3 unique path from the top-left to the bottom-right corner.

'''
def uniquePathsWithObstacles(grid):
    """
    Returns the number of unique paths from the top-left corner to the bottom-right corner of an m x n grid
    considering obstacles where grid[i][j] = 1 indicates an obstacle and grid[i][j] = 0 indicates an open space.
    """
    m = len(grid)
    n = len(grid[0])
    
    # If starting or ending cell has an obstacle, no path is possible
    if grid[0][0] == 1 or grid[m-1][n-1] == 1:
        return 0
    
    # Create a 2D list initialized to 0
    dp = [[0] * n for _ in range(m)]
    
    # Initialize the starting point
    dp[0][0] = 1
    
    # Initialize first row
    for j in range(1, n):
        if grid[0][j] == 0:
            dp[0][j] = dp[0][j - 1]
    
    # Initialize first column
    for i in range(1, m):
        if grid[i][0] == 0:
            dp[i][0] = dp[i - 1][0]
    
    # Fill the dp array
    for i in range(1, m):
        for j in range(1, n):
            if grid[i][j] == 0:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    
    return dp[-1][-1]

grid = [[0,1,0],[0,0,0],[0,0,0]] 
print(uniquePathsWithObstacles(grid))