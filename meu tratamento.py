#!/usr/bin/env python
# coding: utf-8

# In[39]:


import pandas as pd
import statistics as sts
import seaborn as srn
import os


# In[4]:


os.chdir('C:/Users/Intel/Desktop/Formação Cientista De Dados/Dados')


# In[5]:


dados = pd.read_csv('tempo.csv', sep = ';')


# In[6]:


dados


# In[7]:


dados.shape


# In[9]:


dados['Aparencia'].describe()


# In[17]:


agrupados = dados.groupby(['Aparencia']).size()
agrupados


# In[24]:


dados.loc[dados['Aparencia'] == 'menos', 'Aparencia'] = 'Sol'


# In[25]:


agrupados = dados.groupby(['Aparencia']).size()


# In[26]:


agrupados


# In[29]:


agrupados = dados.groupby(['Temperatura']).size()
agrupados


# In[32]:


dados['Temperatura'].describe()


# In[37]:


srn.boxplot(dados['Temperatura'])


# In[43]:


mediana = sts.median(dados['Temperatura'])
mediana


# In[44]:


dados.loc[dados['Temperatura'] > 130 , 'Temperatura'] = mediana


# In[45]:


dados['Temperatura'].describe()


# In[46]:


dados['Umidade'].describe()


# In[54]:


median = sts.median(dados['Umidade'])
dados.loc[dados['Umidade'] > 100, 'Umidade'] = median 


# In[55]:


dados['Umidade'].describe()


# In[51]:


agrupados = dados.groupby(['Jogar']).size()
agrupados


# In[52]:


dados.isnull().sum()


# In[58]:


median = sts.median(dados['Umidade'])
dados['Umidade'].fillna(median, inplace = True)
dados.isnull().sum()


# In[61]:


agrupado = dados.groupby(['Vento']).size()
agrupado


# In[62]:


dados['Vento'].isnull().sum()


# In[63]:


dados['Vento'].fillna('FALSO', inplace = True)


# In[64]:


dados['Vento']


# In[ ]:




