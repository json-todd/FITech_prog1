"""
Author: Tri Phung
Email: tri.phung@tuni.fi
StudentID: tuni.fi:K441912
COMP.CS.100 Programming 1
Code template for the hottest hit song Yogi Bear
"""

def repeat_name(bear, repeat=2):
    """Print out three lines according to instructions.
    Must defined as this to complete unit test

    Args:
        bear (string): the name of the bear
        repeat (int): the number of line it will print out
    """
    output_string = ""
    
    the_name_so_nice_you_say_it_twice = bear + ", " + bear
    # https://www.youtube.com/watch?v=DhiISGr9LFc
    
    # Loop to repeat the lines
    for i in range(repeat): 
        output_string += the_name_so_nice_you_say_it_twice + " Bear" + '\n'
    
    # PRINT out the result, so that the function has NoneType return
    print(output_string)

def repeat_name_cheat(bear, repeat=2):
    """ A function to actually help me complete this assingment, rather than using the `repeat_name` fucntion suggested in the course
    Output the name of the bear repeated for a certain amount of time, and a word "Bear" in the end
    e.g. "Yogi, Yogi Bear"
    
    Args:
        bear (str): [description]
        repeat (int, optional): [description]. Defaults to 2.
        
    Return:
        int: [description]
    """
    output_string = ""
    
    for i in range(repeat):
        output_string += bear 
        if i != repeat - 1:
            output_string += ', '
    
    output_string += " Bear"
    return output_string

def verse(verse_lyrics, bear_name):
    """Finish the lyrics of the song
    Note that I use the self-defined repeat_name_cheat() rather than using one suggested by the instruction

    Args:
        verse_lyrics (int): the normal verse of the song
        bear_name (int): int of the song

    Returns:
        int: the complete verse of the song
    """
    if bear_name == "Cindy":
        # for the verse "Cindy", there is no empty line in the end
        output_string = [' '] * 8 # A list of 8 empty spaces [" ", " ", " ", ...]
    else:
        output_string = [' '] * 9 # A list of 9 empty spaces
    
    for i in (0, 2, 6):
        output_string[i] = verse_lyrics # At i-th index of the list, replace it with verse_lyrics
        
    for y in (1, 3, 4, 5 ,7):
        output_string[i] = repeat_name_cheat(bear_name) # At y-th index of the list, replace it with the call of function repeat_name_check that receives bear_name as argument
        if y == 1:
            output_string[i] = output_string[i].replace(" Bear", "")  # At the second line, there is no "Bear"

    print( "\n".join(output_string)) # Joing everything together with a new line

def main():
    
    verse("I know someone you don't know", "Yogi")
    verse("Yogi has a best friend too", "Boo Boo")
    verse("Yogi has a sweet girlfriend", "Cindy")


if __name__ == "__main__":
    main()
