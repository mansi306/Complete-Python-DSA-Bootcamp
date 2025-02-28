'''
Longest Increasing Subsequence

Asked in Companies:

Sharechat
Acko
Facebook

Description:
You are given an integer array nums. Your task is to return the length of the longest strictly increasing subsequence in the array. A subsequence is a sequence that can be derived by deleting some or no elements from the array without changing the order of the remaining elements.

Input Parameters:

nums (List[int]): A list of integers.

Output:

Return an integer representing the length of the longest strictly increasing subsequence.

Example:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4.
 
Input: nums = [7,7,7,7,7,7,7]
Output: 1
 
Input: nums = [0,1,0,3,2,3]
Output: 4
'''

def length_of_lis(nums):
    
    # If the input list is empty, return 0
    if not nums:
        return 0
    
    # Create a dp array where dp[i] will store the length of the LIS ending at index i
    n = len(nums)
    dp = [1] * n  # Initialize dp array with 1 as every element is a subsequence of length 1 by itself
    
    # Iterate over each element and find the LIS ending at each index
    for i in range(1, n):
        for j in range(0, i):
            if nums[i] > nums[j]:  # Check if current element can extend the subsequence ending at nums[j]
                dp[i] = max(dp[i], dp[j] + 1)  
    
    return max(dp)
 

def display_lis_result(nums):
    print(length_of_lis(nums))
 

print(length_of_lis([7,7,7,7,7,7,7])) 
