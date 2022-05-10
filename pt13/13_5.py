"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Author: Tri Phung
StudentID: tuni.fi:K441912
COMP.CS.100 Programming 1

Code template for counter program.
"""

from tkinter import *


class Counter:
    def __init__(self):
        self.__main_window = Tk()
        
        self.__counter = 0

        # Label displaying the current value of the counter.
        self.__current_value_label = Label(self.__main_window, text = self.__counter)  
        self.__current_value_label.pack()
        
        # Button which resets counter to zero.
        self.__reset_button = Button(self.__main_window, text = "Reset", command = self.reset)
        self.__reset_button.pack(side=LEFT)
        
        # Button which increases the value of the counter by one.   
        self.__increase_button = Button(self.__main_window, text = "Increase", command = self.increase)
        self.__increase_button.pack(side=LEFT)
        
        # Button which decreases the value of the counter by one.
        self.__decrease_button = Button(self.__main_window, text = "Decrease", command = self.decrease)
        self.__decrease_button.pack(side=LEFT)
        
        # Button which quits the program.
        self.__quit_button = Button(self.__main_window, text="Quit", command=self.quit)
        self.__quit_button.pack(side=LEFT)
        
        self.__main_window.mainloop()
        # TODO: You have to create one label and four buttons and store
        #       them in the following attributes:
        #
        #       self.__current_value_label  # Label displaying the current value of the counter.
        #       self.__reset_button         # Button which resets counter to zero.
        #       self.__increase_button      # Button which increases the value of the counter by one.
        #       self.__decrease_button      # Button which decreases the value of the counter by one.
        #       self.__quit_button          # Button which quits the program.
        #
        #       Make sure you name the components exactly as shown above,
        #       otherwise the automated tests will fail.

    # TODO: Implement the rest of the needed methods here.
    
    def reset(self):
        self.__counter = 0
        self.__current_value_label.configure(text = self.__counter)
    
    def increase(self):
        self.__counter += 1
        self.__current_value_label.configure(text = self.__counter)
    
    def decrease(self):
        self.__counter -= 1
        self.__current_value_label.configure(text = self.__counter)
    
    def quit(self):
        self.__main_window.destroy()
        


def main():
    # There is no need to modify the main function.
    # As a matter of fact, automated tests ignore main
    # once again.

    Counter()


if __name__ == "__main__":
    main()
