from collections import deque
class TreeNode:
    def __init__(self,data):
        self.data = data 
        self.children = []

def print_tree(root):
    if(root==None): # Edge Case
        return
    
    print(f"{root.data}:",end = "")

    for eachChild in root.children:
        print(eachChild.data,end = ",")

    print()

    for eachChild in root.children:
        print_tree(eachChild)


def take_input_level_wise():
    data = int(input("Enter the root data: "))
    root = TreeNode(data)

    queue = deque([root])

    while (len(queue)) != 0 :
        current_node = queue.popleft()

        num_children = int(input("Enter the number of Children for " + str(current_node.data)))

        for i in range(num_children):
            child_data = int(input(f"Enter the data for  child {i+1} of Node {current_node.data} : "))
            child_node = TreeNode(child_data)
            current_node.children.append(child_node)
            queue.append(child_node)
    
    return root

root = take_input_level_wise()
print_tree(root)

# def take_input():
#     data = int(input("Enter the data for the Node :"))
#     node = TreeNode(data)
#     num_children = int(input(f"Enter the number of Children for {data} : "))
#     for _ in range(num_children):
#         child = take_input()
#         node.children.append(child)
#     return node 


# root = take_input()
# print_tree(root)


# root = TreeNode(10)
# c1 = TreeNode(20)
# c2 = TreeNode(30)
# c3 = TreeNode(40)
# c4 = TreeNode(50)
# root.children.append(c1)
# root.children.append(c2)
# root.children.append(c3)
# root.children.append(c4)
# # print_tree(root)



