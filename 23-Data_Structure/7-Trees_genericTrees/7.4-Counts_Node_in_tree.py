from GenericTreesInput import GenericTreeNode,predifined_generic_tree_input

def count_node(root):
    if (root==None):
        return 0 
    number_of_nodes = 1
    for child in root.children:
        number_of_nodes = number_of_nodes + count_node(child)
    return number_of_nodes

root1,root2,root3 = predifined_generic_tree_input()
print(count_node(root1))
print(count_node(root2))
print(count_node(root3))