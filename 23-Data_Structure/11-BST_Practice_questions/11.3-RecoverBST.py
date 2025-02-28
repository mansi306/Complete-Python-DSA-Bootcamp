'''
Recover a BST
Asked in Companies:
Microsoft
Apple
LinkedIn

Description:
You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Your task is to recover the BST by swapping the values of these two nodes back to their correct positions. The structure of the tree should remain unchanged.
Input Parameters:
root (TreeNode): The root of the binary search tree.
Output:
The root of the corrected binary search tree.
Example:

Input:
      3
     / \
    1   4
       /
      2
 
Output:
      2
     / \
    1   4
       /
      3
 
Explanation: The original tree has 2 and 3 swapped. The corrected tree is a valid BST.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
 
def recover_tree(root):
    """
    Function to recover a BST where two nodes were swapped by mistake.
    
    :param root: TreeNode -> The root of the binary search tree
    :return: TreeNode -> The root of the corrected binary search tree
    """
    def inorder_traversal(node):
        if node is None:
            return []
        return inorder_traversal(node.left) + [node] + inorder_traversal(node.right)
    
    # In-order traversal to get nodes in sorted order
    nodes = inorder_traversal(root)
    
    # Find the two nodes that are swapped
    first = second = None
    prev = TreeNode(float('-inf'))
    
    for node in nodes:
        if node.val < prev.val:
            if first is None:
                first = prev
            second = node
        prev = node
    
    # Swap the values of the two nodes
    if first and second:
        first.val, second.val = second.val, first.val
 
    return root
 
# Helper function for debugging (can be removed for production)
def display_recovered_tree(root):
    result = inorder_traversal(root)
    print(result)
 
def inorder_traversal(node):
    """Helper function to get in-order traversal of the tree."""
    if node is None:
        return []
    return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)
 
# Example usage (can be removed)
# Correct Test Case (from problem description)
tree = TreeNode(3)
tree.left = TreeNode(1)
tree.right = TreeNode(4)
tree.right.left = TreeNode(2)  # Swapped node

print("Before Fix:", inorder_traversal(tree))
recovered_tree = recover_tree(tree)
print("After Fix:", inorder_traversal(recovered_tree))
