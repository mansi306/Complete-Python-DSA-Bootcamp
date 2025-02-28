class BST:
    def __init__(self,val):
        self.val = val 
        self.left = None
        self.right = None

def checkBST(root):
    if (root==None):
        return True,float('inf'),float('-inf')
    
    is_leftBST,left_min,left_max = checkBST(root.left)
    isrightBST,right_min,right_max = checkBST(root.right)
    if (is_leftBST and isrightBST and left_max < root.val and  root.val< right_min):
        return True, min(left_min, root.val), max(right_max, root.val)
    else:
        return False, min(left_min, root.val), max(right_max, root.val)
    
root2 = BST(20)
root2.left = BST(10)
root2.right = BST(30)
root2.left.left = BST(5)
root2.left.right = BST(15)
root2.right.left = BST(25)
root2.right.right = BST(35)
print(checkBST(root2))