"""
Then, write a method attack() that takes 
in a Pokemon object opponent and decreases 
opponent's hp by their self's damage amount.
"""

class Pokemon:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp  # Hit points
        self.damage = damage  # The amount of damage this pokemon does to its opponent every attack

    def attack(self, opponent):
        opponent.hp -= self.damage
        if opponent.hp <= 0:
            opponent.hp = 0
            print(f"{opponent.name} fainted")
        else:
            print(f"{self.name} dealt {self.damage} damage to {opponent.name}")


pikachu = Pokemon("Pikachu", 35, 20)
bulbasaur = Pokemon("Bulbasaur", 45, 30) 

opponent = bulbasaur
pikachu.attack(opponent)

"""
decrease opponents hp -1 
if opponent is 0 or less - 0 and fainted 
otherwise name damage
"""



class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def add_first(head, new_node):
    new_node.next = head
    #head = new_node.next
    return new_node

    # new_node = head
    # head = head.next

#create python list as a linked list 
wigglytuff = Node("Wigglytuff")
jigglypuff = Node("Jigglypuff", wigglytuff)
# jigglypuff.next = wigglytuff

print(jigglypuff.value, "->", jigglypuff.next.value)
# print(wigglytuff.value, "->", wigglytuff.next)

new_node = Node("Ditto")
jigglypuff = add_first(jigglypuff, new_node)

print(jigglypuff.value, "->", jigglypuff.next.value)
print(jigglypuff.next.value)

"""
Write a function get_tail() that 
takes in the head of a linked list as a parameter.

It should print out the value of the tail of the list.
"""


def get_tail(node):
	while node:
        print(node.value)
        node = node.next

get_tail(new_node)
# head = num1
# tail = get_tail(num1)
# print(tail)

