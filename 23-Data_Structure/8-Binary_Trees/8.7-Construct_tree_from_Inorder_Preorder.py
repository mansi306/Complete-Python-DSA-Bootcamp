from predefinedBT import predefined_binary_tree_inputs
from collections import deque
class BT:
    def __init__(self,data):
        self.data = data 
        self.left = None
        self.right = None

def construct_tree_from_Inorder_and_Preorder(inorder,preorder,inS,inE,prS,prE):
    if (prS>prE or inS>inE):
        return None
    
    root_data = preorder[prS]
    root = BT(root_data)
    rootIndexInInorder = -1
    for i in range(inS,inE+1):
        if (inorder[i]==root_data):
            rootIndexInInorder = i 
            break 
    
    if (rootIndexInInorder==-1):
        print("Root not found in Inorder, please check logic")
        return None 
    linS = inS
    linE = rootIndexInInorder - 1
    lprS = prS + 1
    lprE = lprS + (linE-linS)

    rinS = rootIndexInInorder + 1
    rinE = inE
    rprS = lprE + 1
    rprE = prE

    root.left = construct_tree_from_Inorder_and_Preorder(inorder,preorder,linS,linE,lprS,lprE)
    root.right = construct_tree_from_Inorder_and_Preorder(inorder,preorder,rinS,rinE,rprS,rprE)
    return root 

def print_level_wise(root):
    if (root==None):
        return None
    
    queue = deque([root])
    while queue:
        current_node = queue.popleft()
        print(f"{current_node.data}:",end=" ")
        if current_node.left:
            print(f"L-> {current_node.left.data}",end=",")
            queue.append(current_node.left)
        else:
            print(f"L-> None",end=",")

        if current_node.right:
            print(f"R-> {current_node.right.data}")
            queue.append(current_node.right)
        else:
            print(f"R-> None")

preorder = [1,2,4,5,3,6]
inorder = [4,2,5,1,3,6]
n = len(inorder)
root = construct_tree_from_Inorder_and_Preorder(inorder,preorder,0,n-1,0,n-1)
print_level_wise(root)