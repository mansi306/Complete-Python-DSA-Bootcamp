from GenericTreesInput import predifined_generic_tree_input, print_tree
def height_of_a_tree(root):
    if(root==None):
        return 0
    
    height = 1
    max_child_height = 0

    for eachChild in root.children:
        max_child_height = max(max_child_height,height_of_a_tree(eachChild))

    height = height + max_child_height
    return height

root1 = predifined_generic_tree_input()
# result = height_of_a_tree(root1)
# print_tree(result)
print(height_of_a_tree(root1))