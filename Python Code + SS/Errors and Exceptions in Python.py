#!/usr/bin/env python
# coding: utf-8

# ## Errors and Exceptions in Python

# In[26]:


# Python code to illustrate working of try()
def divide(x, y):
    try:
        # Floor Division : Gives only Fractional Part as Answer
        result = x // y
        print("\nYeah ! Your answer is :", result)
    except ZeroDivisionError:
        print("\nSorry ! You are dividing by zero ")
        
divide(3, 0)

def multiply(x, y):
    try:
        result = x * y
        print("\nYeah ! Your answer is :", result)
    except ZeroDivisionError:
        print("\nSorry ! You are multiplying by zero ")

multiply(5, 2)

def normal_division(x, y):
    try:
        result = x / y
        print("\nYeah ! Your answer is :", result)
    except ZeroDivisionError:
        print("\nSorry ! You are dividing by zero ")
    finally:
    # this block is always executed regardless of exception generation.
        print('This is always executed')

normal_division(5, 0)


# In[ ]:




