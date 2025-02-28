from Common_ll import Node ,Printlist,createLLFromList
head = createLLFromList([0,1,2,3])
Printlist(head)


def search_by_value(head,data):
    temp = head 
    index = 0
    while(temp!=None):
        if(temp.data==data):
            return index 
        temp=temp.next 
        index+=1
    return "Not found!!"
print("Searching ")
print(search_by_value(head,0))