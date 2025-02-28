'''
Minimum cost to climb stairs

Asked in Companies:

Oyo
Squadstack
Byjus



Description:
You are given an integer array cost where cost[i] is the cost of the i-th step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1. Return the minimum cost to reach the top of the floor.

Input Parameters:
cost (List[int]): An array of integers where cost[i] represents the cost of the i-th step. (2 ≤ len(cost) ≤ 1000)
Output:
Return the minimum cost to reach the top of the floor (int).



Example:
Input: cost = [10, 15, 20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
 
 
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: You will start at index 0.
- Climb one step to index 2, pay 1.
- Climb two steps to index 4, pay 1.
- Climb two steps to index 6, pay 1.
- Climb one step to index 7, pay 1.
- Climb two steps to index 9, pay 1.
- Climb one step to reach the top.
'''

def minCostClimbingStairs(cost):
    
    n = len(cost)
    
    # Edge cases for small inputs
    if n == 2:
        return min(cost[0], cost[1])
    
    # DP array to store the minimum cost to reach each step
    dp = [0] * n
    
    # Initializing the base cases
    dp[0] = cost[0]
    dp[1] = cost[1]
    
    # Fill the DP array iteratively for each step from 2 to n-1
    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i-1], dp[i-2])
    
    # The minimum cost to reach the top can come from either the last step or the second last step
    return min(dp[n-1], dp[n-2])
 
# Helper function to display DP array for debugging
def display_dp_array(cost):
    n = len(cost)
    dp = [0] * n
    dp[0] = cost[0]
    dp[1] = cost[1]
    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i-1], dp[i-2])
    print(dp)
 

print(minCostClimbingStairs([10, 15, 20])) 


