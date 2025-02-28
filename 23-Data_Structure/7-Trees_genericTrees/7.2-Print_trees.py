class TreeNode:
    def __init__(self,data):
        self.data = data 
        self.children = []

def print_tree(root):
    if(root==None): # Edge Case
        return
    
    print(f"{root.data}:",end = "")

    for eachChild in root.children:
        print(eachChild.data,end = ",")

    print()

    for eachChild in root.children:
        print_tree(eachChild)

root = TreeNode(10)
c1 = TreeNode(20)
c2 = TreeNode(30)
c3 = TreeNode(40)
c4 = TreeNode(50)
root.children.append(c1)
root.children.append(c2)
root.children.append(c3)
root.children.append(c4)
print_tree(root)



