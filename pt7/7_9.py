"""
Using dictionary to count occurance of letter from a user input


Author: Tri Phung
Student ID: K441912
Email: tri.phung@tuni.fi
"""

def main():
    word_count = {}
    
    print("Enter rows of text for word counting. Empty row to quit.")
    while True:
        user_input = input("")
        if user_input == "": break
        
        for word in user_input.split(' '):
            word = word.lower()
            word_count[word] = word_count.get(word,0) + 1


    for word in sorted(word_count):
        print(f"{word} : {word_count[word]} times")

if __name__ == "__main__":
    main()
