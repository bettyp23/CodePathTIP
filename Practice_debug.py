
#
# Complete the 'range_sum_bst' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. TreeNode root
#  2. INTEGER low
#  3. INTEGER high
#
'''
tree here

Example Input Tree

3 types of traversals(visiting each node "going through every hole")
    - in order
        * 
    - pre order
        * (node.val) -> (node.right) -> (node.left)
    - post order
        * 

recursion - using a function that calls itself

def callFunction(x, y)
    # base case
    return callFunction

main:
    x+x
    y+y
    callFunction(x, y)

node.val = none
def preorder_dfs(node, list[]):
    # base case terminates recursive call
    if node:
        return nothing/message/val/node/True/False/Any
    # evaluate curNode
    print(node.val)
    # visit left child
    preorder_dfs(node.left)
    # visit right child
    preorder_dfs(node.right)

stackframe:
            main 
            dfs(10) 45
            dfs(5) 45
            dfs(3) 45 <-
            dfs(none(3left)) 43
            dfs(none(3right))
            dfs(7) 45
            dfs(none)
            dfs(none)
            dfs(15) 45
            dfs(none)
            dfs(18)
            dfs(none)
            dfs(none)

terminal:
10
5
3
7
15
18
done

main:
    root(10) #whole tree
    preorder_dfs(root)   #print nodes preorder
    print(done)
    10
   /  \
  5    15
 / \     \
3   7    18
none
dfs - depth first search

bfs - recursion / queue

queue = deque([])

[3, 7, 8, more children] - in order bfs - breadth first search - level by level

queue.append(root)
sum = 0
while queue:
    curNode(5) = queue.popleft()
    if in range:
        add to sum
    # add 10's children into queue bc you want to go to them next
    #check if has children then append to queue
        queue.append(curNode.left)
        queue.append(curNode.right)

[8, 5, 8]


'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
def range_sum_bst(root, low, high):
    # Write your code here
    queue = deque([node])
    
    sum = 0
    
    while queue:
        node = queue.popleft()
        if node.left and node.right:
            range_sum_bst(node.left, low, high)
            range_sum_bst(node.right, low, high)

# function that returns list of node values in preorder

def preorder_dfs(node, result):

    if node is None:
        return result
    
    if node:
        result.append(node.val)
        preorder_dfs(node.left, result)
        preorder_dfs(node.right, result)
        
    return result


if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right = TreeNode(15)
    root.right.right = TreeNode(18)
    print("running preorder")

    print(preorder_dfs(root, []))


'''
    10
   /  \
  5    15
 / \     \
3   7    18
none 

def main:
    root(10)
    range_sum_bst(root, 7, 15)
'''