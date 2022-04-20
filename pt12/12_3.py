"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

This program models a character adventuring in a video game,
or more like, the stuff that the character carries around.

Author: Tri Phung
Student ID: K441912
Email: tri.phung@tuni.fi
"""

class Character:
    def __init__(self, name):
        # Construc an object the `name` of the character
        # The hero as a `backpack` attribute with datastructure as dictionary
        self.name: str = name
        self.backpack: dict = {}
        
    def give_item(self, item: str) -> None:
        # Add item into backpack
        self.backpack[item] = self.backpack.get(item, 0) + 1
    
    def remove_item(self, item) -> None:
        # Remove item from backpack
        # If number of item reaches zero, remove its property from datastructure
        if self.backpack.get(item, 0) > 0:
            self.backpack[item] -= 1
        
        if self.backpack.get(item) == 0:
            self.backpack.pop(item)
    
    def printout(self) -> None:
        # Print out in format of name, amount and associated items
        name_line: str = f"Name: {self.name}\n"
        item_line_list: list = []
        item_line: str = ""
    
        if len( self.backpack.keys() ) == 0:
            item_line = '  --nothing--'
        else:
            for item in sorted( self.backpack.keys() ):
                amount = self.backpack[item]
                item_line_list.append(f"  {amount} {item}")
            
            item_line = "\n".join(item_line_list)
        
        print( name_line + item_line)
    
    def get_name(self) -> str:
        # Return the name of character
        return self.name
    
    def has_item(self, item) -> bool:
        # Return true if character has item in backpack
        return item in self.backpack
    
    def how_many(self, item) -> int:
        # Return amount of item in character's backpack
        return self.backpack.get(item, 0)

def main():
    character1 = Character("Conan the Barbarian")
    character2 = Character("Deadpool")

    for test_item in ["sword", "sausage", "plate armor", "sausage", "sausage"]:
        character1.give_item(test_item)

    for test_item in ["gun", "sword", "gun", "sword", "hero outfit"]:
        character2.give_item(test_item)

    character1.remove_item("sausage")
    character2.remove_item("hero outfit")

    character1.printout()
    character2.printout()

    for hero in [character1, character2]:
        print(f"{hero.get_name()}:")

        for test_item in ["sausage", "sword", "plate armor", "gun", "hero outfit"]:
            if hero.has_item(test_item):
                print(f"  {test_item}: {hero.how_many(test_item)} found.")
            else:
                print(f"  {test_item}: none found.")


if __name__ == "__main__":
    main()
