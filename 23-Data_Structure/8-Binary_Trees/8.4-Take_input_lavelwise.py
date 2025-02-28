from collections import deque
class BT:
    def __init__(self,data):
        self.data = data 
        self.left = None
        self.right = None

def print_Binary_tree(root):
    if (root==None):
        return 
    print(f"{root.data}:",end=" ")
    if (root.left != None):
        print(f"L-> {root.left.data}",end=",")
    else:
        print(f"L-> None",end=",")
    if (root.right != None):
        print(f"R-> {root.right.data}")
    else:
        print(f"R-> None")
    print_Binary_tree(root.left)
    print_Binary_tree(root.right)

def take_input_level_wise():
    data = int(input("Enter data value  for root : "))
    if (data==-1):
        return None
    root = BT(data)
    queue = deque([root])
    while (len(queue)!=0):
        current_node = queue.popleft()
        left_child_data = int(input(f"Enter Left child for {current_node.data}: "))
        if left_child_data!=-1:
            left_node = BT(left_child_data)
            current_node.left = left_node
            queue.append(left_node)
        

        right_child_data = int(input(f"Enter Right child for {current_node.data}: "))
        if right_child_data!=-1:
            right_node = BT(right_child_data)
            current_node.right = right_node
            queue.append(right_node)
    return root 
        





root = BT(1)
root.left = BT(2)
root.right = BT(3)
take_input_level_wise()
print(print_Binary_tree(root))