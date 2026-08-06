#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np
a=np.array([[2,5],[6,3]])
b=np.array([[4,2],[7,1]])
print("add=\n",np.array(a+b))
print("sub=\n",np.array(a-b))
print("mul=\n",np.array(a*b))
print("div=\n",np.array(a/b))
print("matrix multiplication=\n",np.dot(a,b))
print("transpose of A=\n",np.transpose(a))
print("transpose of B=\n",np.transpose(b))




# In[13]:


import numpy as np
X=np.array([[1,2,3],[4,5,6],[7,8,9]])
U,S,VT=np.linalg.svd(X)
n_components=2
X_reconstructed=np.dot(U[:,:n_components],np.dot(np.diag(S[:n_components]),VT[:n_components,:]))
print("original matrix:")
print(X)
print("\nReconstructed Matrix(with reduced dimensions):")
print(X_reconstructed)


# In[19]:


import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[1,4,2,5]
plt.plot(x,y)
plt.title("graph")
plt.xlabel("length")
plt.ylabel("time")


# In[21]:


import matplotlib.pyplot as plt
subjects=["physics","Data science","iot"]
marks=[80,78,90]
plt.bar(subjects,marks)
plt.title("Result")
plt.xlabel("subject")
plt.ylabel("mark")


# In[22]:


import matplotlib.pyplot as plt
subjects=["physics","Data science","iot"]
marks=[80,78,90]
plt.scatter(subjects,marks)
plt.title("Result")
plt.xlabel("subject")
plt.ylabel("mark")


# In[28]:


import matplotlib.pyplot as plt

marks=[10,10,20,20,20,30,30,30,30,40,40,40,40,50,50]
plt.hist(marks)
plt.legend("profit")
plt.title("Result")
plt.xlabel("subject")
plt.ylabel("mark")


# In[37]:


import matplotlib.pyplot as plt

marks=[10,40,50,80]
subjects=["physics","maths","daa","french"]
plt.pie(marks,labels=subjects)
plt.show()


# In[40]:


import matplotlib.pyplot as plt
x=[1,2,6,18]
y=[3,10,12,20]
plt.plot(x,y,'r:o')
plt.title("plot")


# In[43]:


import matplotlib.pyplot as plt
x=np.array([0,1,2,3])
y=np.array([3,8,1,10])
plt.subplot(1,2,1)
plt.plot(x,y)
plt.suptitle("SUBPLOT")
x=np.array([0,1,2,3])
y=np.array([3,8,1,10])
plt.subplot(1,2,2)
plt.plot(x,y)


# In[ ]:




