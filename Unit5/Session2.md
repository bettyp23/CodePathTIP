10/17/14

Tracing Code
-> Keeping track of what is happening inside the computer when it runs
    Which line
    which  variables
    how does this code change the variables
    ->easier to plan and solve problems

Linked Lists
-> why useful

linked lists can dynamically grow
- removing a node is O(1)

Attributes of a linked list node:
    Removing or inserting a node at the beginning of a linked list is O(1) (constant time), as you only need to update pointers.
    For arrays, removing or adding an element requires shifting other elements, which takes O(n) time.

1. Singly Linked List
In a singly linked list, each node has a data attribute and a next pointer that points to the next node in the sequence.
    class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
This creates a linked list that looks like: 1 -> 2 -> 3 -> None

def print_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

def insert_at_beginning(head, value):
    new_node = Node(value)
    new_node.next = head
    return new_node
Deleting a Node
To delete a node, adjust the next pointer of the previous node to skip over the node being deleted.


