'''
Balanced Binary Tree
Asked in Companies:

Google

Amazon

Facebook

Microsoft



Description:
Given the root of a binary tree, determine if it is height-balanced. A binary tree is considered height-balanced if, for every node in the tree, the height difference between the left and right subtrees is at most 1.



Input Parameters:

root (TreeNode): The root node of the binary tree.

Output:

A boolean value (True or False) indicating whether the tree is height-balanced.



Example:

Input:
        3
       / \
      9   20
         /  \
        15   7
 
Output: True
 
 
Input:
        1
       /
      2
     /
    3
 
Output: False'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(root):
    def checkHeight(node):
        if not node:
            return 0
        
        left_height = checkHeight(node.left)
        if left_height == -1:
            return -1
        
        right_height = checkHeight(node.right)
        if right_height == -1:
            return -1
        
        if abs(left_height - right_height) > 1:
            return -1
        
        return max(left_height, right_height) + 1
    
    return checkHeight(root) != -1


# root1 = TreeNode(3)
# root1.left = TreeNode(9)
# root1.right = TreeNode(20)
# root1.right.left = TreeNode(15)
# root1.right.right = TreeNode(7)
# print(isBalanced(root1))
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.left.left = TreeNode(3)

print(isBalanced(root2))