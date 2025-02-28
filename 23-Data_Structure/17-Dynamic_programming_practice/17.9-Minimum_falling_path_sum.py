'''
Minimum Falling Path Sum

Asked in companies:

Google
Uber
Zomato
TRC



Description:
Given an n×nn \times nn×n array of integers matrix, return the minimum sum of any falling path through the matrix. A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

Parameters:

matrix (List[List[int]]): A 2D list where each inner list represents a row of the matrix.

Return Values:

int: The minimum sum of any falling path through the matrix.

Example:

Input: matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]] 
Output: 13 
Explanation: The minimum path sum is 2 → 1 → 4 → 6 with a total sum of 13.
 
Input: matrix = [[-19, 57], [-40, -5]] 
Output: -59 
Explanation: The minimum path sum is -19 → -40 → -5 with a total sum of -59.
'''

def minFallingPathSum(matrix):
    """
    Find the minimum sum of any falling path through the matrix.
    """
    n = len(matrix)
    
    # Start from the second to last row and move upwards
    for row in range(n - 2, -1, -1):
        for col in range(n):
            # Initialize the minimum value for the current cell
            min_below = matrix[row + 1][col]
            
            # Check diagonal left
            if col > 0:
                min_below = min(min_below, matrix[row + 1][col - 1])
            
            # Check diagonal right
            if col < n - 1:
                min_below = min(min_below, matrix[row + 1][col + 1])
            
            # Update the current cell with the minimum path sum
            matrix[row][col] += min_below
    
    # The top row now contains the minimum falling path sum
    return min(matrix[0])


matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]] 
print(minFallingPathSum(matrix))