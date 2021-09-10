#!/usr/bin/env python
# coding: utf-8

# # File Handling in Python

# ## Reading a File

# In[27]:


file = open('myfile.txt', 'r')
# This will print complete file
print(file.read())


# In[28]:


file = open('myfile.txt', 'r')

# This will print every line one by one in the file
for each in file:
    print (each)


# In[29]:


# Python code to illustrate with()  using this method any files opened
# will be closed automatically after one is done, so auto-cleanup.
with open("myfile.txt") as file:  
    data = file.read()
print(data)


# ## Creating a File

# In[30]:


# Python code to create a file
file = open('myfile2.txt','w')
file.write("This is the write command")
file.write("\nIt allows us to write in a particular file")
file.close()


# In[31]:


# Here i am reading the above file which is writen by using write function
file = open('myfile2.txt','r')
print(file.read())


# In[34]:


# Python code to illustrate with() alongwith write()
with open("myfile3.txt", "w") as f: 
    f.write("Hello World!!!")
    
with open("myfile3.txt","r") as file:
    result= file.read()
    print(result)


# In[39]:


# Python code to illustrate Write, Read & Splits the text using split() function
with open("myfile.text", "w+") as file:
    file.write("This is the write command")
    file.write("\nIt allows us to write in a particular file")
with open("myfile.text", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print (word)


# In[ ]:




