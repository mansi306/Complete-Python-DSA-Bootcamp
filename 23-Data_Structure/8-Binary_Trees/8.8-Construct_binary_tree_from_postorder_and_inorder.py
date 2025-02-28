from collections import deque

class BT:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def construct_tree_from_Inorder_and_Postorder(inorder, postorder, inS, inE, poS, poE):
    # Base case: if indices are invalid
    if poS > poE or inS > inE:
        return None

    # The root is the last element in the postorder segment
    root_data = postorder[poE]
    root = BT(root_data)

    # Find the root index in inorder array
    rootIndexInInorder = -1
    for i in range(inS, inE + 1):
        if inorder[i] == root_data:
            rootIndexInInorder = i
            break

    if rootIndexInInorder == -1:
        print("Root not found in Inorder, please check logic")
        return None

    # Calculate the sizes of the left and right subtrees
    # Left subtree is between inS and rootIndexInInorder - 1
    # Right subtree is between rootIndexInInorder + 1 and inE
    left_size = rootIndexInInorder - inS

    # Recursively construct the left and right subtrees
    root.left = construct_tree_from_Inorder_and_Postorder(
        inorder, postorder, inS, rootIndexInInorder - 1, poS, poS + left_size - 1
    )
    root.right = construct_tree_from_Inorder_and_Postorder(
        inorder, postorder, rootIndexInInorder + 1, inE, poS + left_size, poE - 1
    )

    return root

def print_level_wise(root):
    if root is None:
        return None

    queue = deque([root])
    while queue:
        current_node = queue.popleft()
        print(f"{current_node.data}:", end=" ")

        if current_node.left:
            print(f"L-> {current_node.left.data}", end=", ")
            queue.append(current_node.left)
        else:
            print(f"L-> None", end=", ")

        if current_node.right:
            print(f"R-> {current_node.right.data}")
            queue.append(current_node.right)
        else:
            print(f"R-> None")

# Example usage:
postorder = [4, 5, 2, 6, 3, 1]  # Postorder traversal
inorder = [4, 2, 5, 1, 3, 6]  # Inorder traversal
n = len(inorder)

# Construct the binary tree
root = construct_tree_from_Inorder_and_Postorder(inorder, postorder, 0, n - 1, 0, n - 1)

# Print the tree level-wise
print_level_wise(root)
