"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id:
Name:
Email:

Template for pricelist assignment.
"""

PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.7, "grasshopper": 13.25,
    "sushi": 19.9, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}


def main():
    # TODO
    while True:
        item = input('Enter product name: ').strip()
        
        if item == "":
            print('Bye!')
            break
        elif item not in PRICES:
            print(f'Error: {item} is unknown.')
        else:
            print(f'The price of {item} is {PRICES[item]:.2f} e')
        
            
    
    
    


if __name__ == "__main__":
    main()
