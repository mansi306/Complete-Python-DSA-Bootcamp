class TreeNode:
    def __init__(self,data):
        self.data = data 
        self.children = []



root = TreeNode(1)
c1 = TreeNode(2)
c2 = TreeNode(3)
c3 = TreeNode(4)
c4 = TreeNode(5)
c5 = TreeNode(6)
root.children.append(c1)
root.children.append(c2)
root.children.append(c3)
root.children.append(c4)
root.children.append(c5)
print(root.children[0].data )