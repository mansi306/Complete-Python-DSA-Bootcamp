class ListNode:
    def __init__(self,val):
        self.val = val 
        self.next = None
    
def remove_duplicate(head):
    temp = head 
    while(temp!=None and temp.next !=None):
        if (temp.val == temp.next.val):
            temp.next = temp.next.next 
        else:
            temp = temp.next 
    return head 

def createLL(lst):
    if (lst==None):
        return None
    head = ListNode(lst[0])
    temp = head 
    for val in lst[1:]:
        temp.next = ListNode(val)
        temp = temp.next 
    return head 

def Print_linked_list(head):
    temp = head 
    while(temp!=None):
        print(temp.val,end='->')
        temp= temp.next 
    print("None")

test_cases = [
    [1, 1, 2, 3, 3],
    [1, 1, 1, 2, 3],
    [1, 2, 3]
]

for i, test in enumerate(test_cases, 1):
    head = createLL(test)
    print(f"Test Case {i}: Original List:")
    Print_linked_list(head)

    new_head = remove_duplicate(head)
    print(f"Test Case {i}: Modified List:")
    Print_linked_list(new_head)
    print("-" * 30)