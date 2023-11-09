# Importing Other Functionalities 
import os
import sys

if __name__ == '__main__':
    SELECTION= '''Enter a valid path to organize your files: '''
    
    user_input = input(SELECTION)
    
    if not os.path.isdir(user_input): 
        print('Invalid Path')
        sys.exit()
    
    
    # List of files to organize
    list_of_files = os.listdir(user_input)
    
    # Perform the automation
    

    