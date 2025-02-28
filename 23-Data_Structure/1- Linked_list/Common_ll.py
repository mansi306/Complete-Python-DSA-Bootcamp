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

def createLLFromList(l1):
    head = None
    tail = None 
    for data in l1:
        newNode = Node(data)
        if(head==None):
            head = newNode
            tail=newNode
        else:
            tail.next = newNode
            tail = newNode
    return head 




    
# new_head = take_input()
# Printlist(new_head)






