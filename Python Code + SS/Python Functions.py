#!/usr/bin/env python
# coding: utf-8

# # Python Functions

# In[2]:


# Function Syntax:
# def function_name(parameters):
#     """docstring"""
#     statement(s)
#     return expression
 

# A simple Python function to check
# whether x is even or odd

def evenodd(x):
    """Function to check if the number is even or odd"""
     
    if (x % 2 == 0):
        return("even")
    else:
        return("odd")

# Driver code to call the function
print(evenodd.__doc__)


num = int(input("Enter a number: "))
evenodd(num)


# In[ ]:




