"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

Code template for Mölkky.
"""


# TODO:
# a) Implement the class Player here.
class Player():
    def __init__(self, name):
        self.name = name
        self.point = 0
        self.acq_point_hist = []
        
    def add_points(self, acquired_point: int) -> None:
        """After the throw, update the point of player

        Args:
            acquired_point (int): the point of the throw
        """
        self.point += acquired_point

        if self.point > 50:
            print(f"{self.name} gets penalty points!")
            self.point = 25
        
        self.warn()
            
        self.acq_point_hist.append(acquired_point)
    
    def get_name(self) -> str:
        """
        Returns:
            str: Name of player
        """
        return self.name
    
    def get_points(self) -> int:
        """
        Returns:
            int: Current point of player
        """
        return self.point
    
    def warn(self) -> None:
        """Print warning message if point is within the range of 40 to 49.
        """
        current_point = self.get_points()
        if current_point >= 40 and current_point <= 49:
            print(f"{self.name} needs only {50 - self.point} points. It's better to avoid knocking down the pins with higher points.")
    
    def calculate_point_avg(self) -> float:
        """Average of point acquired

        Returns:
            float: _description_
        """
        if len(self.acq_point_hist) == 0: return 0
        
        return sum(self.acq_point_hist)/len(self.acq_point_hist)
    
    def hit_percentage(self) -> float:
        """Calculate the occurence of non-zero-point throws divided by total throws

        Returns:
            float: hit percentage of player
        """
        if len(self.acq_point_hist) == 0: return 0
        
        return len([pts for pts in self.acq_point_hist if pts != 0]) / len(self.acq_point_hist) * 100
    
    def has_won(self) -> bool:
        """Return True if the player scores equals to 50; False otherwise
        """
        return self.point == 50

def main():
    # Here we define two variables which are the objects initiated from the
    # class Player. This is how the constructor of the class Player
    # (the method that is named __init__) is called!

    player1 = Player("Matti")
    player2 = Player("Teppo")

    throw = 1
    while True:

        # if throw is an even number
        if throw % 2 == 0:
            in_turn = player1

        # else throw is an odd number
        else:
            in_turn = player2

        pts = int(input("Enter the score of player " + in_turn.get_name() +
                        " of throw " + str(throw) + ": "))

        in_turn.add_points(pts)

        # TODO:
        # c) Add a supporting feedback printout "Cheers NAME!" here.
        if pts > in_turn.calculate_point_avg():
            print(f"Cheers {in_turn.get_name()}!")

        if in_turn.has_won():
            print("Game over! The winner is " + in_turn.get_name() + "!")
            return

        print("")
        print("Scoreboard after throw " + str(throw) + ":")
        print(player1.get_name() + ":", player1.get_points(), "p, hit percentage", f"{player1.hit_percentage():.1f}")  # TODO: d)
        print(player2.get_name() + ":", player2.get_points(), "p, hit percentage", f"{player2.hit_percentage():.1f}")  # TODO: d)
        print("")

        throw += 1


if __name__ == "__main__":
    main()
