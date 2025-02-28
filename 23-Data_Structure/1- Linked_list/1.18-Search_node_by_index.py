from Common_ll import Node, createLLFromList, Printlist

head = createLLFromList([1, 2, 3, 4, 5, 6])
Printlist(head)

def search_node_by_index(head, index):
    if index < 0:
        return None  # Negative index is invalid
    temp = head
    count = 0
    while temp is not None:
        if count == index:
            return temp.data  # Return the node's data
        temp = temp.next
        count += 1
    return None  # Index out of bounds

print("Searching:")
print(search_node_by_index(head, 4))  # Now it will print output
