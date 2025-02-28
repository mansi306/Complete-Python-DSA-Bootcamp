from All_function import Node , Printlist, createLLFromList,Length_of_LL

headOdd = createLLFromList([1,2,3,4,5])
Printlist(headOdd)
headEven = createLLFromList([1,2,3,4,5,6,7,8])
Printlist(headEven)

def Middle_of_LL(head):
    if (head==None or head.next == None):
        return head 
    
    length = Length_of_LL(head)
    middle = length//2
    temp = head 
    count = 0 
    while(count<middle):
        temp = temp.next 
        count+=1
    return temp 


def middleOfLLusingSlowFast(head):
    if (head==None or head.next ==None):
        return head 
        
    slow = head 
    fast = head 
    while (fast!=None and fast.next!=None):
        slow = slow.next 
        fast = fast.next.next 
    return slow 

headOddmid = middleOfLLusingSlowFast(headOdd)
headEvenmid = middleOfLLusingSlowFast(headEven)
print(headOddmid.data)
print(headEvenmid.data)