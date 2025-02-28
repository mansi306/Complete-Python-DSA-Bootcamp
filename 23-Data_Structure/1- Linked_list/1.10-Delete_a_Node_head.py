from Common_ll import Node,take_input,Printlist
head = take_input()
def delete_at_head(head):
    if (head is  None):
        return None
    newhead = head.next 
    return newhead
Printlist(head)

head = delete_at_head(head)
print("After Deletion ")
Printlist(head)
