'''Successor and Predecessor in a BST
Asked in Companies:

De Shaw

IBM

Oracle



Description:
You are given a binary search tree (BST) with N nodes and an integer KEY representing the data of a node in this BST. Your task is to find and return the predecessor and successor of the node with the given KEY.

Predecessor: The node that would be visited immediately before the node with KEY in an inorder traversal of the BST. If the given node is the first node in the inorder traversal, the predecessor should be NULL.

Successor: The node that would be visited immediately after the node with KEY in an inorder traversal of the BST. If the given node is the last node in the inorder traversal, the successor should be NULL.



Input Parameters:

root (TreeNode): The root of the binary search tree.

KEY (int): The data value of the node for which to find the predecessor and successor.

Output:

A tuple (predecessor, successor), where both predecessor and successor are integers. If the predecessor or successor does not exist, return None for that value.



Example:

Input:
      20
     /  \
    10   30
   / \    \
  5  15   35
KEY = 35
Output: (30, None)
Explanation: In the inorder traversal [5, 10, 15, 20, 30, 35], the predecessor of 35 is 30 and there is no successor.
 
 
Input:
      20
     /  \
    10   30
   / \    \
  5  15   35
KEY = 10
Output: (5, 15)
Explanation: In the inorder traversal [5, 10, 15, 20, 30, 35], the predecessor of 10 is 5 and the successor is 15.'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
 
def find_predecessor_successor(root, key):
    # Initialize predecessor and successor
    predecessor = None
    successor = None
 
    # Helper function to find the node with the given key
    def find_node(root, key):
        if root is None:
            return None
        if root.val == key:
            return root
        elif key < root.val:
            return find_node(root.left, key)
        else:
            return find_node(root.right, key)
 
    # Helper function to find the maximum value node in a subtree
    def find_max(node):
        while node.right is not None:
            node = node.right
        return node
 
    # Helper function to find the minimum value node in a subtree
    def find_min(node):
        while node.left is not None:
            node = node.left
        return node
 
    # Find the target node
    target_node = find_node(root, key)
    
    if not target_node:
        return (None, None)
    
    # Finding predecessor
    if target_node.left:
        predecessor = find_max(target_node.left).val
    
    # Finding successor
    if target_node.right:
        successor = find_min(target_node.right).val
    
    # Find predecessor if target node has no left subtree
    def find_predecessor(root, key):
        pred = None
        while root:
            if key > root.val:
                pred = root.val
                root = root.right
            elif key < root.val:
                root = root.left
            else:
                break
        return pred
    
    predecessor = find_predecessor(root, key) if target_node.left is None else predecessor
    
    # Find successor if target node has no right subtree
    def find_successor(root, key):
        succ = None
        while root:
            if key < root.val:
                succ = root.val
                root = root.left
            elif key > root.val:
                root = root.right
            else:
                break
        return succ
    
    successor = find_successor(root, key) if target_node.right is None else successor
    
    return (predecessor, successor)
 
# Helper function for debugging (can be removed for production)
def display_predecessor_successor(root, key):
    result = find_predecessor_successor(root, key)
    print(result)
 
# Example usage (can be removed)
root = TreeNode(20)
root.left = TreeNode(10)
root.right = TreeNode(30)
root.left.left = TreeNode(5)
root.left.right = TreeNode(15)
root.right.right = TreeNode(35)
display_predecessor_successor(root, 10)  # Output: (5, 15)
