class Node:
    def __init__(self,value):
        self.val = value 
        self.next = None

class QueueUsingLL:
    def __init__(self):
        self.head = None 
        self.tail = None
        self.len = 0 

    def size(self):
        return self.len
    
    def isEmpty(self):
        return self.size()==0
    
    def enqueue(self,data):
        newNode = Node(data)
        self.len+=1
        if (self.head==None):
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        return f"Added {data} to the queue"
    
    def front(self):
        if(self.isEmpty()):
            print ("Queue is Empty, cannot show Front")
            return
        return self.head.val
    
    def dequeue(self):
        if(self.isEmpty()):
            print ("Queue is Empty, cannot show Front")
            return
        self.len-=1
        dataTobeReturned = self.head.val
        self.head = self.head.next 
        if(self.head == None): # Very Very Important to handle the Right Form of Queue 
            self.tail = None 
        return dataTobeReturned
    
    def rear(self):
        if self.isEmpty():
            print("Queue is empty , cannot show Rear")
            return 
        return self.tail.val
    
Q = QueueUsingLL()

Q.enqueue(10)
Q.enqueue(20)
Q.enqueue(30)
print(Q.size())
print(Q.isEmpty())
print(Q.front())
print(Q.dequeue())
print(Q.dequeue())
print(Q.front())
print(Q.size())
print(Q.rear())

    



    
