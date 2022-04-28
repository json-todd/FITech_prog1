"""
Box printing with error checking

Author: Tri Phung
StudentID: tuni.fi:K441912
COMP.CS.100 Programming 1

"""

def print_box(width:int, height:int, mark:str):
    """Draw a box with width x height in the mark

    Args:
        width (int): the width of the box
        height (int): the height of the box
        mark (char): the mark displayed
    """
    box = ""
    
    width = int(width); height = int(height)
    for row in range(height):
        box += width * mark
        if row != height-1:
           box += "\n"
        else:
            continue
        
    print(box)
    


def main():

    while True:
        width = input("Enter the width of a frame: ")
        try:
            width = int(width)
            break
        except:
            continue
    
    while True:
        height = input("Enter the height of a frame: ")
        try:
            height = int(height)
            break
        except:
            continue
    
    mark = input("Enter a print mark: ")

    print()
    print_box(width, height, mark)


if __name__ == "__main__":
    main()
