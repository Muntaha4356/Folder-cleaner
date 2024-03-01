import os
import shutil
def move_to_folder(file):
     # Source and destination directories
    files= os.listdir()
    files.remove("main.py")
    
    imgExts = [".png", ".jpg", ".jpeg"]
    docExts=[".txt", ".docx", "doc", ".pdf"]
    mediaExts= [".mp4", ".mp3", ".flv"]

    docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]
     
    for file in files:
      if os.path.splitext(file)[1].lower() in docExts:
         destination_dir = r"C:\Users\Lenovo\Desktop\fun project\docs"
      elif os.path.splitext(file)[1].lower() in imgExts:
         destination_dir = r"C:\Users\Lenovo\Desktop\fun project\images"   
      elif  os.path.splitext(file)[1].lower() in mediaExts:
         destination_dir =  r"C:\Users\Lenovo\Desktop\fun project\Media "
    source_dir = r"C:\Users\Lenovo\Desktop\fun project" 
       


# File to be moved
    
    file_to_move = file

# Construct full paths for source and destination
    source_file_path = os.path.join(source_dir, file_to_move)
    destination_file_path = os.path.join(destination_dir, file_to_move)

# Check if the source file exists
    if os.path.exists(source_file_path):
    # Move the file
        shutil.move(source_file_path, destination_file_path)
        print(f"File '{file_to_move}' moved successfully from '{source_dir}' to '{destination_dir}'")
    else:
        print(f"File '{file_to_move}' does not exist in '{source_dir}'")



directory_path =    r"C:\Users\Lenovo\Desktop\fun project"    
for filename in os.listdir(directory_path) :
   if os.path.isfile(os.path.join(directory_path, filename)):
      move_to_folder(filename)
