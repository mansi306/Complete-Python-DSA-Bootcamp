'''
Binary Tree Postorder Traversal
Asked in Companies:

Amazon

Microsoft

Google

Facebook

Description:
Given the root of a binary tree, return the postorder traversal of its nodes' values. In postorder traversal, the nodes are visited in this order: first the left subtree, then the right subtree, and finally the root node.



Input Parameters:

root (TreeNode): The root node of the binary tree.

Output:

A list of integers representing the postorder traversal of the tree.

Example:

Input:
        1
         \
          2
         /
        3
 
Output: [3, 2, 1]
'''

class BT:
    def __init__(self,val):
        self.val = val 
        self.left = None
        self.right = None


def Postorder_traversal(root):
    if (root==None):
        return []
    
    stack = []
    result = []
    last_visited = None
    while stack or root:
        if root:
            stack.append(root)
            root = root.left 
        else:
            peek_node = stack[-1]
            if peek_node.right and last_visited != peek_node.right:
                root = peek_node.right
            else:
                result.append(peek_node.val)
                last_visited = stack.pop()

    return result 

def create_tree():
    root = BT(1)
    root.left = BT(2)
    root.right = BT(3)
    root.left.left = BT(4)
    root.left.right = BT(5)
    root.left.right.left = BT(6)
    root.left.right.right = BT(7)
    root.right.right = BT(8)
    root.right.right.left = BT(9)
    return root 


root1 = create_tree()
print(Postorder_traversal(root1))


    