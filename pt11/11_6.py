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
        Change the fraction object to its simplified form
        """        
        gcd = greatest_common_divisor(self.__numerator, self.__denominator)
        self.__numerator = int(self.__numerator/gcd)
        self.__denominator = int(self.__denominator/gcd)
        
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
