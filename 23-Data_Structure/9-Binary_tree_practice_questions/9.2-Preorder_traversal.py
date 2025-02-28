class BT:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def Preorder_traversal(root):
    if root is None:
        return []
    result = []
    # stack follows FILO principle 
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result

def create_tree():
    root = BT(1)
    root.left = BT(2)
    root.right = BT(3)
    root.left.left = BT(4)
    root.left.right = BT(5)
    root.left.right.left = BT(6)
    root.left.right.right = BT(7)
    root.right.right = BT(8)
    root.right.right.left = BT(9)
    return root

root1 = create_tree()
print(Preorder_traversal(root1))