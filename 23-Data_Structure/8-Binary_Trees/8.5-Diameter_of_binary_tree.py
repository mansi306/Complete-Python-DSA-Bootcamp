from predefinedBT import predefined_binary_tree_inputs
class BT:
    def __init__(self,data):
        self.data = data 
        self.left = None
        self.right = None

def height_of_tree(root):
    if root is None:
        return 0 
    left_height  = height_of_tree(root.left)
    right_height = height_of_tree(root.right)
    height_tree = 1 + max(left_height,right_height)
    return height_tree


def diameter_of_tree(root):
    if root == None:
        return 0,0 
    
    left_height , left_diameter = diameter_of_tree(root.left)
    right_height, right_diameter= diameter_of_tree(root.right)
    diameter_throught_root = left_height + right_height
    ans_diameter = max(left_height,right_height,diameter_throught_root)
    current_tree_height = 1 + max(left_height,right_height)
    return current_tree_height,ans_diameter


root1 = BT(1)
root1.left = BT(2)
root1.right = BT(3)
root1.left.left = BT(4)
root1.left.right = BT(5)
root1.right.right = BT(6)




# root1,root2,root3 = predefined_binary_tree_inputs()
print(height_of_tree(root1))
print(diameter_of_tree(root1))