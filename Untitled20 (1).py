#!/usr/bin/env python
# coding: utf-8

# In[2]:


x=1 ; y=1 ; h=1 ; r=y; ş=5
print("   x             y               z" )
while True:
    y=r
    while True:
        z=x+y
        print(" x={}        y={}           z={}      ".format(x,y,z))
        
        if z<ş:
            y=y+h 
        else:
            x=x+h            
            break
        
    if x>ş-r-1:
        break


# In[ ]:




