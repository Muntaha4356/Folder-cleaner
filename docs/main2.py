import os 
import shutil
directory_path= "C:\Users\Lenovo\Desktop\fun project"
for root, dirs, files in os.walk(directory_path):
    
    for file_name in files:
        file_path = os.path.join(root, file_name)
        print(file_path)
#to find file name
        file_name = os.path.basename(file_path)    
        print(file_name)  
        source_file= file_name
        destination_folder =  "C:\Users\Lenovo\Desktop\fun project\docs"
        shutil.move(source_file, destination_folder)
        print("file cut successfully")
        




        