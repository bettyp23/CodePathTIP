"""
Add a line of code (outside of the class) 
to instantiate an instance of the class 
Pokemon and store it in a variable named 
my_pokemon. The Pokemon instance created 
should have name "Pikachu" and its types should be ["Electric"].
"""


class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

my_pokemon = Pokemon("Pikachu", ["Electric"])
print(my_pokemon.name)


"""
Step 1: Add the print_pokemon definition below to your code on Replit.

Step 2: Instantiate an instance of the class Pokemon and store it in a 
variable named squirtle. The Pokemon instance created should have name 
"Squirtle" and its types should be ["Water"].

Step 3: Call the method print_pokemon() on your new Pokemon instance squirtle.

"""

class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

    def print_pokemon(self):
        print({
            "name": self.name,   # Output: "name": "Squirtle",
            "types": self.types, # Output: "types": ["Water"],
            "is_caught": self.is_caught # Output: "is_caught": False
        })

    def catch(self):
        self.is_caught = True

    def choose(self):
        if self.is_caught == True:
            print(self.name + " I choose you!")
        else:
            print(self.name + " is wild! Catch them if you can!")

    def add_type(self, new_type):
        self.types.append(new_type)


def get_by_type(my_pokemon, pokemon_type):
	result = []

    for pokemon in my_pokemon:
        if pokemon.pokemon_type == "Normal":
            result.append(pokemon)

    return result

    # initializing pokemons
jigglypuff = Pokemon("Jigglypuff", ["Normal", "Fairy"])
diglett = Pokemon("Diglett", ["Ground"])
meowth = Pokemon("Meowth", ["Normal"])
pidgeot = Pokemon("Pidgeot", ["Normal", "Flying"])
blastoise = Pokemon("Blastoise", ["Water"])

my_pokemon = [jigglypuff, diglett, meowth, pidgeot, blastoise]
normal_pokemon = get_by_type(my_pokemon, "Normal")
print(normal_pokemon)

# squirtle = Pokemon("Squirtle", "water")
# squirtle.print_pokemon()

# squirtle.is_caught = True
# squirtle.print_pokemon()




"""
Update the Pokemon class with a new method catch() 
that takes in no parameters except self.

The method should update the Pokemon's is_caught 
attribute to True and not return any value.

"""



# my_pokemon = Pokemon("rattata", ["Normal"])
# my_pokemon.print_pokemon()

# my_pokemon.catch()
# my_pokemon.print_pokemon()

# my_pokemon = Pokemon("rattata", ["Normal"])
# my_pokemon.print_pokemon()

# my_pokemon.choose()
# my_pokemon.catch()
# my_pokemon.choose()

jigglypuff = Pokemon("Jigglypuff", ["Normal"])
jigglypuff.print_pokemon()

jigglypuff.add_type("Fairy")
jigglypuff.print_pokemon()