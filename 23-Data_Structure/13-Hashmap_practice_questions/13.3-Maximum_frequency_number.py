'''
Maximum Frequency Number
Asked in Companies:

Qualcomm

Accenture

Walmart

Description:
You are given an array of integers where the numbers are in random order. Your task is to write a function to find and return the number that occurs the most times in the given array. If there are two or more numbers with the maximum frequency, return the number that appears first in the array (i.e., the number with the lowest index).

Input Parameters:

arr (List[int]): A list of integers.

Output:

An integer which is the most frequent number in the array. If there are ties, the number that appears first should be returned.
Example:

Input: arr = [1, 3, 2, 2, 1, 1, 4, 5, 1]
Output: 1
Explanation: The number 1 appears the most times (4 times). 
 
Input: arr = [4, 4, 5, 5, 6, 6, 6]
Output: 6
Explanation: The number 6 appears the most times (3 times). Even though 4 and 5 each appear twice, 6 appears more frequently.
'''

def most_frequent_number(arr):
    """
    Function to find and return the number that occurs the most times in the array.
    In case of ties, return the number that appears first in the array.
    
    :param arr: List[int] -> The input list of integers
    :return: int -> The most frequent number in the array
    """
    # TODO: Implement the logic using a hashmap (dictionary)
    frequency = {}
    for i in arr:
        if i in frequency:
            frequency[i]+= 1
        else:
            frequency[i]= 1 
    max_freq = max(frequency.values())
    for i in arr:
        if frequency[i]==max_freq:
            return i 
        
arr = [1, 3, 2, 2, 1, 1, 4, 5, 1]
print(most_frequent_number(arr))