from Common_ll import Node, take_input,Printlist

def delete_at_index_using_recursion(head,index):
    if(head==None):
        print("Index out of bound ")
        return None 
    if (index==0):
        return head.next 
    
    head.next = delete_at_index_using_recursion(head.next,index-1)
    return head 

head = take_input()
head1 = delete_at_index_using_recursion(head,3)
print("After deletion ")
Printlist(head1)