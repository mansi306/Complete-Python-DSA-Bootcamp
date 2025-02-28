'''
Count Even Odd

Asked in Companies:

Walmart
Adobe
Paypal

Description:
You are given an array ARR of integers of size N. Your task is to determine the following:
The number of elements that occur an odd number of times in the array.
The number of elements that occur an even number of times in the array.
Your solution should make use of a hashmap (Python dictionary) to track the count of each element.

Input Parameters:
ARR (List[int]): A list of integers.
N (int): The size of the array.
Output:
A tuple with two integers:
The first integer is the count of elements that occur an odd number of times.
The second integer is the count of elements that occur an even number of times.

Example:
Input: ARR = [1, 2, 3, 2, 3, 3]
Output: (1, 2)
Explanation: 
- 1 occurs 1 time (odd), 2 occurs 2 times (even), 3 occurs 3 times (odd)
- Number of elements occurring odd times = 2 (1, 3)
- Number of elements occurring even times = 1 (2)
 
 
Input: ARR = [5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 7]
Output: (1, 2)
Explanation:
- 5 occurs 6 times (even), 6 occurs 4 times (even), 7 occurs 1 time (odd)
- Number of elements occurring odd times = 1 (7)
- Number of elements occurring even times = 2 (5, 6)
'''

def count_even_odd(arr):
    # Step 1: Use a dictionary to count the frequency of each element
    frequency_map = {}
    for num in arr:
        if num in frequency_map:
            frequency_map[num] += 1
        else:
            frequency_map[num] = 1

    # Step 2: Count the number of elements with odd and even frequencies
    odd_count = 0
    even_count = 0
    for count in frequency_map.values():
        if count % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    # Step 3: Return the counts as a tuple
    return (odd_count, even_count)

# Example usage
arr1 = [1, 2, 3, 2, 3, 3]
print(count_even_odd(arr1))  # Output: (2, 1)

arr2 = [5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 7]
print(count_even_odd(arr2))  # Output: (1, 2)