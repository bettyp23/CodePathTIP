class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right

# node1 = TreeNode(1)

# node2 = TreeNode(1)

# node3 = TreeNode(1)

# node4 = TreeNode(1)

# node5 = TreeNode(1)

# node1.left = node2

# node1.right = node3

# node2.left = node4

# Node2.right = node5


# Create nodes for each value
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.left.left = TreeNode(7)
root.left.right = TreeNode(3)


def height(root):
    if root is None:
        return 0

    left_height = height(root.left)
    right_height = height(root.right)

    return 1 + max(left_height, right_height)

print(height(root))