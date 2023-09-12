from dotenv import load_dotenv
import os
from .my_display import mydisplay

class File_Search: 
    def __init__(self):
        self.searchMap = { 'file': self.file, 'folder': self.folder} 
        load_dotenv()
        self.path = os.environ.get('FILE_PATH')
    
    def file(self):
        
        user_input = input("Search by name, extension, or both: ")

        if user_input.lower() == 'extension': 
            # Search by Extension
            ext = input("Enter the extension: ")
            if ext[0] != '.': return "Invalid Syntax"
            extension = []
            for root, dirs, files in os.walk(self.path):
                for file in files:
                    if file.endswith(f'{ext.lower()}'):
                        extension.append(file)
            if extension: return extension
            else: return f'File Not Found by This Extension: {ext}'
        
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
            file_name = input("Enter the file name you are finding: ")
            ext = input("Enter the extension of the file: ")
            fullFiles = []
            full_file = file_name+ext
            for (root, dirs, files) in os.walk(self.path): 
                for file in files:
                    if full_file.lower() == file.lower():
                        fullFiles.append(os.path.join(root, file))
                    
            if fullFiles: return fullFiles
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
        if operation: print("Your File Has Been Searched: \n")
        
        # print(operation)
        mydisplay(operation)
    
        seconds = input("Would like to make another search for a file or for a folder (Type Yes or No): ")
        if seconds.lower() == 'no': 
            return 
        user = input("Would like to search for a file or for a folder: ")
    else: 
        print('Invalid Input Please Try Again\n')  
        return