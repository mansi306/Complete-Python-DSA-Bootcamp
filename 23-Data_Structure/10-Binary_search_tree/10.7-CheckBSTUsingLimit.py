class BST:
    def __init__(self,val):
        self.val = val 
        self.left = None
        self.right = None
def checkBStUSingLimit(root,minimum,maximum):
    if (root==None):
        return True 
    
    if (root.val < minimum or root.val > maximum):
        return False 
    ansLeft = checkBStUSingLimit(root.left,minimum,root.val-1)
    ansRight = checkBStUSingLimit(root.right,root.val+1,maximum)

    return ansLeft and ansRight

root2 = BST(20)
root2.left = BST(10)
root2.right = BST(30)
root2.left.left = BST(5)
root2.left.right = BST(15)
root2.right.left = BST(25)
root2.right.right = BST(35)
print(checkBStUSingLimit(root2,float('-inf'),float('inf')))



