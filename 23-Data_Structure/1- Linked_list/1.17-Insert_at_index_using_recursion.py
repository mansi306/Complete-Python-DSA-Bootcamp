from Common_ll import Node , Printlist,take_input

def  insert_at_index_using_recursion(head,data,index):
    if (index==0):
        newnode = Node(data)
        newnode.next = head 
        return newnode
    
    if (head==None):
        print("Index out of range ")
    head.next = insert_at_index_using_recursion(head.next,data,index-1)
    return head 

head = take_input()
print("Before Inserting ")
Printlist(head)
# head1 = insert_at_tail(head,50)
# head1 = insert_at_index(head,50,2)
head1 = insert_at_index_using_recursion(head,30,3)
print("After inserting ")
Printlist(head1)