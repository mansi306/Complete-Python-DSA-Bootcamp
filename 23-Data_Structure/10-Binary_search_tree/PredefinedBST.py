
class BSTNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
    
def CreatePredefinedBST():

    # Tree1 
    # Structure
    #          10
    #        /    \
    #       5     15

    root1 = BSTNode(10)
    root1.left = BSTNode(5)
    root1.right = BSTNode(15)


    #  Tree2 
    root2 = BSTNode(20)
    root2.left = BSTNode(10)
    root2.right = BSTNode(30)
    root2.left.left = BSTNode(5)
    root2.left.right = BSTNode(15)
    root2.right.left = BSTNode(25)
    root2.right.right = BSTNode(35)


    #Tree3 

    root3 = BSTNode(40)
    root3.left = BSTNode(20)
    root3.right = BSTNode(60)
    root3.left.left = BSTNode(10)
    root3.left.right = BSTNode(30)
    root3.right.left = BSTNode(50)
    root3.right.right = BSTNode(70)
    root3.left.left.left = BSTNode(5)
    root3.left.left.right = BSTNode(15)
    root3.left.right.left = BSTNode(25)
    root3.left.right.right = BSTNode(35)
    root3.right.left = BSTNode(50)
    root3.right.left.right = BSTNode(55)
    root3.right.right = BSTNode(70)
    root3.right.right.left = BSTNode(65)
    root3.right.right.right = BSTNode(75)
    return root1,root2,root3

    
def print_Inorder_traversal(root):
    if root==None:
        return 
    
    print_Inorder_traversal(root.left )
    print(root.val,end=' ')
    print_Inorder_traversal(root.right)

    


# root1,root2, root3 = CreatePredefinedBST()
# print_Inorder_traversal(root2)
    


    
    


