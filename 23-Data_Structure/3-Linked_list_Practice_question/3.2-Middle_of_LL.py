'''
Middle of the Linked list
Asked in Companies:
Amazon
Microsoft
Google
Facebook

Description:
Given the head of a singly linked list, write a function to return the middle node of the linked list. If there are two middle nodes, return the second middle node.

Input Parameters:
head (ListNode): The head node of the singly linked list.
Output:
The middle node of the linked list.
Example:
Input: head = [1 -> 2 -> 3 -> 4 -> 5]
Output: 3
Input: head = [1 -> 2 -> 3 -> 4 -> 5 -> 6]
Output: 4
Input: head = [1]
Output: 1

'''

class ListNode:
    def __init__(self,val):
        self.val = val 
        self.next = None 

def find_middle(head):
    slow = head 
    fast = head 
    while (fast!=None and fast.next !=None):
        slow = slow.next 
        fast = fast.next.next 
    return slow


def createLLfromList(l1):
    head = None
    tail = None
    for val in l1:
        newNode = ListNode(val)
        if (head==None):
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
    return head 

def display_middle(head):
    result = find_middle(head)
    if result:
        print(f"Middle Node of the Linked list is {result.val}")
    else:
        print("Linked list is empty.")



def printLL(head):
    temp = head 
    while(temp!=None):
        print(temp.val,end='->')
        temp = temp.next 
    print("None")


head = createLLfromList([1,2,3,4])
printLL(head)
display_middle(head)


# createLLfromList(head)
# display_middle(head)
