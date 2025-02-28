'''
Climbing Stairs

Asked in Companies:
Infosys
Accenture
Morgan Stanley

Description:
You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 step or 2 steps. In how many distinct ways can you climb to the top?

Input Parameters:
n (int): The total number of steps required to reach the top (1 ≤ n ≤ 45).
Output:
Return the number of distinct ways to reach the top (int).

Example:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
 
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''

def climbStairs(n):
    # If there are 1 or 2 steps, return n (base cases)
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    # Initialize DP array to store the number of ways to reach each step
    dp = [0] * (n + 1)
    
    # Base cases: 1 way to reach step 1, 2 ways to reach step 2
    dp[1] = 1
    dp[2] = 2
    
    # Fill the DP array iteratively from step 3 to n
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    # Return the number of ways to reach the nth step
    return dp[n]
 
# Helper function to display the DP array for debugging (optional)
def display_dp_array(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    if n > 1:
        dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    print(dp)
 

print(climbStairs(10))
