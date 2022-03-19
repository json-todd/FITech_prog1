"""
COMP.CS.100 Programming 1
Contacts

Author: Tri Phung
"""
def read_file(file_name):
    """Read a designated csv file to turn into an esay-to-look-up datastructure

    Args:
        file_name: str, csv file containing people and contact info

    Returns:
        data: dict, datastructure for people and contact infor
    """
    
    try:
        file_handle = open(file_name, 'r')
        
        data = {}

        payload_key = []
        
        for l in file_handle:
            l = l.rstrip()
            
            if "key;name" in l:
                payload_key = l.split(';')[1:]
                continue
            
            parts = l.split(';')
            
            name = parts[0]; facts = parts[1:]
            
            payload = {}
            
            for indx in range(len(payload_key)):
                payload[ payload_key[indx] ] = facts[indx]
                
            data[name] = payload
            
        file_handle.close()   
        
    except:
        print('File handling error')
        data = None
        
    return data
 
