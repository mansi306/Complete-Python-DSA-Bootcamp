class queueUsingList:
    def __init__(self):
        self.__queue = [] # make it private for correct functinality 
    
    # size function 
    def size(self):
        return len(self.__queue)
    
    def isEmpty(self):
        return self.size() == 0
    
    def enqueue(self,data):
        self.__queue.append(data)
        return f"We have added {data} to queue "
    
    def front(self):
        if self.size()==0:
            print(f"Queue is Empty,cannot have front ")
        return self.__queue[0]
    
    def rear(self):
        if self.size()==0:
            print(f"Queue is Empty,cannot have Rear element ")
        return self.__queue[-1]
    
    def dequeue(self):
        if self.size()==0:
            print(f"Queue is Empty,cannot have front ")
        return self.__queue.pop(0)
    

q = queueUsingList()
print(q.isEmpty())
print(q.enqueue(10))
print(q.enqueue(20))
print(q.enqueue(30))
# print(q.enqueue(40))
# print(q.enqueue(50))
print(q.isEmpty())
print(q.size())
print(q.front())
print(q.rear())
print(q.dequeue())
print(q.front())
print(q.rear())
