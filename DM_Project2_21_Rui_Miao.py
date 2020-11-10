#!/usr/bin/env python
# coding: utf-8

# In[113]:


import pandas as pd
import numpy as np 


# In[114]:


df=pd.read_csv('E:\Project 2\Earthquakes.csv')
df


# In[118]:


# Printing again 
print("Average magnitude is: {}".format(np.mean(df['Magnitude'])))
print("Average Depth is: {}".format(np.mean(df['Depth'])))


# In[116]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

df.hist(figsize=(10,10))


# In[117]:


import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
plt.style.use('ggplot')

plt.rcParams['axes.facecolor'] = "#b3ffff"
plt.rcParams['figure.facecolor'] ="#b3ffff"
plt.figure(figsize=(18,8))
plt.subplot(1, 4, 1)
plt.title('Magnitude')
sns.violinplot(y='Magnitude',data=df,color='red',linewidth=3)
plt.subplot(1, 4, 3)
plt.title('Depth')
sns.violinplot(y='Depth',data=df,color='blue',linewidth=3)
plt.show()


# In[105]:


sns.distplot(df['Magnitude'])


# In[106]:


sns.distplot(df['Depth'])


# In[107]:


df.hist(by='Magnitude',column = 'Depth')


# In[109]:


df.groupby('Magnitude').median()


# In[110]:


df.groupby('Depth').median()


# In[111]:


corr = df.corr()
corr


# In[112]:


sns.heatmap(corr, annot=True)


# In[104]:


corr = df.corr()
mask = np.zeros_like(corr)
mask[np.triu_indices_from(mask)] = True
with sns.axes_style("white"):
    f, ax = plt.subplots(figsize=(8, 8))
    ax = sns.heatmap(corr,mask=mask,square=True,linewidths=.8,cmap="autumn",annot=True)


# In[103]:


plt.rcParams['axes.facecolor'] = "#ffe5e5"
plt.rcParams['figure.facecolor'] = "#ffe5e5"
sns.pairplot(data=df,hue='Magnitude',plot_kws={'alpha':0.3},palette='hot_r')


# In[102]:


df[(df['Magnitude'] > 8) & (df['Depth'] < 25)].sort_values(by=['Magnitude'], ascending=False)


# In[100]:


plt.rcParams['figure.facecolor'] = "#ffffe6"
plt.rcParams['axes.facecolor'] = "#ffffe6"
plt.figure(figsize=(12,6))
plt.title('Magnitude')
sns.countplot(x='Magnitude',data=df,palette='inferno')
plt.tight_layout()


# In[99]:


plt.rcParams['figure.facecolor'] = "#ffe6f9"
plt.rcParams['axes.facecolor'] = "#ffe6f9"
plt.figure(figsize=(12,6))
plt.title('Magnitude vs Depth')
sns.barplot(x=df['Magnitude'],y='Depth',data=df,palette='magma')
plt.tight_layout()


# In[97]:


#plot the number of earthquakes and depth

ax = df.plot(figsize=(16,8), fontsize=13)
ax.set_xlabel('Number of Earthquakes')
ax.set_ylabel('Depth')

ax.grid()
plt.show()


# In[ ]:


#map


# In[96]:


import pandas as pd
df = pd.read_csv('E:\Project 2\Earthquakes.csv')

import plotly.express as px
fig = px.density_mapbox(df, lat='Latitude', lon='Longitude', z='Magnitude', radius=10,
                        center=dict(lat=0, lon=180), zoom=0,
                        mapbox_style="stamen-terrain")
fig.show()

