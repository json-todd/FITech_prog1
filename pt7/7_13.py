"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Author: Tri Phung
Student ID: K441912
Email: tri.phung@tuni.fi

Template for sorting by price assignment.
"""

PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.70, "grasshopper": 13.25,
    "sushi": 19.90, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}


def main():
    # TODO
    for price_item in sorted( PRICES.items(), key = lambda kv: kv[1] ):
        print(f"{price_item[0]} {price_item[1]:.2f}")


if __name__ == "__main__":
    main()
