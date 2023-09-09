# TODO: File Searching 
from dotenv import load_dotenv
import os

class File_Search: 
    def __init__(self):
        self.searchMap = { 'file': self.file, 'folder': self.folder} 
        load_dotenv()
        self.path = os.environ.get('FILE_PATH')
    
    def file(self):
        
        user_input = input("Search by name, extension, or both: ")

        # Search by Extension
        if user_input.lower() == 'extension': 
            ext = input("Enter the extension: ")
            if ext[0] != '.': return "Invalid Syntax"
            for root, dirs, files in os.walk(self.path):
                for file in files:
                    if file.endswith(f'{ext.lower()}'):
                        print(file)
        
        elif user_input.lower() == 'name':
             # Search by File Name
            file_name = input("Enter the file you are finding: ")
            filenames = []
            for (root, dirs, files) in os.walk(self.path): 
                for file in files:
                    if file_name.lower() == os.path.splitext(file)[0].lower() or file_name.lower() in file.lower():
                        filenames.append(os.path.join(root, file))
            if filenames: return filenames 
            else: return f'File Not Found by This Name: {file_name}'
        
        else:   
            # Search by Both
            file_name = input("Enter the file you are finding: ")
            ext = input("Enter the extension of the file: ")
            full_file = file_name+ext
            for (root, dirs, files) in os.walk(self.path): 
                if full_file in files:
                    return os.path.join(root, full_file)
            else: return f'File Not Found by This Name: {file_name}'
        
    def folder(self): 
        user_folder = input("What is the folder name: ")
        directory = []
        for root, dirs, files in os.walk(self.path): 
            for dir in dirs: 
                if dir.lower() == user_folder.lower(): 
                    directory.append(os.path.join(root, dir))    
        if directory: return directory
        else: return f'Folder, {user_folder}, Not Found'
        
def file_folder_search(): 
    
    user = input("Would like to search for a file or for a folder: ")
    
    while user.lower() == 'file' or user.lower() == 'folder': 
        file_search = File_Search()
        operation = file_search.searchMap[user.lower()]()
        if operation: print(operation, end='\n')
        
        seconds = input("Would like to make another search for a file or for a folder (Type Yes or No): ")
        if seconds.lower() == 'no': 
            return
        user = input("Would like to search for a file or for a folder: ")
    else: print('Invalid Input Please Try Again\n')  

if __name__ == '__main__':
    file_folder_search()