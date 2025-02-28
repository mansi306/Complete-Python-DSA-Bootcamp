from PredefinedBST import CreatePredefinedBST

class BST:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def SearchInBST(root, value):
    if root is None:
        return False
    if root.val == value:
        return True
    if root.val > value:
        return SearchInBST(root.left, value)  # Pass value in recursive call
    else:
        return SearchInBST(root.right, value)  # Pass value in recursive call

# Creating predefined BSTs
root1, root2, root3 = CreatePredefinedBST()

# Searching for a value in root2
print(SearchInBST(root2, 25))  # Should return True if 25 exists, else False
