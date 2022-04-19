"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

This program models a character adventuring in a video game.

Author: Tri Phung
Student ID: K441912
Email: tri.phung@tuni.fi
"""

from unicodedata import name


class Character:
    """
    This class defines what a character is int he game and what
    he or she can do.
    """   
    def __init__(self, name, hp):
        # Instantiate an object the `name` and `hp` (hitpoints) of the character
        # The hero as a `backpack` attribute with datastructure as dictionary
        
        self.name: str = name
        self.hp: int = hp
        self._backpack: dict = {}
        
    def give_item(self, item: str) -> None:
        # Add item into backpack
        
        self._backpack[item] = self._backpack.get(item, 0) + 1
        
    def remove_item(self, item) -> bool:
        # Remove item from backpack
        # If number of item reaches zero, remove its property from datastructure
        
        if item not in self._backpack:
            return False
        elif self._backpack.get(item) > 0:
            self._backpack[item] -= 1
        
        if self._backpack.get(item) == 0:
            self._backpack.pop(item)

        return True
        
    def printout(self) -> None:
        # Print out in format of name, amount and associated items
        
        name_line: str = f"Name: {self.name}\n"
        hp_line: str = f"Hitpoints: {self.hp}\n"
        item_line_list: list = []
        item_line: str = ""
    
        if len( self._backpack.keys() ) == 0:
            item_line = '  --nothing--'
        else:
            for item in sorted( self._backpack.keys() ):
                amount = self._backpack[item]
                item_line_list.append(f"  {amount} {item}")
            
            item_line = "\n".join(item_line_list)
        
        print( name_line + hp_line + item_line)

    def pass_item(self, item, target) -> bool: 
        """
        Passes (i.e. transfers) an item from one person (self)
        to another (target).

        :param item: str, the name of the item in self's inventory
                     to be given to target.
        :param target: Character, the target to whom the item is to
                     to be given.
        :return: True, if passing the item to target was successful.
                 False, it passing the item failed for any reason.
        """

        is_remove_success= self.remove_item(item)
        
        if is_remove_success:
            target.give_item(item)
            return True
        else:
            return False

    def attack(self, target, weapon):
        """
        A character (self) attacks the target using a weapon.
        This method will also take care of all the printouts
        relevant to the attack.

        There are three error conditions:
          (1) weapon is unknown i.e. not a key in WEAPONS dict.
          (2) self does not have the weapon used in the attack
          (3) character tries to attack him/herself.
        You can find the error message to printed in each case
        from the example run in the assignment.

        The damage the target receives if the attack succeeds is
        defined by the weapon and can be found as the payload in
        the WEAPONS dict. It will be deducted from the target's
        hitpoints. If the target's hitpoints go down to zero or
        less, the target is defeated.

        The format of the message resulting from a successful attack and
        the defeat of the target can also be found in the assignment.

        :param target: Character, the target of the attack.
        :param weapon: str, the name of the weapon used in the attack
                       (must exist as a key in the WEAPONS dict).
        :return: True, if attack succeeds.
                 False, if attack fails for any reason.
        """

        # TODO: the implementation of the method
        
        attack_failure_string: str = "Attack fails: "
        failure_string_len: int = len(attack_failure_string)
        
        if weapon not in WEAPONS: 
            attack_failure_string += f'unknown weapon \"{weapon}\".'
        elif self.name == target.name:
            attack_failure_string += f'{self.name} cannot attack him/herself.'
        elif not self._backpack.get(weapon, 0):
            attack_failure_string += f'{self.name} doesn\'t have \"{weapon}\".'
        
        if failure_string_len < len(attack_failure_string):
            print(attack_failure_string)
            return False
        
        success_attack_printout = f"{self.name} attacks {target.name} delivering {WEAPONS[weapon]} damage."
        print(success_attack_printout)
        return True
        
       


WEAPONS = {
    # Weapon          Damage
    #--------------   ------
    "elephant gun":     15,
    "gun":               5,
    "light saber":      50,
    "sword":             7,
}


def main():
    conan = Character("Conan the Barbarian", 10)
    deadpool = Character("Deadpool", 45)


    # Testing the pass_item method

    for test_item in ["sword", "sausage", "plate armor", "sausage", "sausage"]:
        conan.give_item(test_item)

    for test_item in ["gun", "sword", "gun", "sword", "hero outfit"]:
        deadpool.give_item(test_item)

    conan.pass_item("sword", deadpool)
    deadpool.pass_item("hero outfit", conan)
    conan.pass_item("sausage", deadpool)
    deadpool.pass_item("gun", conan)
    conan.pass_item("sausage", deadpool)
    deadpool.pass_item("gun", conan)

    print("-" * 5, "How are things after passing items around", "-" * 20)
    conan.printout()
    deadpool.printout()


    # Testing a fight i.e. the attack method

    print("-" * 5, "Let's see how a fight proceeds", "-" * 32)

    # Conan's turn
    conan.attack(deadpool, "sword") # Conan doesn't have a sword.
    conan.attack(conan, "gun")      # A character is not allowed to attack himself.
    conan.attack(conan, "pen")      # Pen is not a known weapon in WEAPONS dict.
    conan.attack(deadpool, "gun")   # Attack with a gun.

    # Deadpool retaliates
    deadpool.attack(conan, "sword") # Deadpool has a sword.

    # Conan's 2nd turn
    conan.attack(deadpool, "gun")   # Attack with a gun again.

    # Deadpool strikes back again and Conan drops "dead".
    deadpool.attack(conan, "sword")

    print("Are You Not Entertained?!")

    print("-" * 5, "How are things after beating each other up", "-" * 20)

    conan.printout()
    deadpool.printout()


if __name__ == "__main__":
    main()
