#!/usr/bin/env python
# coding: utf-8

# ## Counstructor In Python

# In[7]:


class Mobile:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price
        
    def result(self):
        print (self.brand)
        print (self.model)
        print (self.price)
        
user1 = Mobile("Samsung", "S8+", 50000)

user1.result()
        


# In[ ]:





# In[ ]:




