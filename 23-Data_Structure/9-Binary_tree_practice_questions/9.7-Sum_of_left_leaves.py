'''
Sum of Left Leaves
Asked in Companies:

Google

Amazon

Microsoft

Facebook



Description:
Given the root of a binary tree, return the sum of all left leaves. A leaf is defined as a node with no children. A left leaf is a leaf that is the left child of another node.



Input Parameters:

root (TreeNode): The root of the binary tree.

Output:

int: The sum of all left leaves in the binary tree.



Example:

Input: root = [1, 2, 3, 4, null, null, 5]
Output: 4
     1
    / \
   2   3
  /     \
 4       5
 
 
Input: root = [3, 9, 20, null, null, 15, 7]
Output: 24
     3
    / \
   9  20
      / \
     15  7
'''
class BT:
    def __init__(self,val):
        self.val = val 
        self.left = None
        self.right = None
    
def sumOfLeftLeaves(root):
    if (root==None):
        return 0 
    total = 0 
    if root.left and root.left.left == None and root.left.right == None:
        total += root.left.val 
    
    total += sumOfLeftLeaves(root.left)
    total += sumOfLeftLeaves(root.right)
    return total 

root = BT(1)
root.left = BT(2)
root.right = BT(3)
root.left.left = BT(4)
root.right.right = BT(5)
print(sumOfLeftLeaves(root))