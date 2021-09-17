#!/usr/bin/env python
# coding: utf-8

# ## Inheritance in Python

# In[25]:


#Creating a parent class

class Vehicle:
    def __init__(self, price, milage):
        self.price = price
        self.milage = milage
        
    def show_details(self):
        print("I am a Vehicle")
        print("Price of vehicle is :",self.price)
        print("Milage of vehicle is :",self.milage)


# In[26]:


v1 = Vehicle(5000000,15)


# In[27]:


v1.show_details()


# In[28]:


#Creating a child class which is inherited from parent class

class Car(Vehicle):
    def show_car_details(self):
        print("I am car inherted from Vehicle Class")


# In[29]:


c1 = Car(100000,20)
c1.show_details()
c1.show_car_details()


# In[ ]:




