'''
Binary Tree Right Side View
Asked in Companies:

Adobe

Apple

Uber

Atlassian



Description:
Given the root of a binary tree, imagine yourself standing on the right side of it. Return the values of the nodes you can see ordered from top to bottom.



Parameters:

root (TreeNode): The root node of the binary tree.



Return Values:

List[int]: A list of integers representing the values of nodes visible from the right side of the tree.



Example:

Input:
    1
   / \
  2   3
   \
    5
     \
      4
 
Output: [1, 3, 5, 4] 
Explanation: The right side view of the tree includes the nodes 1, 3, 5, and 4.
 
 
 
Input:
    1
   / \
  2   3
 
Output: [1, 3] 
Explanation: The right side view of the tree includes the nodes 1 and 3.'''
from collections import deque
class BT:
    def __init__(self,val):
        self.val = val 
        self.left = None
        self.right = None
def rightSideView(root):
    if (root==None):
        return []
    result = []
    queue = deque([root])
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if i == level_size - 1:
                result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return result 


root = BT(1)
root.left = BT(2)
root.right = BT(3)
root.left.left = BT(4)
root.right.right = BT(5)
print(rightSideView(root))