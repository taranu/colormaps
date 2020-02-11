#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Required imports
import cmasher as cmr
import matplotlib as mpl
import matplotlib.colors as mplcol
import matplotlib.pyplot as plt
import seaborn as sns
import viscm.gui as vg


# In[2]:


# Setup for plotting
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set_style('whitegrid')
mpl.rcParams['figure.figsize'] = (12, 9)
mpl.rcParams['figure.dpi'] = 100
#sns.set(rc={'axes.facecolor': '0.85', 'figure.facecolor': 'w'})


# In[3]:


# Plot a colormap
def plot_cmap(cmap, name, method="CatmulClark", uniform_space="CAM02-UCS", fig=None):
    if fig is None:
        fig = plt.figure()
    #figureCanvas = vg.FigureCanvas(fig)
    v = vg.viscm(cmap, name=name, figure=fig, uniform_space=uniform_space)


# In[4]:


# CB2 RdBu
plot_cmap(mplcol.ListedColormap(sns.color_palette("RdBu", 100)), 'CB2 RdBu')


# In[5]:


# CB2 RdYlBu
plot_cmap(mplcol.ListedColormap(sns.color_palette("RdYlBu", 100)), 'CB2 RdYlBu')


# In[6]:


# cmasher fusion
plot_cmap(cmr.fusion, 'cmasher fusion')

