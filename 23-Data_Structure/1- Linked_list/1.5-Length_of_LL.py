class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
    
def take_input():
    data = int(input("Enter a node value : "))
    head = None 
    tail = None
    while (data!=-1):
        newnode = Node(data)
        if(head==None):
            head = newnode
            tail = newnode
        else:
            tail.next = newnode
            tail = newnode
        data = int(input("Enter a node value : "))
    return head 
    

def length_of_LL(head):
    temp = head 
    count = 0 
    while(temp!=None):
        temp=temp.next 
        count+=1
    return f"Count : {count}"


newhead = take_input()
print(length_of_LL(newhead))

def lengthOfLinkedRecursion(head):
    if (head==None):
        return 0
    recursionAns = lengthOfLinkedRecursion(head.next)
    return 1+ recursionAns


length = lengthOfLinkedRecursion(newhead)
print(length)


