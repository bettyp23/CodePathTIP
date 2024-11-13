"""
Input: root = 1
Expected Output: True
"""
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Constructing the tree
# Level 1
root = TreeNode(1)

# Level 2
root.left = TreeNode(2)
root.right = TreeNode(2)

# Level 3
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

def is_mirror(left, right):
    if not left and not right:
        return True  # Both are None, hence symmetric
    if not left or not right:
        return False  # Only one is None, hence not symmetric
    if left.val != right.val:
        return False  # Values do not match, hence not symmetric
    # Recursively check the outer pairs and the inner pairs for symmetry
    return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)

def is_symmetric(root):
    if not root:
        return True  # An empty tree is symmetric.
    return is_mirror(root.left, root.right)

print(is_symmetric(root))