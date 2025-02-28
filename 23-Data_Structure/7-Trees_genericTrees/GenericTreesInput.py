class GenericTreeNode:
    def __init__(self,data):
        self.data = data 
        self.children = []
    
def predifined_generic_tree_input():
    root1 = GenericTreeNode(1)
    ch1 = GenericTreeNode(2)
    ch2 = GenericTreeNode(3)
    root1.children.append(ch1)
    root1.children.append(ch2)
    ch1.children.append(GenericTreeNode(4))
    ch1.children.append(GenericTreeNode(5))


    # root 2 
    # root2 = GenericTreeNode(10)
    # ch1 = GenericTreeNode(20)
    # ch2 = GenericTreeNode(30)
    # ch3 = GenericTreeNode(40)
    # root2.children.append(ch1)
    # root2.children.append(ch2)
    # root2.children.append(ch3)
    # ch1.children.append(GenericTreeNode(50))
    # ch2.children.append(GenericTreeNode(60))


    # root3 = GenericTreeNode(100)
    # ch1 = GenericTreeNode(200)
    # ch2 = GenericTreeNode(300)
    # root3.children.append(ch1)
    # root3.children.append(ch2)
    # ch2.children.append(GenericTreeNode(400))
    # ch2.children.append(GenericTreeNode(500))
    return root1

def print_tree(root):
    if(root==None): # Edge Case
        return
    
    print(f"{root.data}:",end = "")

    for eachChild in root.children:
        print(eachChild.data,end = ",")

    print()

    for eachChild in root.children:
        print_tree(eachChild)


def count_node(root):
    if (root==None):
        return 0 
    number_of_nodes = 1
    for child in root.children:
        number_of_nodes = number_of_nodes + count_node(child)
    return number_of_nodes

def height_of_a_tree(root):
    if(root==None):
        return 0
    
    height = 1
    max_child_height = 0

    for eachChild in root.children:
        max_child_height = max(max_child_height,height_of_a_tree(eachChild))

    height = height + max_child_height
    return height


# root1, root2, root3 = predifined_generic_tree_input()

# print(height_of_a_tree(root1))
# print(height_of_a_tree(root2))
# print(height_of_a_tree(root3))


# root1,root2,root3 = predifined_generic_tree_input()
# print(count_node(root1))
# print(count_node(root2))
# print(count_node(root3))
# root1, root2, root3 = predifined_generic_tree_input()

# print("Tree 1:")
# print_tree(root1)

# print("\nTree 2:")
# print_tree(root2)

# print("\nTree 3:")
# print_tree(root3)
