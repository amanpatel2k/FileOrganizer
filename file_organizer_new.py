# Importing Other Functionalities 
import os
import sys

if __name__ == '__main__':
    SELECTION= '''Welcome to File Organizer!!!\nEnter a valid path to organize your files: '''
    
    user_input = input(SELECTION)
    
    if not os.path.isdir(user_input): 
        print('Invalid Path')
        sys.exit()
        
    
    
    

    