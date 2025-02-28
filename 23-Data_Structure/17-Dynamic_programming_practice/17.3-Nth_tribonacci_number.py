'''
Nth Tribonacci Number

Asked in Companies:
Walmart
TCS
Myntra

Description:
The Tribonacci sequence is defined as follows:

T0 = 0
T1 = 1
T2 = 1
For n >= 0, Tn+3 = Tn + Tn+1 + Tn+2

Given an integer n, return the value of Tn. Use a dynamic programming approach to optimize the solution.

Input Parameters:

n (int): The index of the Tribonacci sequence to compute (0 ≤ n ≤ 37).

Output:

Return the value of Tn (int).

Example:

Input: n = 4
Output: 4
Explanation: T_3 = 0 + 1 + 1 = 2, T_4 = 1 + 1 + 2 = 4
 
Input: n = 25
Output: 1389537
'''

def tribonacci(n):
    """
    Function to calculate the nth Tribonacci number using dynamic programming.
    
    :param n: int -> The index of the Tribonacci sequence
    :return: int -> The nth Tribonacci number
    """
    # Base cases for small values of n
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    
    # Initialize a DP array to store the Tribonacci numbers
    dp = [0] * (n + 1)
    
    # Set the initial values for the first three numbers
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1
    
    # Fill the DP array iteratively
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    
    # Return the nth Tribonacci number
    return dp[n]
 
# Helper function to display DP array for debugging (optional)
def display_tribonacci_sequence(n):
    dp = [tribonacci(i) for i in range(n + 1)]
    print(dp)
 

print(tribonacci(25))  
