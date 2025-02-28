class BT:
    def __init__(self,val):
        self.val = val 
        self.left = None
        self.right = None

def count_leaves(root):
    if (root==None):
        return 0 
    count = 0
    
    if root.left==None and root.right ==None:
        count +=1 
    
    count += count_leaves(root.left)
    count+= count_leaves(root.right)
    return count 

root2 = BT(30)
root2.left = BT(25)
root2.right = BT(35)
root2.left.left = BT(20)
root2.left.right = BT(28)
root2.right.right = BT(40)
root2.left.right.left = BT(27)
# root1 =BT(10)
# root1.left =BT(5)
# root1.right =BT(15)

print(count_leaves(root2))

