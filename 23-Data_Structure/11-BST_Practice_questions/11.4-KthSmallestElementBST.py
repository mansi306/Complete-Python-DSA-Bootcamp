class BST:
    def __init__(self,val):
        self.val = val 
        self.left = None 
        self.right = None

def kth_smallest(root, k):
    # Core logic for the learner to implement
    n = 0 
    stack = []
    cur = root
    while stack or cur :
        while cur :
            stack.append(cur)
            cur = cur.left 
        cur = stack.pop()
        n+= 1 
        if n== k :
            return cur.val 
        cur = cur.right 


root = [3,1,4,2]
k = 2
print(kth_smallest(root,k))