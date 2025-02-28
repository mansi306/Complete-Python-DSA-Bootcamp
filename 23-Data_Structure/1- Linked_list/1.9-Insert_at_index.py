from Common_ll import Node ,Printlist,take_input
head = take_input()
print("Before inserting at index ")
Printlist(head)

def insert_at_index(head,data,index):
    if(index==0):
        newNode= Node(data)
        newNode.next = head
        head = newNode
        return head 
    
    newNode= Node(data)
    temp = head 
    count = 0
    while temp is not None and count<index-1:
        temp = temp.next 
        count+=1
    if (temp is None):
        print("Index out of bound , please check index ")
        return head 
    newNode.next = temp.next 
    temp.next = newNode
    return head 
newhead = insert_at_index(head,50,3)
print("After inserting at index ")
Printlist(newhead)









