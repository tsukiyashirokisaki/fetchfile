import os;  
import sys;  
path=os.getcwd()
flag=True
for name in os.listdir(path):  
    newName = name.replace("2F","")
    print(newName)
    if flag:  
        os.chdir(path)  
        flag=False  
    os.rename(name,newName)  




# In[46]:




