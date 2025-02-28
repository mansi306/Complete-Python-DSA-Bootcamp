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


def has_cycle(head):
    slow,fast = head,head 
    while(fast!=None and fast.next!=None):
        slow = slow.next 
        fast = fast.next.next 
        if slow==fast:
            return True 
    return False 

head = createLLfromList([3, 2, 0, -4])
printLL(head)
head1 = has_cycle(head)
print(head1)
    