#!/usr/bin/env python
# coding: utf-8

# # Data Frame

# In[9]:


import pandas as pd
import numpy as np

array1=np.arange(0,20).reshape(5,4)

df=pd.DataFrame(array1, index=["ROW1","ROW2","ROW3","ROW4","ROW5"], columns=["column1","column2","column3","column4"])
df.head()


# In[10]:


#Column indexing
df[['column1','column2']]


# In[13]:


df.loc[['ROW1','ROW2']]


# In[15]:


df.head()
df.iloc[2:4,0:2]


# In[42]:


dic={'name':['a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d'],
    'marks':[50,37,16,27,47,50,37,16,27,47,50,37,16,27,47,50,37,16,27,47]}
df=pd.DataFrame(dic)
df
data_new=df.groupby('name')
data_new
for x,y in data_new:
    print(x)
    print(y)

data_new.name.value_counts()
text='the the the the the hellow world'
print('the is number of times: ',text.count('the'))


# In[54]:


import pandas as pd
import numpy as np

array1=np.arange(0,20).reshape(5,4)

df=pd.DataFrame(array1, index=["ROW1","ROW2","ROW3","ROW4","ROW5"], columns=["column1","column2","column3","column4"])
print(df.head())

print('min value :',df.min())
print('max value ',df.max())
print(df.mean())
print(df.median())


# In[68]:


import pandas as pd
dic={'name':['john','joe','smith','horn','john','joe','smith','horn','john','joe','smith','horn','john','joe','smith','horn'],
    'date':['12-jan-2013','12-jan-2013','12-jan-2013','12-jan-2013','13-jan-2014','13-jan-2014','13-jan-2014','13-jan-2014','14-jan-2015','14-jan-2015','14-jan-2015','14-jan-2015','15-jan-2016','15-jan-2016','15-jan-2016','15-jan-2016'],
    'number':[10,20,34,56,78,90,12,34,21,32,43,54,23,56,67,87]}
df=pd.DataFrame(dic)

new=df.pivot(index='name', columns='date', values='number')
print(new)


# In[73]:


#matplotlib
from matplotlib import pyplot as plt
plt.plot([1,2,3],[4,5,1])
plt.title('info')
plt.xlabel('X Axis')
plt.ylabel("Y Axis")
plt.show()


# In[80]:


from matplotlib import pyplot as plt

plt.bar([10,20,30,40],[10,25,30,40], label="Example-1")
plt.bar([5,15,25,35,45],[5,15,25,35,45], label="Example-2", color='g')

plt.legend()
plt.xlabel('X-Axis')
plt.ylabel('Y-Axix')

plt.show()


# In[85]:


from matplotlib import pyplot as plt

ages=[20,23,24,27,5,22,23,25,42,25,21,20,34,32,31,35,37,41,21,23,34,54,65,15,16,17,19,3,4,5,6,7,5,6]
bins=[0,10,20,30,40,50,60,70,80,90,100,110,120,130]

plt.hist(ages,bins,histtype='bar',rwidth=0.8)
plt.title('Histogram')
plt.legend()
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()


# In[92]:


from matplotlib import pyplot as plt
x=[10,40,20,30,60,10]
y=[80,30,40,50,10,70]
plt.scatter(x,y, label="skitscak", color='k')
plt.title("Scatter Daigram")
plt.xlabel('X-Axis')
plt.ylabel('y-Axis')
plt.legend()
plt.show()


# In[101]:


from matplotlib import pyplot as plt
days=[1,2,3,4,5]

sleeping=[7,6,8,2]
eating=[2,5,7,9]
working =[7,2,2,8]
playing=[8,2,6,4]

plt.plot([],[],color='m',label='sleeping',linewidth=5)
plt.plot([],[], color='c',label='Eating',linewidth=5)
plt.plot([],[], color='r', label='Working',linewidth=5)
plt.plot([],[], color='k', label='Playing',linewidth=5)

plt.stackplot(days,sleeping,eating,working,playing, colors=['m','c','r','k'])
plt.title("Stack Plot")
plt.xlabel('X-Axis')
plt.ylabel('y-Axis')
plt.legend()
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




