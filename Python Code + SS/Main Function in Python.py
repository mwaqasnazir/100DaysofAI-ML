#!/usr/bin/env python
# coding: utf-8

# ## Use of  if __name__ == "__main__" In Python

# In[27]:


import Module

def main():
    add(5,6)
    subtract(6,3)
    divide(8,2)
    multiply(2,2)

if __name__ == "__main__":
    main()


# In[26]:


# Simple Modules 

def add(x, y):
    print (x+y)
    
def subtract(x, y):
    print (x-y)

def divide(x, y):
    print (x/y)

def multiply(x, y):
    print (x*y)
    
def main():
    subtract(6,3)
    divide(8,2)
    
if __name__ == "__main__":
    main()


# In[ ]:




