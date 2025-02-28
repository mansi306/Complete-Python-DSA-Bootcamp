class BST:
    def __init__(self,val):
        self.val = val 
        self.left = None
        self.right = None

def PrintInRange(root,low,high):
    if (root==None):
        return 
    
    if (low < root.val):
        PrintInRange(root.left,low,high)
    if (low<=root.val<=high):
        print(root.val,end=" ")
    if (high> root.val):
        PrintInRange(root.right,low,high)
    
root2 = BST(20)
root2.left = BST(10)
root2.right = BST(30)
root2.left.left = BST(5)
root2.left.right = BST(15)
root2.right.left = BST(25)
root2.right.right = BST(35)
print(PrintInRange(root2,15,35))

