import shutil
import os
def createifnotexists(folder):
     if not os.path.exists(folder):
          os.makedirs(folder)


createifnotexists("Images")  
createifnotexists("Docs")        

def file_to_move(file):
# # Source and destination directories
   #findinf extension of the file
   
   
   source_dir = r"C:\Users\Lenovo\Desktop\fun project" #Name of the folder


   

# File to be moved
   file_to_move = file

   
   file_path = os.path.basename(__file__)
   extension = os.path.splitext(file_path)[1]
   if extension == ".txt" or ".pdf" or ".rtf":
       destination_dir = r"C:\Users\Lenovo\Desktop\fun project\docs"
   if extension == ".png" or ".jpg" or ".raw":
       destination_dir= r"C:\Users\Lenovo\Desktop\fun project\Images"

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





#OUt of Def Function
#To find directory path
            
directory_path =  os.path.dirname(os.path.abspath(__file__)) 
print(directory_path)   


for filename in os.listdir(directory_path):
   file_path = os.path.join(directory_path, filename)
   if os.path.isfile(file_path):
      print(f"filename is {filename}")
      print(f"filepath is {file_path}")     

            

# for root, dirs, files in os.walk(os.getcwd()):
    
#         file_path = os.path.join(root) #It's for the file path to

# file_name = os.path.basename(file_path)
file_to_move(filename)
                                             
