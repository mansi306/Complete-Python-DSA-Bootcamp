'''
Greatest Number Product
Asked in Companies:

Linkedin

Amazon



Description:
You are given an array ARR of integers. Your task is to find the greatest number in the array such that this number is also equal to the product of two different elements from the same array.



Input Parameters:

ARR (List[int]): A list of integers.

Output:

An integer which is the greatest number that is also the product of two different elements in the array. If no such number exists, return -1.



Example:

Input: ARR = [1, 2, 3, 6, 12]
Output: 12
Explanation: The number 12 is present in the array and it is the product of 2 and 6.
 
Input: ARR = [4, 2, 3, 8]
Output: 8
Explanation: The number 8 is present in the array and it is the product of 2 and 4.
'''


def greatest_product_equal_to_element(arr):
    """
    Function to find the greatest number in the array that is equal to the product of two different elements.
    
    :param arr: List[int] -> The input list of integers
    :return: int -> The greatest number in the array that is equal to the product of two different elements
    """
    # TODO: Implement the logic using a hashmap approach
    arr.sort 
    num_set = set(arr)
    for i in range(len(arr)-1,-1,-1):
        current_num = arr[i]
        for j in range(i):
            if arr[j]==0:
                continue
            if current_num % arr[j]==0:
                other_factor = current_num // arr[j]
            if other_factor in num_set and other_factor!=arr[j]:
                return current_num
    return -1 

ARR = [1, 2, 3, 6, 12]
print(greatest_product_equal_to_element(ARR))