'''
House Robbers

Asked in Companies:

Dell
Quickr
Amazon
Ola

Description:
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. The only constraint stopping you from robbing each of them is that adjacent houses have security systems connected, and it will automatically contact the police if two adjacent houses are broken into on the same night.

Given an integer array nums representing the amount of money at each house, return the maximum amount of money you can rob tonight without alerting the police.

Input Parameters:

nums (List[int]): An array representing the amount of money in each house.

Output:

Return an integer representing the maximum amount of money you can rob without triggering the alarm.

Example:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total money robbed = 1 + 3 = 4.
 
 
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9), and rob house 5 (money = 1).
             Total money robbed = 2 + 9 + 1 = 12.

'''

def rob(nums):

    n = len(nums)
    
    # Base cases for when there are no houses or only one house
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
 
    # Create a dp array to store the maximum money that can be robbed up to each house
    dp = [0] * n
    dp[0] = nums[0]  # Rob the first house
    dp[1] = max(nums[0], nums[1])  # Choose between the first and second house
    
    # Iterate over the rest of the houses
    for i in range(2, n):
        # For each house, choose between skipping it (dp[i-1]) or robbing it (dp[i-2] + nums[i])
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
    
    # The last element in dp will have the maximum profit
    return dp[-1]
 
# Helper function to display the result for debugging
def display_rob_result(nums):
    print(rob(nums))
 

print(rob([1, 2, 3, 1]))
