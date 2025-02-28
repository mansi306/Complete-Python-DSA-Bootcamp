class Node :
    def __init__(self,data):
        self.data = data 
        self.next = None 
    
def Printlist(head):
    temp = head 
    while(temp!=None):
        print(temp.data,end='->')
        temp = temp.next 
    print()
    return 
def take_input():
    data = int(input("Enter a node value :"))
    head = None
    tail = None 
    while (data!=-1):
        newnode = Node(data)
        if (head==None):
            head = newnode
            tail = newnode 
        else:
            tail.next = newnode
            tail = newnode
        data = int(input("Enter a node value :"))
    return head 

def insert_at_head(head,data):
    newNode = Node(data) 
    newNode.next = head 
    head = newNode
    return head 

def Insert_at_tail(head,data):
    newNode = Node(data) 
    if (head is None):
        return newNode
    temp =head 
    while(temp.next!=None):
        temp = temp.next 
    temp.next = newNode
    return head 

def insertTailUsingRecursion(head,data):
    if (head==None):
        newNode = Node(data)
        return newNode
    head.next = insertTailUsingRecursion(head.next,data)
    return head 

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


head = take_input()
print("Before inserting at index ")
Printlist(head)

newhead = insert_at_index(head,100,2)
print("After inserting at a index ")
Printlist(newhead)


def Length_of_LL(head):
    temp = head 
    count=0
    while(temp!=None):
        temp = temp.next 
        count+=1
    return count 










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
