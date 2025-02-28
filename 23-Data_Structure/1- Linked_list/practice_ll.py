# creating a linked list 
#  creating a node 
class Node:
    # constructor 
    def __init__(self,data):
        self.data = data 
        self.next = None

def PrintLL(head):
    temp = head 
    while(temp!=None):
        print(temp.data,end="->")
        temp = temp.next 
    print()
    return 


def take_input():
    data = int(input("Enter a node value : "))
    head = None
    tail = None
    while(data!=-1):
        newNode = Node(data)
        if (head==None):
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
        data = int(input("Enter a node value : "))
    return head 

def count_length(head):
    temp = head 
    count =0 
    while(temp!=None):
        temp = temp.next 
        count+=1
    return count 


def insert_at_head(head,data):
    newnode= Node(data)
    newnode.next = head 
    head = newnode
    return head 


def insert_at_tail(head,data):
    newnode = Node(data)
    if (head==None):
        return newnode
    temp = head 
    while(temp.next!=None):
        temp = temp.next
    temp.next= newnode
    return head 

def insert_at_index(head,data,index):
    if (index==0):
        newnode = Node(data)
        newnode.next = head 
        head = newnode
        return head 
    newnode = Node(data)
    temp = head 
    count = 0
    while(temp!=None and count<index-1):
        temp = temp.next 
        count+=1
    
    newnode.next = temp.next 
    temp.next = newnode
    return head 

def  insert_at_index_using_recursion(head,data,index):
    if (index==0):
        newnode = Node(data)
        newnode.next = head 
        return newnode
    
    if (head==None):
        print("Index out of range ")
    head.next = insert_at_index_using_recursion(head.next,data,index-1)
    return head 


def delete_node_at_head(head):
    if (head==None):
        return None
    newhead = head.next 
    return newhead

def delete_tail_node(head):
    if (head==None or head.next == None):
        return None
    temp = head 
    while(temp.next.next is not None):
        temp = temp.next 
    temp.next = None
    return head 


# n1 = Node(10)
# n2 = Node(20)
# n3 = Node(30)
# n4 = Node(40)
# n1.next = n2 
# n2.next = n3 
# n3.next = n4 
# head = n1 
# PrintLL(head)



# print(count_length(newhead))
# head1 = insert_at_head(head,0)
# PrintLL(head1)
head = take_input()
# print("Before Inserting ")
print("Before Deletion ")
PrintLL(head)
# head1 = insert_at_tail(head,50)
# head1 = insert_at_index(head,50,2)
# head1 = insert_at_index_using_recursion(head,30,3)
# head1=delete_node_at_head(head)
head1 = delete_tail_node(head)
# print("After inserting ")
print("After deletion ")
PrintLL(head1)