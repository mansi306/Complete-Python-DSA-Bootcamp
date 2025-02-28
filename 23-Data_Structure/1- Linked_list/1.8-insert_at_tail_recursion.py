from Common_ll import Node , Printlist,take_input
head = take_input()
print("before inserting at tail ")
Printlist(head)

def insertTailUsingRecursion(head,data):
    if (head==None):
        newNode = Node(data)
        return newNode
    head.next = insertTailUsingRecursion(head.next,data)
    return head 

newhead = insertTailUsingRecursion(head,100)
print("After inserting at tail ")
Printlist(newhead)