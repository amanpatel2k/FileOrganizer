# Importing Other Functionalities 
from files.file_searching import file_folder_search

class File: 
    def __init__(self): 
        self.selection = { '1': self.search, '2': self.renaming, '3': None,'4': None, '5': None, '6': None }
    
    def search(self): 
        file_folder_search()
    
    def renaming(self):
        pass
        

if __name__ == '__main__':
    SELECTION = '''
Select an Operation to Perform
1. File Searching
2. File Organizing
3. File Filtering
4. File Sorting
5. File Delection 
6. File Compression/Decompression 
7. Quit
Enter user input: '''
    
    user_input = input(SELECTION)
    
    while user_input != '7':
        file = File()
        if user_input in file.selection: 
            method = file.selection[user_input]
            method()
        else: 
            print('Invalid Input Please Select Another Input')
        user_input = input(SELECTION)
    else: 
        print('Thank You for Using the Application')

    