#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt

#initializing the data
x = [10, 20, 30, 40]
y = [20, 25, 35, 55]

# plotting the data plt.plot(x, y)
plt.plot(x,y)

plt.show()


# In[4]:


import matplotlib.pyplot as plt

#initializing the data
x = [10, 20, 30, 40]
y = [20, 25, 35, 55]

# plotting the data plt.plot(x, y)
plt.plot(x,y)

#adding title to the plot
plt.title("Linear graph", fontsize=25, color="green")

plt.show()


# In[5]:


import matplotlib.pyplot as plt

#initializing the data
x = [10, 20, 30, 40]
y = [20, 25, 35, 55]

# plotting the data plt.plot(x, y)
plt.plot(x,y)

#adding title to the plot
plt.title("Linear graph", fontsize=25, color="green")

#adding label on the y-axis
plt.ylabel('Y-Axis')

#adding label on the y-axis
plt.xlabel('X-Axis')

plt.show()


# In[6]:


import matplotlib.pyplot as plt

#initializing the data
x = [10, 20, 30, 40]
y = [20, 25, 35, 55]

# plotting the data plt.plot(x, y)
plt.plot(x,y)

#adding title to the plot
plt.title("Linear graph", fontsize=25, color="green")

#adding label on the y-axis
plt.ylabel('Y-Axis')

#adding label on the y-axis
plt.xlabel('X-Axis')

#Setting the limit of y-axis
plt.ylim(0,80)

#setting the limiy of y-axis
plt.xticks(x, labels=["one", "two", "three", "four"])

#adding legends
plt.legend(["GFG"])

plt.show()


# In[9]:


# Python program to show pyplot module 
import matplotlib.pyplot as plt 
from matplotlib.figure import Figure

#initializing the data 
x = [10, 20, 30, 40] 
y = [20, 25, 35, 55]

# Creating a new figure with width = 5 inches # and height = 4 inches
fig = plt.figure(figsize =(5, 4))

# Creating first axes for the figure 
ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])

# Creating second axes for the figure 
ax2 = fig.add_axes ([1, 0.1, 0.8, 0.8])

# Adding the data to be plotted
ax1.plot(x, y)
ax2.plot(y, x)

plt.show()


# In[11]:


import pandas as pd

data = pd.read_csv("data bank.csv")

display(data.head(10))


# In[15]:


import pandas as pd 
import matplotlib.pyplot as plt
# reading the database 
data = pd.read_csv("data bank.csv")
# Scatter plot with day against tip 
plt.scatter (data['month'], data['education'])
# Adding Title to the Plot 
plt.title("Scatter Plot")
# Setting the X and Y Labels
plt.xlabel('month')
plt.ylabel('Education')

#saving the figure
plt.savefig("scatter plot1.jpg")

plt.show()


# In[13]:


import pandas as pd 
import matplotlib.pyplot as plt

# reading the database 
data = pd.read_csv("data bank.csv")

# Scatter plot with day against tip 
plt.plot(data['month'])
plt.plot(data['education'])

# Adding Title to the Plot 
plt.title("Scatter Plot")

# Setting the X and Y Labels
plt.xlabel('month')
plt.ylabel('education')

#saving the figure
plt.savefig("scatter plot2.jpg")

plt.show()


# In[17]:


import pandas as pd 
import matplotlib.pyplot as plt

# reading the database 
data = pd.read_csv("data bank.csv")

# Scatter plot with day against tip 
plt.scatter(data['job'], data['marital'], c=data['age'],
            s=data['duration'])

# Adding Title to the Plot 
plt.title("Scatter Plot")

# Setting the X and Y Labels
plt.xlabel('job')
plt.ylabel('marital')

plt.colorbar()

#saving the figure
plt.savefig("scatter plot3.jpg")

plt.show()


# In[12]:


import pandas as pd 
import matplotlib.pyplot as plt

# reading the database 
data = pd.read_csv("data bank.csv")

# Scatter plot with day against tip 
plt.bar(data['month'], data['education'])

# Adding Title to the Plot 
plt.title("Bar Chart")

# Setting the X and Y Labels
plt.xlabel('month')
plt.ylabel('education')

#saving the figure
plt.savefig("barchart output.jpg")

plt.show()


# In[10]:


import pandas as pd 
import matplotlib.pyplot as plt

# reading the database 
data = pd.read_csv("data bank.csv")

# Scatter plot with day against tip 
plt.hist(data['balance'])

# Adding Title to the Plot 
plt.title("Histogram")

#saving the figure
plt.savefig("histogram output.jpg")

plt.show()


# In[8]:


import pandas as pd 
import matplotlib.pyplot as plt

# reading the database 
data = pd.read_csv("data bank.csv")

# Scatter plot with day against tip 
job = ['admin', 'services', 'technician', 'management', 'retired']
age = [59, 41 , 28 , 56 , 60]

#plotting the data
plt.pie(age, labels=job)

# Adding Title to the Plot 
plt.title("Job data")

plt.show()


# In[ ]:




