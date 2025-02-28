from Common_ll import Node , Printlist,take_input
# head = take_input()

def delete_tail_node(head):
    if (head==None or head.next == None):
        return None
    temp = head 
    while(temp.next.next is not None):
        temp = temp.next 
    temp.next = None
    return head 
head = take_input()
head = delete_tail_node(head)
Printlist(head)

