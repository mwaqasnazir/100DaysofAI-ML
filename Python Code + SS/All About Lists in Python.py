#!/usr/bin/env python
# coding: utf-8

# ## Lists in Python

# In[4]:


# Creating a List of numbers
List = [10, 20, 14]
print("\nList of numbers: ")
print(List)
  
# Creating a List of strings and accessing
# using index
List = ["Proud", "To Be A ", "Muslim"]
print("\nList Items: ")
print(List[0]) 
print(List[2])
  
# Creating a Multi-Dimensional List
# (By Nesting a list inside a List)
List = [['Proud'], ['To Be A'] , ['Muslim']]
print("\nMulti-Dimensional List: ")
print(List)


# ## List With Mix Values 

# In[9]:


# mixed type of values
List = [1, 2, 'Proud', 4, 'To Be A', 6, 'Muslim']
print("\nList with the use of Mixed Values: ")
print(List)


# ## Size of List  & Accessing Elements From List

# In[8]:


# Finding Length of a List # accessing a element from the 
List = [10, 20, 14]
print(len(List2))
print("Accessing a element from the list")
print(List[0]) 
print(List[2])
  
# accessing an element from the 
# Multi-Dimensional List using
List = [['Geeks', 'For'] , ['Geeks']]

print("Accessing a element from a Multi-Dimensional list")
print(List[0][1])
print(List[1][0])


# ## Adding Elements From a List

# In[33]:


List = []
print("Initial blank List: ")
print(List)

# Addition of Elements in the List Using Append
List.append('W')
print("\nList after Addition of Two elements: ")
print(List)

# Addition of Elements in the List Using Extend
List.extend([2, 'Always', 'Smile'])
print("\nList after performing Extend Operation: ")
print(List)

# Adding elements to the List using Iterator
for i in range(1, 5):
    List.append(i)
print("\nList after Addition of elements from 1-5: ")
print(List)

# Addition of Element at specific Position using Insert Method
List.insert(3, 12)
List.insert(0, 'Wicky')
print("\nList after performing Insert Operation: ")
print(List)

# Adding Tuples to the List
List.append((5, 6))
print("\nList after Addition of a Tuple: ")
print(List)

# Addition of List to a List
List2 = ["It's me" , 'Wicky']
List.append(List2)
print("\nList after Addition of a List: ")
print(List)


# ##  Removing Elements From a List

# In[46]:



List = [1,2,3,4,5,6,7]
List.pop(3)
print("\nList after Removal of one elements Using Pop: ")
print(List)


List.remove(6)
print("\nList after Removal of one elements Using Remove: ")
print(List)


# In[ ]:




