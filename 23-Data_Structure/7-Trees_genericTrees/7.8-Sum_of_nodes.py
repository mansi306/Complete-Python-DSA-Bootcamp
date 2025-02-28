r'''
 (r'' is called as raw string )
Sum of Nodes
Asked in Companies:

Google

Amazon

Microsoft

Facebook



Description:
Given the root of an N-ary tree, return the sum of all the nodes' values. An N-ary tree is a tree in which each node has at most N children.



Input Parameters:

root (Node): The root of the N-ary tree. Each node contains a value and a list of children nodes.

Output:

int: The sum of all node values in the N-ary tree.



Example:

Input: root = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
Output: 21
 
Input: root = Node(10, [])
Output: 10
 
Input: root = Node(1, [Node(2, [Node(3)]), Node(4)])
Output: 10
'''

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

def sum_of_nodes(root):
    """
    Function to find the sum of all nodes in an N-ary tree.
    :param root: Node -> The root of the N-ary tree
    :return: int -> The sum of all node values in the tree
    """
    # TODO: Implement this function
    if (root==None):
        return 0 
    
    total_sum = root.val
    
    for child in root.children:
        total_sum = total_sum + sum_of_nodes(child)
    
    return total_sum
    
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
print(sum_of_nodes(root1))