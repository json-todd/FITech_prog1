"""
Calculting scores

Author: Tri Phung
StudentID: tuni.fi:K441912
COMP.CS.100 Programming 1
"""

def main():
    file = input('Enter the name of the score file: ')

    try: file_handle = open(file,'r')
    except OSError: print('There was an error in reading the file.'); return

    player_score_DB = {}
    
    for line in file_handle:
        line = line.rstrip()
        player_score = line.split(' ')
        
        try: player = player_score[0]; score = player_score[1]
        except: print('There was an erroneous line in the file:'); print(line); return
        
        try: score = int(score)
        except: print('There was an erroneous score in the file:'); print(score); return
        
        player_score_DB[ player ] = player_score_DB.get( player, 0 ) + score
    
    print('Contestant score:')
    for player in sorted(player_score_DB):
        score = player_score_DB[player]
        print(f'{player} {score}')


if __name__ == "__main__":
    main()