#Arrange files 
import os
files = os.listdir() # to print all the files in this directory
files.remove("main.py")
print(files)
def create_if_not_exist(folder):
   
   if not os.path.exists(folder): #tells if a folder doesn't exist in a specified directory
      os.makedirs(folder)
def move(folderName, files)      :
   for file in files:
      os.replace(file, f"{folderName},{file}")
create_if_not_exist('docs')
create_if_not_exist("docs")
create_if_not_exist('others')
create_if_not_exist('images')
# Time to decide hat to add in these folders
# files = os.listdir() # to print all the files in this directory
# files.remove("main.py")
# print(files) #Can be removed
imgExts = [".png", ".jpg", ".jpeg"]
images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]
# print(images)
docExts=[".txt", ".docx", "doc", ".pdf"]


docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]
# print(docs)

mediaExts= [".mp4", ".mp3", ".flv"]
medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]
others = []

for file in files:
   ext = os.path.splitext(file)[1].lower()
   if os.path.isfile(file):
     if (ext not in mediaExts) or (ext not in docExts) or (ext not in imgExts):
        others.append(file)
move("Media", medias)
move("images", images)
move("docs", docs)  
move("other", others)







