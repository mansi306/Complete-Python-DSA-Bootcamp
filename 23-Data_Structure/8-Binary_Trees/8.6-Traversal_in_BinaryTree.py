from predefinedBT import predefined_binary_tree_inputs
class BT:
    def __init__(self,data):
        self.data = data 
        self.left = None
        self.right = None

def Preorder_traversal(root): # Root -> left -> Right
    if (root==None):
        return 
    print(f"{root.data}",end=" ")
    Preorder_traversal(root.left)
    Preorder_traversal(root.right)

def Postorder_traversal(root): # Left -> Right -> Root 
    if (root==None):
        return 
    Postorder_traversal(root.left)
    Postorder_traversal(root.right)
    print(root.data,end=" ")

def Inorder_traversal(root): # Left -> Root -> Right 
    if (root==None):
        return 
    Inorder_traversal(root.left)
    print(root.data,end=" ")
    Inorder_traversal(root.right)



root1,root2,root3,root4 = predefined_binary_tree_inputs()
print("Preorder Traversal ")
print(Preorder_traversal(root4))
print("Postorder Traversal")
print(Postorder_traversal(root4))
print("Inorder Traversal ")
print(Inorder_traversal(root4))
