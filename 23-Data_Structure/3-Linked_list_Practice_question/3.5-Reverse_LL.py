class ListNode:
    def __init__(self,val):
        self.val = val 
        self.next = None 

def reverse_list(head):
    """
    Function to reverse a singly linked list.
    :param head: ListNode -> head of the singly linked list
    :return: ListNode -> the head of the reversed linked list
    """
    # TODO: Implement this function
    prev = None
    temp = head 
    while (temp!=None):
        next_node = temp.next 
        temp.next = prev 
        prev = temp 
        temp = next_node
    return prev


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

def printLL(head):
    temp = head 
    while(temp!=None):
        print(temp.val,end='->')
        temp = temp.next 
    print("None")


# Create Linked List
head = createLLfromList([1, 2, 3, 5, 6])

# Print Original Linked List
print("Original Linked List:")
printLL(head)

# Reverse Linked List
head = reverse_list(head)

# Print Reversed Linked List
print("Reversed Linked List:")
printLL(head)
