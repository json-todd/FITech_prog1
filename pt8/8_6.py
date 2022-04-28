"""
Numbering in reading files from a file


Author: Tri Phung
StudentID: tuni.fi:K441912
COMP.CS.100 Programming 1

"""

def main():
    file = input('Enter the name of the file: ')
    try:
        file_handle = open(file, 'r')
    except OSError:
        print('There was an error in reading the file.')
        return
    
    line_number = 1
    for line in file_handle:
        line = line.rstrip()
        print(f'{line_number} {line}')
        line_number += 1
        
    file_handle.close()

if __name__ == "__main__":
    main()