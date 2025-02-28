'''
Maximum Depth of a Binary Tree
Asked in Companies:

Google

Amazon

Facebook

Microsoft

Description:
Given the root of a binary tree, return its maximum depth. The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Input Parameters:

root (TreeNode): The root node of the binary tree.

Output:

An integer representing the maximum depth of the binary tree.
Example:

Input:
        3
       / \
      9   20
         /  \
        15   7
 
Output: 3
'''
from collections import deque 
class BT:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
def Max_depth(root):
    if (root==None):
        return 0 
    level = 0
    queue = deque([root])
    while queue:
        for i in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right :
                queue.append(node.right)
        level+=1
    return level 

def create_tree():
    root = BT(3)
    root.left = BT(9)
    root.right = BT(20)
    root.right.left  = BT(15)
    root.right.right = BT(7)
    return root 

root1 = create_tree()
print(Max_depth(root1))