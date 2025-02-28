from collections import deque 
class BT:
    def __init__(self,data):
        self.data = data 
        self.left = None
        self.right = None

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
    # return root 

root = BT(1)
root.left = BT(2)
root.right = BT(3)
print_level_wise(root)

        
    
