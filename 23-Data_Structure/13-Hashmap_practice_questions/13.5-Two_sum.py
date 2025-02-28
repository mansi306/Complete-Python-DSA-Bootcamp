'''
Two Sum
Asked in Companies:

Thales

Oracle

Natwest Group

Delhivery

Description:
You are given an array of integers nums and an integer target. Your task is to find two distinct indices in the array such that the sum of the elements at these indices equals the given target. You must return the indices in a list, and you can assume that each input has exactly one solution. You may not use the same element twice.

Input Parameters:

nums (List[int]): A list of integers.

target (int): The target sum that two distinct numbers in the list should add up to.

Output:

A list of two integers representing the indices of the two numbers that add up to the target.

Example:

Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
 
Input: nums = [3, 2, 4], target = 6
Output: [1, 2]
Explanation: Because nums[1] + nums[2] == 6, we return [1, 2].
'''

def two_sum(nums, target):
    """
    Function to return indices of the two numbers such that they add up to the target.
    
    :param nums: List[int] -> The input list of integers
    :param target: int -> The target sum
    :return: List[int] -> A list of two indices whose corresponding elements add up to the target
    """
    # TODO: Implement the logic using a hashmap (dictionary)
    num_to_index = {}
    for i , num in enumerate(nums):
        complement = target- num 
        if complement in num_to_index:
            return [num_to_index[complement],i]
        num_to_index[num]= i 
    return []
nums = [3, 2, 4]
target = 6
print(two_sum(nums,target))
