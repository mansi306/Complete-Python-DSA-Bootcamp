'''
Same Tree
Asked in Companies:

Google

Amazon

Microsoft

Facebook



Description:
Given the roots of two binary trees p and q, write a function to check if they are the same or not. Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.



Input Parameters:

p (TreeNode): The root node of the first binary tree.

q (TreeNode): The root node of the second binary tree.

Output:

A boolean value (True or False) indicating whether the two trees are the same.

Example:

Input:
    Tree 1:
        1
       / \
      2   3
 
    Tree 2:
        1
       / \
      2   3
 
Output: True
 
 
Input:
    Tree 1:
        1
       / \
      2   1
 
    Tree 2:
        1
       / \
      1   2
 
Output: False
'''

class BT:
    def __init__(self,val):
        self.val = val 
        self.left = None
        self.right  = None

def isSameTree(p,q):
    if (p==None and q==None):
        return True 
    if (p==None or q==None):
        return False 
    if (p.val != q.val):
        return False
    return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)


def create_tree():
    root1 = BT(1)
    root1.left = BT(2)
    root1.right = BT(3)

    root2 = BT(1)
    root2.left = BT(2)
    root2.right = BT(3)
    return root1,root2

p,q  = create_tree()
print(isSameTree(p,q))

