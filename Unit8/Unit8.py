class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

node_one = TreeNode(10)
node_one.left = TreeNode(4)
node_one.right = TreeNode(6)


def check_tree(root):
    if root.left.val + root.right.val == root.val:
        return True
    else:
        return False



def left_most(root):
    if root is None:
        return None

    if root.left is None:
        return root.val
    else:
        return left_most(root.left)

print(left_most(node_one))


def right_most(root):
    if root is None:
        return None

    if root.right is None:
        return root.val
    else:
        return right_most(root.right)

print(left_most(node_one))

def inorder_traversal(root, result = None):
    if result is None:
        result = []

    if root is None:
        return result
    
    inorder_traversal(root.left, result)
    result.append(root.val)
    inorder_traversal(root.right, result)
    return result

print(inorder_traversal(node_one))

"""""""""""""""







