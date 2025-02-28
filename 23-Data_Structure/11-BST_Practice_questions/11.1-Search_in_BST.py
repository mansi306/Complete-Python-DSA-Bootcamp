'''Search in a BST
Asked in Companies:

Google

Amazon

Facebook

Microsoft



Description:
You are given the root of a binary search tree (BST) and an integer val. Your task is to find the node in the BST whose value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

A binary search tree (BST) is a binary tree in which for every node, all elements in the left subtree are smaller, and all elements in the right subtree are larger than the node's value.



Input Parameters:

root (TreeNode): The root node of the binary search tree.

val (int): The value to search for in the tree.

Output:

The node whose value matches val, or None if the node does not exist in the tree.

Example:

Input:
        4
       / \
      2   7
     / \
    1   3
val = 2
 
Output:
      2
     / \
    1   3
 
 
Input: 
        4
       / \
      2   7
     / \
    1   3
val = 5
 
Output: None

'''
class BSTNode:
    def __init__(self,val):
        self.val = val 
        self.left = None
        self.right = None

def searchBST(root,val):
    if (root==None or root.val==val):
        return root 
    
    if (val < root.val):
        return searchBST(root.left,val)
    return searchBST(root.right,val)

def print_tree(root):
    if not root:
        return
    print_tree(root.left)
    print(root.val, end=" ")
    print_tree(root.right)
    
root = BSTNode(4)
root.left = BSTNode(2)
root.right = BSTNode(7)
root.left.left = BSTNode(1)
root.left.right = BSTNode(3)
found_node = searchBST(root, 2)

if found_node:
    print("Subtree rooted at node with value 2:")
    print_tree(found_node)  # Printing the subtree starting from the found node
else:
    print("Node not found.")

