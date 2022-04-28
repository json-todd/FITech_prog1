"""
COMP.CS.100 Programming 1
Tourist dictionary with cool features.

Author: Tri Phung
Student ID: K441912
Email: tri.phung@tuni.fi
"""

def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}

    print("Dictionary contents:")
    print(", ".join( sorted( english_spanish.keys() ) ) )
    while True:
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":

            word = input("Enter the word to be translated: ")
            if word in english_spanish: 
                print(f"{word} in Spanish is {english_spanish[word]}")
            else: 
                print("The word", word, "could not be found from the dictionary.")

        elif command == "A":
            word_eng = input("Give the word to be added in English: ")
            word_esp = input("Give the word to be added in Spanish: ")
            english_spanish[word_eng] = word_esp
            print("Dictionary contents:")
            print(", ".join( sorted( english_spanish.keys() ) ) )

        elif command == "R":
            word_rmv= input("Give the word to be removed: ")
            if word_rmv in english_spanish:
                english_spanish.pop(word_rmv)
            else:
                print("The word", word, "could not be found from the dictionary.")
            
        elif command == "P":
            print("\nEnglish-Spanish")
            for eng in sorted( english_spanish ):
                print(f"{eng} {english_spanish[eng]}")
                
            print("\nSpanish-English")
            for eng_span in sorted( english_spanish.items(), key = lambda kv: kv[1] ):
                print(f"{eng_span[1]} {eng_span[0]}")
            print()

        elif command == "T":
            sent = input("Enter the text to be translated into Spanish: ")
            sent_list = sent.split(' ')
            sent_trans = []
            for word in sent_list:
                if word not in english_spanish:
                    sent_trans.append(word)
                    continue
                sent_trans.append( english_spanish[word] )
                
            print("The text, translated by the dictionary:")
            print(" ".join(sent_trans))
                
        elif command == "Q":
            print("Adios!")
            return

        else:
                print("Unknown command, enter W, A, R, P, T or Q!")

if __name__ == "__main__":
    main()
