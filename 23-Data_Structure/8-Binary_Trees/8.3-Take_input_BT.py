class BinaryTreeNode:
    def __init__(self,data):
        self.data = data 
        self.left = None
        self.right = None
    
def take_input():
    data = int(input("Enter the data for the Node:"))
    if (data==-1):
        return None
    node = BinaryTreeNode(data)
    print(f"Enter left child of {data}: ")
    node.left = take_input()
    print(f"Enter Right child of {data}: ")
    node.right = take_input()
    return node 

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


root1 = take_input()
print(root1)
print_binary_tree(root1)