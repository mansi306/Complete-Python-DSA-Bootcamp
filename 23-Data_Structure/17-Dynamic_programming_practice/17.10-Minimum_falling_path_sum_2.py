'''
Minimum Falling Path Sum II

Asked in companies:

Apple
Codenation
Google
Arcesium

Description:
Given an n×nn \times nn×n integer matrix grid, return the minimum sum of a falling path with non-zero shifts. A falling path with non-zero shifts is a choice of exactly one element from each row of grid such that no two elements chosen in adjacent rows are in the same column.
Parameters:

grid (List[List[int]]): A 2D list where each inner list represents a row of the matrix.

Return Values:

int: The minimum sum of a falling path with non-zero shifts.

Example:

Input: grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 
Output: 13 
Explanation: The minimum falling path sum with non-zero shifts is 1 → 5 → 7 with a total sum of 13.
 
Input: grid = [[5, 1, 3], [2, 4, 6], [7, 8, 9]] 
Output: 11
Explanation: The minimum falling path sum with non-zero shifts is 1 → 4 → 9 with a total sum of 15.

'''

def minFallingPathSum(grid):
    """
    Find the minimum sum of a falling path with non-zero shifts.
    """
    n = len(grid)
    
    # Initialize dp array
    dp = [[float('inf')] * n for _ in range(n)]
    
    # Initialize the first row of dp with the first row of the grid
    for j in range(n):
        dp[0][j] = grid[0][j]
    
    # Process each row from the second row to the last
    for i in range(1, n):
        # Find the minimum and second minimum values in the previous row
        min1, min2 = float('inf'), float('inf')
        min1_index = -1
        for j in range(n):
            if dp[i-1][j] < min1:
                min2 = min1
                min1 = dp[i-1][j]
                min1_index = j
            elif dp[i-1][j] < min2:
                min2 = dp[i-1][j]
        
        # Update the dp values for the current row
        for j in range(n):
            if j == min1_index:
                dp[i][j] = grid[i][j] + min2
            else:
                dp[i][j] = grid[i][j] + min1
    
    # The result is the minimum value in the last row of dp
    return min(dp[-1])


grid = [[5, 1, 3], [2, 4, 6], [7, 8, 9]]
print(minFallingPathSum(grid)) 