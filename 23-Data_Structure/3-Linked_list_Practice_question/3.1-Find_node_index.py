'''
Find the Node Index in Linked List
Asked in Companies:

Amazon

Google

Microsoft

Uber

Description:
You are given the head of a singly linked list and an integer k. Your task is to find the index of the first node in the linked list whose value equals k. If no such node exists, return -1.

The index starts at 0 for the head of the list.

Input Parameters:

head (ListNode): The head node of the singly linked list.

k (int): The value you are looking for in the linked list.

Output:

An integer representing the index of the node where the node's value is equal to k. If no such node exists, return -1.

Example:
Input: head = [1 -> 2 -> 3 -> 4], k = 3
Output: 2
 
Input: head = [1 -> 2 -> 3 -> 4], k = 5
Output: -1
 
Input: head = [], k = 3
Output: -1
'''

class listNode:
    def __init__(self,val):
        self.val = val
        self.next = None

def Find_index(head,k):
    temp = head 
    index = 0 
    while (temp!=None):
        if (temp.val==k):
            return index 
        temp = temp.next 
        index+=1
    return -1 
    
def createLLfromList(l1):
    head = None
    tail = None
    for val in l1:
        newNode = listNode(val)
        if (head==None):
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
    return head 


# def count_length(head):
#     temp = head 
#     count = 0
#     while(temp!=None):
#         temp = temp.next 
#         count+=1
#     return count 


# def display_find_index(head,k):
#     result = Find_index(head,k)
#     print(f"The index of Node of value {k}  of the Linked List  is {result}")


def print_linked_list(head):
    temp = head
    while temp:
        print(temp.val, end=" -> ")
        temp = temp.next
    print("None")



# def find_middle(head):
#     if (head==None or head.next==None):
#         return head 
#     length = count_length(head)
#     middle = length//2
#     index = 0 
#     temp = head 
#     while(index<middle):
#         temp = temp.next 
#         index+=1
#     return temp


head = createLLfromList([1,2,3,4,5,7])
print_linked_list(head)

result1 = Find_index(head, 5)
  # This will correctly print: 4
print(result1)

