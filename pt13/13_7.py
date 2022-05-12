"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

Body Mass Index template
"""

from tkinter import *


class Userinterface:

    def __init__(self):
        self.__mainwindow = Tk()

        # TODO: Create an Entry-component for the weight.
        self.__weight_value = Entry(self.__mainwindow)
        self.__weight_label = Label(self.__mainwindow,
                                   text = "Weight (kg)")

        # TODO: Create an Entry-component for the height.
        self.__height_value = Entry(self.__mainwindow)
        self.__height_label = Label(self.__mainwindow,
                                   text = "Height (cm)")

        # TODO: Create a Button that will call the calculate_BMI-method.
        # TODO: Change the colour of the Button to something else than
        #       the default colour.
        self.__calculate_button = Button(self.__mainwindow,
                                         text="Get BMI",
                                         command=self.calculate_BMI)

        # TODO: Create a Label that will show the decimal value of the BMI
        #      after it has been calculated.
        self.__result_text = Label(background="white",
                                   text="BMI")

        # TODO: Create a Label that will show a verbal description of the BMI
        #       after the BMI has been calculated.
        self.__explanation_text = Label(background="white",
                                        text="BMI desc.")

        # TODO: Create a button that will call the stop-method.
        self.__stop_button = Button(background="red",
                                    text="stop",
                                    command=self.stop)

        # TODO: Place the components in the GUI as you wish.
        # If you read the Gaddis book, you can use pack here instead of grid!
        self.__weight_label.grid(row=0,column=0,sticky=E)
        self.__weight_value.grid(row=0,column=1,sticky=E)
        self.__height_label.grid(row=0,column=2,sticky=E)
        self.__height_value.grid(row=0,column=3,sticky=E)
        self.__calculate_button.grid(row=0,column=4,sticky=E+W)
        self.__stop_button.grid(row=4,column=4,sticky=E+S)
        self.__result_text.grid(row=1,column=1,sticky=E+W)
        self.__explanation_text.grid(row=1,column=3, sticky=E+W)

    # TODO: Implement this method.
    def calculate_BMI(self):
        """
        Part b) This method calculates the BMI of the user and
        displays it. First the method will get the values of
        height and weight from the GUI components
        self.__height_value and self.__weight_value.  Then the
        method will calculate the value of the BMI and show it in
        the element self.__result_text.

        Part e) Last, the method will display a verbal
        description of the BMI in the element
        self.__explanation_text.
        """
        error_message = ""
        weight = self.__weight_value.get()
        height = self.__height_value.get()
        try:
            weight = float(weight)
            height = float(height)/ 100

            try:
                assert weight > 0; assert height > 0
            except: 
                error_message = "Error: height and weight must be positive."
              
        except:
          error_message = "Error: height and weight must be numbers."

        if error_message:
            
            self.__explanation_text.configure(text=error_message)
            self.reset_fields()
            return

        bmi = round(weight / height ** 2, 2)
        self.__result_text.configure(text=bmi)
      
        explain_text = self.bmi_explain(bmi)
        self.__explanation_text.configure(text=explain_text)

        return

    # TODO: Implement this method.      
    def reset_fields(self):
        """
        In error situations this method will zeroize the elements
        self.__result_text, self.__height_value, and self.__weight_value.
        """

        self.__height_value.delete(0, END)
        self.__weight_value.delete(0, END)
        self.__result_text.configure(text="")

    def bmi_explain(self, bmi):
        """
        Explain the condition from the body mass index
        """
        if 18.5 < bmi and bmi < 25:
            return "Your weight is normal."
        elif bmi < 18.5:
            return "You are underweight."
        elif bmi > 25:
            return "You are overweight."
      
    def stop(self):
        """
        Ends the execution of the program.
        """

        self.__mainwindow.destroy()

    def start(self):
        """
        Starts the mainloop.
        """
        self.__mainwindow.mainloop()


def main():
    # Notice how the user interface can be created and
    # started separately.  Don't change this arrangement,
    # or automatic tests will fail.
    ui = Userinterface()
    ui.start()


if __name__ == "__main__":
    main()
