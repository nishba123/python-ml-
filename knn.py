#!/usr/bin/env python
# coding: utf-8

# In[2]:


from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

iris=load_iris()
X=iris.data
y=iris.target

print(iris.feature_names)
print(iris.target_names)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
knn=KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train,y_train)
y_pred=knn.predict(X_test)
accuracy=accuracy_score(y_test,y_pred)
print(f'accuracy:{accuracy:.2f}')
print(y_pred[0])
new=[[1.2,2.2,3.2,4.2]]
new_pred=knn.predict(new)
print(iris.target_names[new_pred])


# In[9]:


from sklearn.datasets import load_breast_cancer
breast_cancer=load_breast_cancer()
X=breast_cancer.data
y=breast_cancer.target
print(X)
print(y)
print(breast_cancer.feature_names)
print(breast_cancer.target_names)


X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
knn=KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train,y_train)
y_pred=knn.predict(X_test)
accuracy=accuracy_score(y_test,y_pred)
print(f'accuracy:{accuracy:.2f}')
print(y_pred[0])
new=[[1.2,2.2,3.2,4.2,1.2,2.2,3.2,4.2,1.2,2.2,3.2,4.2,1.2,2.2,3.2,4.2,1.2,2.2,3.2,4.2,1.2,2.2,3.2,4.2,1.2,2.2,3.2,4.2,2.5,3.3]]
new_pred=knn.predict(new)
print(breast_cancer.target_names[new_pred])


# In[ ]:




