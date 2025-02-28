'''
Binary Tree Inorder Traversal
Description:

Given the root of a binary tree, return the Inorder traversal of its nodes' values. Inorder traversal of a binary tree means visiting the left subtree, the root node, and then the right subtree recursively. The task is to implement this without using any in-built functions like inorder_traversal from Python's libraries.



Asked in Companies:

Google

Facebook

Microsoft

Amazon



Input Parameters:

root (TreeNode): The root node of the binary tree.

Output:

A list of integers representing the inorder traversal of the tree.

Example:

Input:
        1
         \
          2
         /
        3
 
Output: [1, 3, 2]

'''
from predefinedBT import predefined_binary_tree_inputs
class BT:
    def __init__(self,val):
        self.val = val 
        self.left = None
        self.right = None

def Inorder_traversal(root):
    stack = []
    result = []
    current = root
    while stack or current :
        while current:
            # checking for the left node 
            stack.append(current)
            current = current.left 
        # checking for the root node 
        current = stack.pop()
        result.append(current.val)
        # checking for right Node 
        current = current.right 
    return result 




roo1,root2,root3,root4 = predefined_binary_tree_inputs()
print(Inorder_traversal(root4))

