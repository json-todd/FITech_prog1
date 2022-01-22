"""
COMP.CS.100 1.6.8 Smileys
Creator: Tri Phung
Student ID: tuni.fi:K441912
"""

def main():
    def smiley():
        """
        Return emoticon smiley face according to your mood
        """
        
        smiley = ""
        string = input("How do you feel? (1-10) ")
        try: 
            feel = int(string)
        except:
            return "Bad input!"
        
        if feel > 10 or feel < 1:
            return "Bad input!"
        elif feel == 10:
            smiley = ":-D"
        elif feel > 7:
            smiley = ":-)"
        elif feel >= 4:
            smiley = ":-|"
        elif feel > 1:
            smiley = ":-("
        else:
            smiley = ":'("

        return f"A suitable smiley would be {smiley}"
    
    print( smiley() )
    

if __name__ == "__main__":
    main()