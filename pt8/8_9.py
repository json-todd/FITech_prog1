"""
Writing file


Author: Tri Phung
StudentID: tuni.fi:K441912
COMP.CS.100 Programming 1

"""

def main():
    file = input('Enter the name of the file: ')
    try:
        file_handle = open(file, 'w')
    except OSError:
        print(f'Writing the file {file} was not successful.')
        return
    
    print('Enter rows of text. Quit by entering an empty row.')
    line_number = 1
    while True:
        line = input()
        if line == '': break
        
        print(f'{line_number} {line}', file=file_handle)
        line_number += 1
    
    print(f'File {file} has been written.')
    file_handle.close()
    
    
if __name__ == "__main__":
    main()