r'''
Count Nodes in a N-arry Tree
Asked in Companies:

Google

Amazon

Facebook

Microsoft

Description:
You are given the root of an N-ary tree. Your task is to write a function to count the total number of nodes in the tree.

An N-ary tree is a tree in which a node can have at most N children.

Input Parameters:

root (Node): The root node of the N-ary tree.

Output:

An integer representing the total number of nodes in the tree.

Example:

Input:
      1
    / | \
   2  3  4
      |
      5
 
Output: 5
 
 
Input:
      1
    / | \ 
   2  3  4  5
 
Output: 5

'''

# Definition for a Node in an N-ary tree.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []



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

def count_nodes(root):
    """
    Function to count the number of nodes in an N-ary tree.
    :param root: Node -> root of the N-ary tree
    :return: int -> total number of nodes in the tree
    """
    # TODO: Implement this function
    if (root is None):
        return 0 
    count = 1 
    for child in root.children:
        count = count + count_nodes(child)
    return count 

root1 = create_treeNode()
print(count_nodes(root1))
        
    
