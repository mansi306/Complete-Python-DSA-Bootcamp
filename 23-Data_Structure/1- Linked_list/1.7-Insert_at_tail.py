from Common_ll import Node,Printlist,take_input
head = take_input()
print("Before Inserting at tail ")
Printlist(head)

def Insert_at_tail(head,data):
    newNode = Node(data) 
    if (head is None):
        return newNode
    temp =head 
    while(temp.next!=None):
        temp = temp.next 
    temp.next = newNode
    return head 

head = Insert_at_tail(head,100)
print("After inserting at tail ")
Printlist(head)
    