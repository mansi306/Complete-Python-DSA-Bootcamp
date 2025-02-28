from All_function import *

def merge_two_sorted_LL(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    # Determine the starting point of the merged list
    if head1.data < head2.data:
        finalHead = head1
        head1 = head1.next
    else:
        finalHead = head2
        head2 = head2.next

    # Pointer to construct the merged list
    finalTail = finalHead  

    while head1 is not None and head2 is not None:
        if head1.data < head2.data:
            finalTail.next = head1
            head1 = head1.next
        else:
            finalTail.next = head2
            head2 = head2.next
        finalTail = finalTail.next  # Move the tail forward

    # Attach remaining elements
    if head1 is not None:
        finalTail.next = head1
    if head2 is not None:
        finalTail.next = head2

    return finalHead


# Test cases
head1 = createLLFromList([1, 2, 4, 5, 6, 8])  # Ensure the input lists are sorted
head2 = createLLFromList([3, 7, 9])
Printlist(head1)
Printlist(head2)
headfinal = merge_two_sorted_LL(head1, head2)
Printlist(headfinal)
