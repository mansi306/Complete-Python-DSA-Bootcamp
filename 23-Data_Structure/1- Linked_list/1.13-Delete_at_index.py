from Common_ll import Node, take_input,Printlist

def delete_at_index(head,index):
    if(head==None):
        return head 
    if(index==0):
        return head.next 
    temp = head 
    count = 0
    while (head!=None and count<index-1):
        temp = temp.next 
        count+=1
    
    if (temp==None or temp.next==None):
        print("Out of bound")
        return head 
    
    # noteToBeDeleted = temp.next 
    # nodeAfterDeletdNode = noteToBeDeleted.next 
    temp.next = temp.next.next 
    return head 
head1 = take_input()
head = delete_at_index(head1,3)
print("After deletion ")
Printlist(head)

    
