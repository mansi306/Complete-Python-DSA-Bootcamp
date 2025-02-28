class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_elements(head, val):
    """
    Function to remove all nodes with value val from the linked list.
    :param head: ListNode -> head of the singly linked list
    :param val: int -> the value to be removed
    :return: ListNode -> the head of the new linked list
    """
    dummy = ListNode(0)
    dummy.next = head
    
    # Initialize pointers
    current = dummy
    
    # Traverse the list
    while current.next is not None:
        if current.next.val == val:
            # Skip the node with value val
            current.next = current.next.next
        else:
            # Move to the next node
            current = current.next
    
    return dummy.next  # Corrected: Removed extra period

# Helper function to create a linked list from a list
def create_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Test the function
head = create_linked_list([1, 2, 6, 3, 4, 5, 6])
print("Original list:")
print_linked_list(head)

new_head = remove_elements(head, 6)
print("Modified list:")
print_linked_list(new_head)
