# Temporary Head Technique
# When we solve linked list problems, we often encounter edge cases that involve the head of a linked list. Common edge cases involving the head of a linked list include:

# Deleting the current head of a linked list
# Adding a new element to the front of a linked list
# Reducing a linked list containing only one node to an empty list
# Adding a new node to an empty list
# A common technique for handling these edge cases is creating a temporary head node. To apply this technique, an extra node object is created to serve as the temporary head of the list. We can use the temporary head as a placeholder that allows us to easily add items to an empty linked list or manipulate the actual head of a list as if it were any other node.

# Example Usage:

# The following function accepts the head of a linked list and a value and deletes the first node in the list with the specified value. It returns the head of the modified list.

# Example Input List: 1->2->4
# Example Input: head = 1, val = 2
# Expected Return Value: 1 
# Expected Return List: 1->4


class Node:
    def __init__(self, val, next=None):
        self.value = val
        self.next = next
    
def delete_node(head, val):
    temp_head = Node("temp") # Initialize a temporary head node
    temp_head.next = head    # Point the temporary head at the input list
    
    # Traverse the list
    previous = temp_head
    current = head
    while current:
        if current.value == val:          # If the current node is the node to delete
            previous.next = current.next  # Delete the node
            break                         # Break out of the loop

        previous = current
        current = current.next
    return temp_head.next # Return the head of the input list