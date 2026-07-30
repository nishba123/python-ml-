#!/usr/bin/env python
# coding: utf-8

# In[7]:


a=int(input("enter a number"))
b=int(input("enter a number"))
ch=int(input("enter your choice \n 1.addition \n2.subtraction \n3.multiplication \n4.division\n"))

if ch==1:
    print(a+b)
elif ch==2:
    print(a-b)
elif ch==3:
    print(a*b)
elif ch==4: 
    print(a/b)
else:
    print("invalid choice")
        


# In[ ]:


a=int(input("enter a number"))
b=int(input("enter a number"))
print("a&b",a and b)
print("a|b",a or b)
print("a!b",not b)
print("less than or equal to",a <= b)
print("greater than or equal to",a >= b)
print(a>b)
print(a<b)
print(a==b)


# In[1]:


dict1={"rollno":18,"age":21}
dict2={"Name":"nishba","place":"malappuram"}
dict1.update(dict2)
print(dict1)


# In[2]:


num1=int(input("enter first number"))
num2=int(input("enter second number"))
num3=int(input("enter third number"))
if num1>num2 & num1>num3:
    print(num1,"is greater")
elif num2>num1 & num2>num3:
    print(num2,"is greater")
else:
    print(num3,"is greater")


# In[9]:


list1=[2,3,4]

list1.append(9)
print(list1)

list1.insert(0,3)
print(list1)

list1.remove(4)
print(list1)

list1.pop()
print(list1)


# In[ ]:




