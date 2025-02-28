'''
Triangle Array

Asked in companies:

Flipkart
Ola
Toluna

Description:
Given a triangle array, return the minimum path sum from top to bottom. For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

Parameters:

triangle (List[List[int]]): A list of lists where each inner list represents a row in the triangle.

Return Values:

int: The minimum path sum from the top to the bottom of the triangle.

Example:

Input: triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]] 
Output: 11 
Explanation: The path with the minimum sum is 2 → 3 → 5 → 1, which sums to 11.
 
 
Input: triangle = [[-10]] 
Output: -10 
Explanation: There is only one element in the triangle.
'''

def minimumTotal(triangle):
    """
    Find the minimum path sum from top to bottom in a triangle array.
    """
    # Start from the second to last row and move upwards
    for row in range(len(triangle) - 2, -1, -1):
        for col in range(len(triangle[row])):
            # Update the current cell with the minimum path sum from the row below
            triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])
    
    # The top element of the triangle now contains the minimum path sum
    return triangle[0][0]

triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]] 
print(minimumTotal(triangle))