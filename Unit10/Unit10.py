

"""""
# Outer function
def print_sum(x, y):
    
    # Inner function
    def get_sum():
        return x + y

    total = get_sum()
    print(f"{x} + {y} is {total}")

print_sum(1, 2) # Prints: 1 + 2 is 3
"""""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    def inorder(node, result):
        if node:
            inorder(node.left, result)  # Traverse the left subtree
            result.append(node.val)     # Visit the root
            inorder(node.right, result) # Traverse the right subtree
    
    result = []
    inorder(root, result)
    return result



def is_valid(s):
	pass

Example Usage:

Example #1:
Input: s = "()"
Expected Output: True

Example #2:
s = "()[]{}"
Expected Output: True

Example #3: 
s = "(())"
Expected Output: True

Exampel #4:
s = "(]"
Expected Output: False


