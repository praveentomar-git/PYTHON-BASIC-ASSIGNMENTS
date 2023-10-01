#!/usr/bin/env python
# coding: utf-8

# ## Q1. How do you distinguish between shutil.copy() and shutil.copytree()?

# ### ANS1. The shutil.copy() function will copy a single file. 
# ### shutil.copytree() will copy an entire folder, along with all its contents.

# ## Q2. What function is used to rename files?

# ### ANS2. The shutil.move() function is used for renaming files as well as moving them.

# ## Q3. What is the difference between the delete functions in the send2trash and shutil modules?

# ### ANS3. The send2trash functions will move a file or folder to the recycle bin, while shutil functions will permanently delete files and folders.

# import shutil
# 
# shutil.rmtree("PATH") # DELETES PERMANENTLY
# 
# import send2trash
# 
# send2trash.send2trash("PATH") # SEND TO RECYCLEBIN AND CAN BE RECOVERED

# ## Q4.ZipFile objects have a close() method just like File objects’ close() method. What ZipFile method is equivalent to File objects’ open() method?

# ### ANS4. The zipfile.ZipFile() function is equivalent to the open() function; the first argument is the filename, and the second argument is the mode to open the ZIP file in (read, write, or append).

# from zipfile import Zipfile
# 
# with ZipFile(file_name, 'r') as zip

# ## Q5. Create a programme that searches a folder tree for files with a certain file extension (such as .pdf or .jpg). Copy these files from whatever location they are in to a new folder.

# In[5]:


import os
import shutil

def selectiveCopy(source, extensions, destFolder):
    folder = os.path.abspath(source)
    destFolder = os.path.abspath(destFolder)
    print('Looking in', source, 'for files with extensions of', ', '.join(extensions))
    for foldername, subfolders, filenames in os.walk(source):
        for filename in filenames:
            name, extension = os.path.splitext(filename)
            if extension in extensions:
                fileAbsPath = foldername + os.path.sep + filename
                print('Coping', fileAbsPath, 'to', destFolder)
                shutil.copy(fileAbsPath, destFolder)

extensions = ['.pdf','.jpg']
source = r'D:\BUSINESS WHIZ'
destFolder =r'D:\New folder'
selectiveCopy(source, extensions, destFolder)

