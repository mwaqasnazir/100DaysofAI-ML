#!/usr/bin/env python
# coding: utf-8

# ## Destructors in Python

# In[3]:


# Python program to illustrate destructor
class Employee:

    def __init__(self):
        print('Employee created.')

    # Deleting (Calling destructor)
    def __del__(self):
        print('Destructor called, Employee deleted.')

obj = Employee()
del obj


# In[ ]:




