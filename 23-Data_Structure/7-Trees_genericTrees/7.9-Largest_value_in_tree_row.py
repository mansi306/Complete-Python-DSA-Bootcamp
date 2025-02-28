r'''
Largest Value in each tree row
Asked in companies:

Cicso

Atlassian

Myntra

Policy Bazaar

Description:

Given the root of an N-ary tree, return a list of the largest value in each row of the tree. An N-ary tree is a tree where each node can have at most N children.

Input:

root: The root of the N-ary tree. Each node has a value and a list of children.

Output:

A list of integers where each integer represents the largest value found in that level of the tree.

Example:

root = Node(1, [
    Node(3, [Node(5), Node(6)]),
    Node(2),
    Node(4)
])
Output : [1,4,6]

'''

from collections import deque

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

def largest_values_in_rows(root):
    """
    Find the largest value in each row of an N-ary tree.

    Parameters:
    root (Node): The root of the N-ary tree.

    Returns:
    List[int]: A list of integers where each integer is the largest value in that level of the tree.
    """
    # Implement the function
    if not root:
        return []
 
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        max_val = float('-inf')
        
        for _ in range(level_size):
            node = queue.popleft()
            max_val = max(max_val, node.val)
            
            for child in node.children:
                queue.append(child)
        
        result.append(max_val)
    
    return result


def create_treeNode():
    root2 = Node(10)
    ch1 = Node(20)
    ch2 = Node(30)
    ch3 = Node(40)
    root2.children.append(ch1)
    root2.children.append(ch2)
    root2.children.append(ch3)
    ch1.children.append(Node(50))
    # ch2.children.append(Node(60))
    return root2

root1 = create_treeNode()
print(largest_values_in_rows(root1))
