from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def level_order(root):
  # if the tree is empty
    if root is None:
        # return an empty list
        return []
    
    # create a new empty queue
    queue = deque()
    # create a list of nodes we have already explored
    visited = []

    # append the root of the tree to the queue
    queue.append(root)

    # while there are still nodes to explore
    while queue:
        # pop next node off the queue
        current_node = queue.popleft()

        # add the root to list of visited nodes
        visited.append(current_node.val)

        # if the current node has a left child
        if current_node.left is not None:
            # add the left child to the queue
            queue.append(current_node.left)

        # if the current node has a right child
        if current_node.right is not None:
            # add the right child to the queue
            queue.append(current_node.right)

    # return the list of visited nodes
    return visited


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

print(level_order(root))  # Expected output: [4, 2, 6, 1, 3]