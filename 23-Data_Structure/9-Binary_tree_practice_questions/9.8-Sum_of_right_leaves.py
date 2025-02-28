class BT:
    def __init__(self,val):
        self.val = val 
        self.left = None
        self.right = None
    
def sumOfLeftLeaves(root):
    if (root==None):
        return 0 
    total = 0 
    if root.right and root.right.left == None and root.right.right == None:
        total += root.right.val 
    
    total += sumOfLeftLeaves(root.left)
    total += sumOfLeftLeaves(root.right)
    return total 

root = BT(1)
root.left = BT(2)
root.right = BT(3)
root.left.left = BT(4)
root.right.right = BT(5)
print(sumOfLeftLeaves(root))