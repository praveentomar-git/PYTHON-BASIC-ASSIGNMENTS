#!/usr/bin/env python
# coding: utf-8

# ## Q1. To what does a relative path refer?

# ### Ans1: The relative path is the path to some file with respect to our current working directory (PWD).  
# ### For example: if Absolute path to a file called abc.txt is: `C:/users/admin/docs/abc.txt` If my PWD is `C:/users/admin/` , then the relative path to `abc.txt` would be: `docs/stuff.txt`       
# **Note:** PWD + relative path = absolute path

# ## Q2. What does an absolute path start with your operating system?

# ### ANS2. An absolute path contains the full set of directories from the root of the file system up to the target file or directory. 
# ### In Linux based systems the absolute path starts with **`/`**. Where as in Windows based systems absolute path starts with **`C:`**

# ## Q3. What do the functions os.getcwd() and os.chdir() do?

# ### Ans3: `os.getcwd()` method tells us the location of current working directory (CWD). Whereas `os.chdir()` method in Python used to change the current working directory to specified path. These functions are similar to linux commands `pwd` and `cd`.

# In[4]:


import os
print(os.getcwd()) # Prints the current Working Directory
path = r'C:\Users\chpra\FSDS_ASSIGNMENTS'
os.chdir(path)
print(os.getcwd())


# ## Q4. What are the . and .. folders?

# ### ANS4.  `.` Represents the Current Directory Whereas `..` Represents the Parent Directory of the Current Directory. 

# ## Q5. In C:\bacon\eggs\spam.txt, which part is the dir name, and which part is the base name?

# ### ANS5. The dir name is `C:\\bacon\\eggs`  
# ### The base name is `spam.txt`

# In[5]:


import os
path = r'C:\bacon\eggs\spam.txt'
print(os.path.dirname(path))
print(os.path.basename(path))


# ## Q6. What are the three “mode” arguments that can be passed to the open() function?

# **ANS6:** A file can be Accessed in python using `open()` function. open function takes two arguments filename and mode of operation (optional). if mode is not provided the default mode of opening is read mode   
# So, the syntax being: **`open(filename, mode)`**
# * **`‘r’`** – Read Mode: This is the default mode for open(). The file is opened and a pointer is positioned at the beginning of the file’s content.
# * **`‘w’`** – Write Mode: Using this mode will overwrite any existing content in a file. If the given file does not exist, a new one will be created. 
# * **`‘r+’`** – Read/Write Mode: Use this mode if we need to simultaneously read and write to a file.
# * **`‘a’`** – Append Mode: With this mode we can append the data without overwriting any already existing data in the file. 
# * **`‘a+’`** – Append and Read Mode: In this mode we can read and append the data without overwriting the original file.
# * **`‘x’`** – Exclusive Creating Mode: This mode is for the sole purpose of creating new files. Use this mode if we know the file to be written doesn’t exist beforehand.

# ## Q7. What happens if an existing file is opened in write mode?

# ### ANS7.  `‘w’` – Write Mode: Using this mode will overwrite any existing content in a file. If the given file does not exist, a new one will be created. 

# ## Q8. How do you tell the difference between read() and readlines()?

# ### Ans8:
# * The main difference is that **`read()`** will read the whole file at once and then print out the first characters that take up as many bytes as we specify in the parenthesis.
# * The **`read()`** would treat each character in the file separately, meaning that the iteration would happen for every character.
# 
# * Whereas the **`readline()`** that will read and print out only the first characters that take up as many bytes as we specify in the parenthesis. We may want to use readline() when we're reading files that are too big for our RAM.
# * The **`readline()`** function, on the other hand, only reads a single line of the file. This means that if the first line of the file were three lines long, the readline() function would only parse (or iterate/operate) on the first line of the file.

# ## Q9. What data structure does a shelf value resemble?

# ### ANS9. A shelf value resembles a dictionary value; it has keys and values, along with keys() and values() methods that work similarly to the dictionary methods of the same names.
