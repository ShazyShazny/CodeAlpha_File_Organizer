import os
import shutil

def file_organizer(source_dir, destination_dir):    
    
    folders = {
        'Documents': ['.doc', '.docx', '.pdf', '.txt', '.xlsx', '.xls', '.ppt', '.pptx'],
        'Images': ['.png', '.jpg', '.jpeg', '.gif', '.bmp'],
        'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv'],
        'Audio': ['.mp3', '.m4a', '.flac', '.wav', '.wma', '.aac']
    }
    
    for folder in folders:  
        folder_path = os.path.join(destination_dir, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    
    files = os.listdir(source_dir)  
    
    for file in files:
        if os.path.isdir(os.path.join(source_dir, file)):   
            continue
        
        _, extension = os.path.splitext(file)  
        
        destination_folder = None   
        for folder, ext_list in folders.items():
            if extension.lower() in ext_list:
                destination_folder = folder
                break
         
        if destination_folder: 
            src_file = os.path.join(source_dir, file)
            dest_file = os.path.join(destination_dir, destination_folder, file)
            shutil.move(src_file, dest_file)

if __name__ == "__main__":

    foldr_path = r"D:\Eclipse\File Organizer\destination_directory"
    destination_directory = r"D:\Eclipse\File Organizer\destination_directory"

    file_organizer(foldr_path, destination_directory)
