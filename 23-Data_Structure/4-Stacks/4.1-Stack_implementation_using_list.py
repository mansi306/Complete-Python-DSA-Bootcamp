'''
Stack implementation using - built In-built python list 
'''
class StackUsingList:
    def __init__(self):
        self.__stack = []  # very important to make it private so that functionality be right 

    def push(self,data):
        self.__stack.append(data)
        print(f'Pushed {data} into stack ')
    
    def size(self):
        return len(self.__stack)
    
    def is_empty(self):
        if len(self.__stack)==0:
            return True 
        else:
            return False 
        
        # return len(self.stack)==0

    def top(self):
        # self.stack(len(self.stack)-1)
        if len(self.__stack)==0:
            print('Stack is empty ,no top element')
            return None
        return self.__stack[-1]
    

    def pop(self):
        return self.__stack.pop()
    
    def display(self):
        for val in self.__stack :
            print(val)
    
mystack = StackUsingList()
print(mystack.is_empty())
print(mystack.push(10))
print(mystack.push(20))
print(mystack.push(30))
print(mystack.push(40))
print(mystack.is_empty())
print(mystack.pop())
print(mystack.pop())
print(mystack.size())
print(mystack.top())

