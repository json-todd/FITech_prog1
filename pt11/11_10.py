"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Author: Tri Phung
Student ID: K441912
"""

class Fraction:
    """
    This class represents one single fraction that consists of
    numerator (osoittaja) and denominator (nimittäjä).
    """

    def __init__(self, numerator, denominator):
        """
        Constructor. Checks that the numerator and denominator are of
        correct type and initializes them.

        :param numerator: int, fraction's numerator
        :param denominator: int, fraction's denominator
        """

        # isinstance is a standard function which can be used to check if
        # a value is an object of a certain class.  Remember, in Python
        # all the data types are implemented as classes.
        # ``isinstance(a, b´´) means more or less the same as ``type(a) is b´´
        # So, the following test checks that both parameters are ints as
        # they should be in a valid fraction.
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError

        # Denominator can't be zero, not in mathematics, and not here either.
        elif denominator == 0:
            raise ValueError

        self.__numerator = numerator
        self.__denominator = denominator

    def return_string(self):
        """
        :returns: str, a string-presentation of the fraction in the format
                       numerator/denominator.
        """

        if self.__numerator * self.__denominator < 0:
            sign = "-"

        else:
            sign = ""

        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"
        
    def simplify(self):
        """
        Simplify the fraction
        
        Return: object, the simplified form of the fraction
        """        
        gcd = greatest_common_divisor(self.__numerator, self.__denominator)
        return Fraction(int(self.__numerator/gcd), int(self.__denominator/gcd))
    
        
    def reciprocal(self):
        """The inverse of a fraction

        Returns:
            object: the inverse of the Fraction object
        """
        fration_object = Fraction(self.__denominator, self.__numerator)
        return fration_object
    
    def complement(self):
        """The fraction that adds up to 0

        Returns:
            object: opposite sign of the Fraction object
        """
        fraction_object =  Fraction(-self.__numerator, self.__denominator)
        return fraction_object
    
    def multiply(self, other_fraction):
        """Multiply two fractions

        Args:
            other_fraction (object): Other Fraction object

        Returns:
            object: result of multiplying two fractions
        """
        numerator_mult = self.__numerator * other_fraction.__numerator
        denominator_mult = self.__denominator * other_fraction.__denominator
        return Fraction(numerator_mult, denominator_mult)
    
    def divide(self, other_fraction):
        """Division of two fractions

        Args:
            other_fraction (object): Other fraction object

        Returns:
            object: result of dividing two fractions
        """
        other_fraction_reciprocal = other_fraction.reciprocal()
        return self.multiply(other_fraction_reciprocal)
    
    def expand(self, other_fraction):
        first_numerator = self.__numerator * other_fraction.__denominator
        second_numerator = other_fraction.__numerator * self.__denominator
        denominator_common = self.__denominator * other_fraction.__denominator
        return (first_numerator, second_numerator, denominator_common)
   
    def add(self, other_fraction):
        """Addition of two fractions

        Args:
            other_fraction (object): Other Fraction object

        Returns:
            Object: Sum of two fractions
        """
        first_numerator, second_numerator, denominator_common = self.expand(other_fraction)
        
        return Fraction(first_numerator + second_numerator, denominator_common)
    
    def deduct(self, other_fraction):
        """Deduct one fraction from the other

        Args:
            other_fraction (object): Other Fraction object
            
        Returns:
            Object: Result of deduction of two fractions
        """
        first_numerator, second_numerator, denominator_common = self.expand(other_fraction)
        
        return Fraction(first_numerator - second_numerator, denominator_common)
    
    def __lt__(self, other_fraction):
        (first_numerator, second_numerator, common_denominator) = self.expand(other_fraction)
        if first_numerator < second_numerator:
            return True
        else:
            return False
        
    def __gt__(self, other_fraction):
        (first_numerator, second_numerator, common_denominator) = self.expand(other_fraction)
        if first_numerator > second_numerator:
            return True
        else:
            return False
    
    def __str__(self):
        return self.return_string()

def greatest_common_divisor(a, b):
    """
    Euclidean algorithm. Returns the greatest common
    divisor (suurin yhteinen tekijä).  When both the numerator
    and the denominator is divided by their greatest common divisor,
    the result will be the most reduced version of the fraction in question.
    """

    while b != 0:
        a, b = b, a % b

    return a

def input_to_Fraction_obj(string_input):
    """convert the input into a Fraction object

    Args:
        string_input (str): input by users

    Returns:
        object: a Fraction object
    """
    input_split = string_input.split('/')
    return Fraction(int(input_split[0]), int(input_split[1]))

def main():
    
    fraction_dict = {}
    
    while True:
        command = input("> ")
        if command == "quit":
            print("Bye bye!")
            break
        
        elif command == "add":
            input_fraction = input("Enter a fraction in the form integer/integer: ")
            name_fraction = input("Enter a name: ")
            fraction_obj = input_to_Fraction_obj(input_fraction)
            fraction_dict[name_fraction] = fraction_obj
            
        elif command == "print":
            look_up_name = input("Enter a name: ")
            if fraction_dict.get(look_up_name, False):
                print(f"{look_up_name} = {fraction_dict[look_up_name]}")
            else:
                print(f"Name {look_up_name} was not found")
            
        elif command == "list":
            if len(fraction_dict) == 0: continue
            
            for name in sorted (fraction_dict.keys()):
                print(f"{name} = {fraction_dict[name]}")
        
        elif command == "*":
            first_operand_key = input("1st operand: ")
            if fraction_dict.get(first_operand_key, False):
                first_operand = fraction_dict[first_operand_key]
            else:
                print(f"Name {first_operand_key} was not found")
                continue
            
            second_operand_key = input("2nd operand: ")
            if fraction_dict.get(second_operand_key, False):
                second_operand = fraction_dict[second_operand_key]
            else:
                print(f"Name {second_operand_key} was not found")
                continue
            
            mult = first_operand.multiply(second_operand)
            print(f"{first_operand} * {second_operand} = {mult}")
            print(f"simplified {mult.simplify()}")
        
        elif command == "file":
            file_input = input("Enter the name of the file: ")
            try:
                fh = open(file_input)
            except:
                print("Error: the file cannot be read.")
                continue
                
            for line in fh.readlines():
                
                if line.find("=") == -1 or line.find("/") == -1:
                    print("Error: the file cannot be read.")
                    break
                
                name = line[0 : line.find("=")]
                numerator = line[line.find("=") + 1 : line.find("/")]
                denominator = line[line.find("/") + 1 : -1]
                
                
                fraction_dict[name] = Fraction(int(numerator), int(denominator))
                
            fh.close()
        
        else:
            print("Unknown command!")
            continue
        
   
if __name__ == "__main__":
    main()