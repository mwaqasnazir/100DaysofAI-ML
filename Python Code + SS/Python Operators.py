#!/usr/bin/env python
# coding: utf-8

# # Python Operators

# ## 1. Arithmetic Operators

# In[20]:


a=6
b=4
#addition & subtraction
add = a+b
sub=a-b

# Multiplication 
mul = add*sub

# Division(float)
div1 = a / b
 
# Division(floor)
div2 = a // b
 
# Modulo
mod = a % b
 
# Power
p = a ** b
 
# printing results
print(add)
print(sub)
print(mul)
print(div1)
print(div2)
print(mod)
print(p)


# ## 2. Comparison Operators

# In[21]:


# Comparision Oprators gives the out put in true/false here 
print(a > b)
 
print(a < b)
 
print(a == b)
 
print(a != b)
 
print(a >= b)
 
print(a <= b)


# ## 3.  Logical Operators

# In[29]:


a = True
b = False
c = True
 
# and
print(a and b , a and c)
 
# or
print(a or b)

# not
print(not a)


# ## 4. Bitwise Operators

# In[23]:


a = 15
b = 5
 
# Bitwise AND operation
print(a & b)
 
# Bitwise OR operation
print(a | b)
 
# Bitwise NOT operation
print(~b)
 
# Bitwise XOR operation
print(b ^ a)
 
# Bitwise right shift operation
print(a >> 1)
 
# Bitwise left shift operation
print(b << 1)


# ## 5. Assignment Operators

# In[24]:


a = 15
# Assign value
b = a
print(b)
 
# Add and assign value to left operand
b += a
print(b)
 
# Subtract and assign value to left operand
b -= a
print(b)
 
# multiply and assign to left operand
b *= a
print(b)
 
# bitwise lishift operator ((addition of  b+b) to a times)
b <<= a
print(b)


# ## 6. Identity Operators

# In[27]:


a = "Green"
b = "Blue"
c = b
 
print(a is not b)
print(a is c)


# In[ ]:




