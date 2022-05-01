"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Template for the product assignment.

Author: Tri Phung
StudentID: tuni.fi:K441912
COMP.CS.100 Programming 1
"""

class Product:
    """
    This class defines a simplified product for sale in a store.
    """

    def __init__(self, name: str, price: float, sale_perc:float = 0):
        self.__name = name
        self.__price = price
        self.__sale_perc = sale_perc
    
    def printout(self) -> None:
        """
        Print the items, initial offering price, and sale percentage
        """
        print(f"{self.__name}\n  price: {self.__price:.2f}\n  sale%: {self.__sale_perc:.2f}\n")
        
    
    def set_sale_percentage(self, sale_perc_new: float) -> None:
        """Set the sale percentage

        Args:
            sale_perc_new: float, new sale percentage
        """
        self.__sale_perc = sale_perc_new
        
    def get_price(self) -> float:
        return self.__price * (1 - self.__sale_perc / 100)
 

def main():
    ################################################################
    #                                                              #
    #  You can use the main-function to test your Product class.   #
    #  The automatic tests will not use the main you submitted.    #
    #                                                              #
    #  Voit käyttää main-funktiota Product-luokkasi testaamiseen.  #
    #  Automaattiset testit eivät käytä palauttamaasi mainia.      #
    #                                                              #
    ################################################################

    test_products = {
        "milk":   1.00,
        "sushi": 12.95,
    }

    for product_name in test_products:
        print("=" * 20)
        print(f"TESTING: {product_name}")
        print("=" * 20)

        prod = Product(product_name, test_products[product_name])

        prod.printout()
        print(f"Normal price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(10.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(25.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)


if __name__ == "__main__":
    main()
