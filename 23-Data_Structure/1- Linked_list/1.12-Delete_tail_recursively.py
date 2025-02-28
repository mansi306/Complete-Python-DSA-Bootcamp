from Common_ll import Node, take_input,Printlist

def delete_tail_recursively(head):
    if (head==None):
        return None
    if(head.next==None):
        return None
    head.next = delete_tail_recursively(head.next)
    return head 

print("Before Deletion ")
head = take_input()
head1 = delete_tail_recursively(head)
print("After Deletion ")
Printlist(head1)
