#!/usr/bin/env python
# coding: utf-8

# ## Strings in Python

# In[41]:


# Initial String
String1 = '''I'm a "Student"'''
print("Initial String with use of Triple Quotes: ")
print(String1.upper())
 
# Escaping Single Quote
String1 = 'I\'m a "Student"'
print("\nEscaping Single Quote: ")
print(String1)
 
# Escaping Double Quotes
String1 = "I'm a \"Student\""
print("\nEscaping Double Quotes: ")
print(String1)
 
# Printing Paths with the use of Escape Sequences
String1 = "C:\\Python\\Code\\"
print("\nEscaping Backslashes: ")
print(String1)


# ## Strings Using Hex & Raw

# In[4]:



# Printing Geeks in HEX
String1 = "This is \x77\x69\x63\x6b\x79 in \x48\x45\x58"
print("\nPrinting in HEX with the use of Escape Sequences: ")
print(String1)
 
# Using raw String to
# ignore Escape Sequences
String1 = r"This is \x77\x69\x63\x6b\x79 in \x48\x45\x58"
print("\nPrinting Raw String in HEX Format: ")
print(String1)


# ## String Allignments

# In[18]:


# String alignment <left, ^Center, >Right
String1 = "|{:<10}|{:^10}|{:>10}|".format('This','is','Wicky')
print("\nLeft, center and right alignment with Formatting: ")
print(String1)


# ## Strings Formating

# In[5]:


# Python Program for Formatting of Strings
# Default order
String1 = "{} {} {}".format('This', 'Is', 'Wicky')
print("Print String in default order: ")
print(String1)
 
# Positional Formatting
String1 = "{1} {0} {2}".format('This', 'Is', 'Wicky')
print("\nPrint String in Positional order: ")
print(String1)
 
# Keyword Formatting
String1 = "{l} {f} {g}".format(g = 'This', f = 'Is', l = 'Wicky')
print("\nPrint String in order of Keywords: ")
print(String1)


# ## Strings Using Binary, Floats, Exponent, Round off

# In[42]:


# Formatting of Integers
String1 = "{0:b}".format(12)
print("\nBinary representation of 12 is ")
print(String1)

# Formatting of Floats
String1 = "{0:e}".format(185.8509)
print("\nExponent representation of 185.8509 is ")
print(String1)

# Rounding off Integers
String1 = "{0:.2f}".format(1/5)
print("\none-fifth is : ")
print(String1)


# ## Strings Slicing

# In[44]:


# Python Program to demonstrate String slicing
String1 = "this is Wicky"
print("Initial String: ")
print(String1.capitalize())
 
# Printing 8th to 14th character
print("\nSlicing characters from 8-14: ")
print(String1[8:14])
 
# Printing characters 
print("\nSlicing" + "character: ")
print(String1[0:-5])


# In[ ]:




