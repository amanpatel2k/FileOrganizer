# Dictionary of Files Based on Extensions
import os, shutil
from collections import defaultdict

def organize_ext(path, allFiles, directories):
    master = defaultdict(list)
    
    for file in allFiles:
        
        # Split the file to get the extension
        file_split = os.path.splitext(file)
        extension = file_split[1].lower()
        
        for key, values in directories.items():
            if extension in values:
                master[key].append(f'{path}/{file}')
                break
        else:
            master["OTHER"].append(f'{path}/{file}')
            
    return master

def check_create_folders(path, folders, directories):
    for folder in folders: 
        if len(directories[folder]):
            # Check if foldere exist
            if not os.path.exists(f'{path}/{folder.title()}'): 
                os.makedirs(f'{path}/{folder.title()}')

    
def main_process(path):
    directories = {
        "PICTURES": (".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg",
                   "svg", ".heif", ".psd", '.heic'),
        "VIDEOS": (".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob",
                   ".mng",".qt", ".mpg", ".mpeg", ".3gp", ".mkv"),
        "DOCUMENTS": (".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf",
                      ".ods", ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox", ".json", ""
                      ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", ".pptx", ".pdf", ".txt", ".pages"),
        "ARCHIVES": (".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                     ".dmg", ".rar", ".xar", ".zip"),
        "AUDIO": (".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p",
                  ".mp3", ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"),
        "PROGRAMS": (".exe", ".py"),
        "OTHER": ""
    }

    # List of files to organize
    list_of_files = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file)) and not file.startswith(".")]

    # Organize files by extension 
    master_list = organize_ext(path, list_of_files, directories)
    
    # Check or create new folders
    check_create_folders(path, directories.keys(), master_list)
    
    # Organize the folders
    for folder in master_list: 
        for files in master_list[folder]:
            shutil.move(os.path.join(path, files), f'{path}/{folder.title()}')

    
    return True 
    

    