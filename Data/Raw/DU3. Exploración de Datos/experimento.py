#!/usr/bin/env python
# coding: utf-8

# In[28]:


import numpy as np
import matplotlib.pyplot as plt
data = np.random.RandomState(0).randn(100)
plt.boxplot(data)
plt.title("Boxplot con Matplotlib")
plt.show()


# In[3]:


data =[np.random.RandomState(0).randn(100), 
       2 * np.random.RandomState(1).randn(100) + 1,
       0.5 *np.random.RandomState(2).randn(100) - 1]
plt.boxplot(data)
plt.title("Boxplot con Matplotlib")
plt.show()


# In[4]:


import matplotlib.pyplot as plt 

x=[4,5,6,8,9,10,10,11,11,12,13,14,15,15,15,17,18,19,22,23,25]

plt.boxplot(x)
plt.title("Boxplot Using Matplotlib")
plt.show()


# In[39]:


import matplotlib.pyplot as plt 

Lib1=[28.67193398, 37.67445752, 11.15839875, 14.13138197, 15.80249413, 19.69257731, 14.25780042, 17.43216654, 43.59123231] 
plt.boxplot(Lib1)
plt.title("Tiempos: Libreria 1")
plt.show()


# In[40]:


import matplotlib.pyplot as plt 

Lib2= [113.4356293, 147.1395946, 44.94758459, 57.6075922, 53.6704862, 61.83368747, 123.8178965, 58.25793318, 47.17653714]
plt.boxplot(Lib2)
plt.title("Tiempos: Libreria 2")
plt.show()


# In[43]:


import pandas as pd
import os


# In[41]:


import matplotlib.pyplot as plt 

Lib1=[28.67193398, 37.67445752, 11.15839875, 14.13138197, 15.80249413, 19.69257731, 14.25780042, 17.43216654, 43.59123231] 
Lib2= [113.4356293, 147.1395946, 44.94758459, 57.6075922, 53.6704862, 61.83368747, 123.8178965, 58.25793318, 47.17653714]
plt.boxplot(Lib1)
plt.boxplot(Lib2)
plt.title("Tiempos: Librerias 1 y 2")
plt.show()


# In[78]:


import pandas as pd
import os
file_practica= "C:\\experimento.csv"


# In[79]:


df=pd.read_csv(file_practica, encoding='latin-1')


# In[80]:


df


# In[112]:


df.columns


# In[82]:


df


# In[142]:


import pandas as pd 
import os 
from matplotlib import pyplot as plt
import numpy as np


# In[143]:


mainpath="C:\\"
filename= "experimento.csv"
fullpath= os.path.join(mainpath, filename)


# In[147]:


datos=pd.read_csv(file_practica, encoding='latin-1')
df


# In[164]:


x=datos['Tiempo']
y=datos['Memoria']
plt.scatter(x,y)


# In[165]:


from random import seed
from random import randint
x= ['Ley', 'Libreria', 'Tiempo', 'Memoria']
y= [randint (0,100), randint (0,100), randint (0,100), randint (0,100)]
plt.bar(x,y)
plt.show()


# In[166]:


from numpy.random import seed
from numpy.random import randn
seed(1)
x= [28.67193398, 37.67445752, 11.15839875, 14.13138197, 15.80249413, 19.69257731, 14.25780042, 17.43216654, 43.59123231 * randn(1000), 113.4356293, 147.1395946, 44.94758459, 57.6075922, 53.6704862, 61.83368747, 123.8178965, 58.25793318, 47.17653714 * randn(1000)]
plt.boxplot(x)
plt.show()


# In[167]:


df


# In[ ]:




