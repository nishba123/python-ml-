#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
dict={"roll":[1,2,3],"name":['fathima','nishba','sumaiah']}

a=pd.DataFrame(dict)
print(a)


# In[2]:


list=[1,2,3,4]
list2=pd.Series(list)
print(list2)


# In[3]:


list=[1,2,3,4]
list2=pd.Series(list,index=["w","x","y","z"])
print(list2)


# In[4]:


import pandas as pd
dict={"roll":[1,2,3],"name":['fathima','nishba','sumaiah']}

a=pd.DataFrame(dict)
print(a.loc[0])


# In[2]:


import pandas as pd
a=pd.read_csv("student.csv")
print(a)


# In[7]:


import pandas as pd
a=pd.read_csv("student.csv")
print(a.head(2))


# In[8]:


import pandas as pd
a=pd.read_csv("student.csv")
print(a.tail)


# In[12]:


import pandas as pd
a=pd.read_csv("student.csv")
print(a)
b=a.dropna()
print(b)


# In[13]:


import pandas as pd
a=pd.read_csv("student.csv")
print(a)
b=a.fillna(inplace=true)
print(b)


# In[15]:


import pandas as pd
a=[1,7,2]
myvar=pd.Series(a)
print(myvar)


# In[16]:


import pandas as pd
date_series=pd.date_range(start='2024-11-20',end='2024-11-24')
print("Date Series:")
for date in date_series:
    print(date)


# In[17]:


import pandas as pd
data=[[101,'A',23],
     [102,'B',25],
     [103,'c',22]]
df=pd.DataFrame(data,columns=['ID','Name','Age'])
print("2D List to DataFrame:")
print(df)


# In[18]:


import pandas as pd
data={
    "calories":[420,380,390],
    "duration":[50,40,45]
}
df=pd.DataFrame(data)
print(df)


# In[19]:


import pandas as pd
df=pd.DataFrame({
    'Roll':[1,2,3,4,5,6,7],
    'Name':['A','B','C','D','E','F','G'],
    'Marks':[78,82,90,65,85,92,70]
})
print("Head of the DataFrame:")
print(df.head())
print("\nTail of the DataFrame:")
print(df.tail())


# In[21]:


import pandas as pd
import numpy as np

df=pd.DataFrame({
    'A':[10,np.nan,30],
    'B':[np.nan,50,60]
})
print("original DataFrame with Nan:")
print(df)
df_filled=df.fillna(0)
print("\nDataFrame after Replacing Nan with 0:")
print(df_filled)


# In[24]:


import pandas as pd
df=pd.DataFrame({
    'ID':[1,2,3,4],
    'Name':['A','B','C','D'],
    'Age':[20,21,19,22]
})
selected_rows=df.iloc[[1,3]]
print("Selected Rows:")
print(selected_rows)


# In[ ]:





# In[ ]:




