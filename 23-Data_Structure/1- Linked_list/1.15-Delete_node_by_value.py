from Common_ll import Node, take_input, Printlist

def delete_node_by_value(head, data):
    if head is None:
        print("List is empty")
        return None
    
    if head.data == data:
        print(f"Deleting head node with value: {data}")
        return head.next
    
    temp = head
    while temp.next is not None and temp.next.data != data:
        temp = temp.next
    if temp.next is None:
        print(f"Value {data} not found in the list.")
        return head
    print(f"Deleting node with value: {temp.next.data}")
    temp.next = temp.next.next  
    return head
head = take_input()


print("Linked List before deletion:")
Printlist(head)
head = delete_node_by_value(head, 4)

# Print the list after deletion
print("Linked List after deletion:")
Printlist(head)
