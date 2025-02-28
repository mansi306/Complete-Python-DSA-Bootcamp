from Common_ll import Node ,Printlist,take_input

head = take_input()
print("Before inserting Linked list ")
Printlist(head)
def insert_at_head(head,data):
    newNode = Node(data) 
    newNode.next = head 
    head = newNode
    return head 

head = insert_at_head(head,0)
print("After inserting at head ")
Printlist(head)
