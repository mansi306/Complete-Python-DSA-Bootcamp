class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
    
def createLLfromList(l1):
    head = None
    tail= None
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
    


def is_palindrome(head):
    if (head==None or head.next==None):
            return True

        # Step 1: Find the middle of the linked list
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        # Step 2: Reverse the second half of the list
    prev = None
    while slow !=None:
        next_node = slow.next
        slow.next = prev
        prev = slow
        slow = next_node

        # Step 3: Compare both halves
    left, right = head, prev
    while right:  # Right half may be smaller in odd-length lists
        if left.val != right.val:
            return False
        left = left.next
        right = right.next

    return True


head = createLLfromList([1,4,3,5])
printLL(head)
head1 = is_palindrome(head)
print(head1)