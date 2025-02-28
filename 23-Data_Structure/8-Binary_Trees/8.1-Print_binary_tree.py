
from predefinedBT  import BinaryTreeNode, predefined_binary_tree_inputs
class BinaryTreeNode:
    def __init__(self,data):
        self.data = data 
        self.left = None
        self.right = None 
def print_binary_tree(root):
    if (root==None):
        return 
    
    print(f"{root.data}:",end=" ")
    if (root.left !=None):
        print(f"L-> {root.left.data}",end=",")
    else:
        print(f"L-> None",end=",")

    if (root.right !=None):
        print(f"R-> {root.right.data}")
    else:
        print(f"R-> None")
    
    print_binary_tree(root.left)
    print_binary_tree(root.right)


# root = BinaryTreeNode(10)
# root.left = BinaryTreeNode(20)
# root.right = BinaryTreeNode(30)

root1,root2,root3 = predefined_binary_tree_inputs()
print_binary_tree(root1)