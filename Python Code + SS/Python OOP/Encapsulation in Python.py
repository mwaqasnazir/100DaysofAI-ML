#!/usr/bin/env python
# coding: utf-8

# ## Encapsulation in Python

# In[12]:


class Parent():
    def __init__(self):
        self.public = "I am a Public Data Member"
        
        # Declearing a protected data member
        self._protected = "I am a Protected Data Member"
        
        # Declearing a private data member
        self.__private = "I am a private Data Member"
        
obj1 = Parent()
        


# In[16]:


#Accessing Public Member of class
print(obj1.public)


# In[17]:


#Accessing Protected Member of class
print(obj1._protected)


# In[15]:


#Accessing Private Member of class
print(obj1._Parent__private)


# In[ ]:




