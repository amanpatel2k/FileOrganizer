# Importing Other Functionalities 
import os, sys
from classifier import main_process

if __name__ == '__main__':
    SELECTION= '''Enter a valid path to organize your files: '''
    
    user_input = input(SELECTION)
    
    if not os.path.isdir(user_input): 
        print('Invalid Path')
        sys.exit()
    
    
    print('Begin Scanning!')
    if main_process(user_input): 
        print("Done")
    

    