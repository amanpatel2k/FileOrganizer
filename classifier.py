# Dictionary of Files Based on Extensions
import os
from collections import defaultdict

def organize_ext(allFiles):
    master = defaultdict(list)
    
    for file in allFiles:
        
        # Split the file to get the extension
        file_split = os.path.splitext(file)
        extension = file_split[1].lower()
        
        for key, values in directories.items():
            if extension in values:
                master[key].append(f'{path}/{file}')
            
    return master
        
    
if __name__ == '__main__':
    path = '/Users/amanpatel/Downloads'
    
    directories = {
        "PICTURES": (".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg",
                   "svg", ".heif", ".psd", '.heic'),
        "VIDEOS": (".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob",
                   ".mng",".qt", ".mpg", ".mpeg", ".3gp", ".mkv"),
        "DOCUMENTS": (".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf",
                      ".ods", ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox", ".json", ""
                      ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", "pptx", ".pdf", ".txt", ".pages"),
        "ARCHIVES": (".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                     ".dmg", ".rar", ".xar", ".zip"),
        "AUDIO": (".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p",
                  ".mp3", ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"),
        "PROGRAMS": ".exe",
        "OTHER": ""
    }

    # List of files to organize
    list_of_files = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
    
    # Organize files by extension 
    full_path_files = [f'{path}/{file}' for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
    master_list = organize_ext(list_of_files)
    
    
    

    

    