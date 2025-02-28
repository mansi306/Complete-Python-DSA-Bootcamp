class HashmapNode:
    def __init__(self,key,val):
        self.val = val 
        self.key = key 
        self.next = None
    
class hashMap:
    def __init__(self):
        self.bucketSize = 10 
        self.bucket = [None for i in range(self.bucketSize)]
        self.count = 0 

    def size(self):
        return self.count 
    

    def getIndex(self,hc):
        return (abs(hc)%self.bucketSize)

    def insert(self,key,value):
        hc = hash(key)
        index = self.getIndex(hc)
        head = self.bucket[index]
        while (head!=None):
            if (head.key==key):
                head.val = value 
                return 
            head = head.next 
        newNode = HashmapNode(key,value)
        newNode.next = head 
        self.bucket[index] = newNode
        self.count+=1
    
    def getValue(self,key):
        hc = hash(key)
        index = self.getIndex(hc)
        head = self.bucket[index]
        while head!=None:
            if head.key==key:
                return head.val
            head = head.next 
        return None 
    


    def remove(self,key):
        hc = hash(key)
        index = self.getIndex(hc)
        head = self.bucket[index]
        prev = None 
        while head!=None:
            if head.key == key:
                if prev==None:
                    self.bucket[index]=head.next 
                else:
                    prev.next = head.next
                self.count -=1 
                # return head.val 
            prev = head 
            head = head.next 
        return None 
    

m = hashMap()
m.insert("apple",10)
m.insert('mango',100)
print(m.size())
print(m.getValue('apple'))
print(m.insert('chiku',20))
print(m.size())
print(m.remove('apple'))
print(m.size())

        
            
