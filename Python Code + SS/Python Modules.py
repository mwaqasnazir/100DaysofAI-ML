#!/usr/bin/env python
# coding: utf-8

# ## Python Modules

# In[1]:


import Module

Module.add(8,2) 
Module.subtract(8,2)
Module.multiply(8,2)
Module.divide(8,2)


# In[5]:


from Module import multiply

multiply(2,5)


# In[7]:


from Module import*

multiply(2,5)
subtract(8,2)
multiply(8,2)
divide(8,2)

