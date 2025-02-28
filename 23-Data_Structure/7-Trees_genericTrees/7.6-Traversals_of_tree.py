from GenericTreesInput import predifined_generic_tree_input
def preorder_traversals(root):
    if (root==None):
        return 
    
    print(root.data,end=' ')
    for eachChild in root.children:
        preorder_traversals(eachChild)


def postorder_traversals(root):
    if (root==None):
        return root 
    for eachChild in root.children:
        postorder_traversals(eachChild)
    print(root.data,end=' ')

root1 = predifined_generic_tree_input()
print("Preorder Traversing : ")
print(preorder_traversals(root1))
print("Postorder Traversing : ")
print(postorder_traversals(root1))