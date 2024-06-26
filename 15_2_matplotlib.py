# -*- coding: utf-8 -*-
"""15/2  matplotlib.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Xr8nw_Q_jqfflpCuShEAMZlgGMAPza1c

data visualization using python
"""



"""basic plotting in matplotlib"""

!pip install matplotlib==3.4

from matplotlib import pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np
print("step 1")

"""we start creating a figure and an axes in their simplest form"""

#empty
fig=plt.figure()
ax=plt.axes()
ax.grid()

"""the figure can be thought of as a single container that contains all the objectsrepresinting axes,graphics,text and labels.the axes is what we see above"""

fig=plt.figure()
ax=plt.axes()
x=np.linspace(0,10,1000)
ax.plot(x,np.sin(x));

#lets add a title and labels to the plots
fig=plt.figure()
ax=plt.axes()
x=np.linspace(0,10,1000)
ax.plot(x,np.sin(x))
ax.set_title('Simple Plot')#add a title
ax.set_xlabel('x label')#add x label
ax.set_ylabel('y label')#add y label

#lets add a title to the plot
fig=plt.figure()
ax=plt.axes()
x=np.linspace(0,10,1000)
ax.plot(x,np.sin(x))
ax.plot(x,np.cos(x))
#ax.plot(x,np.tan(x))
ax.set_title('Mutliple Lines')
ax.set_xlabel('x label')
ax.set_ylabel('y label')
plt.show

#lets add a title to the plot
fig=plt.figure()
ax=plt.axes()
x=np.linspace(0,10,1000)
ax.plot(x,np.sin(x),label='sin',color='red') #specfiy color by name
ax.plot(x,np.cos(x),label='cos',color='g')  #specify color by short code
ax.set_title('Mutliple Lines')
ax.set_xlabel('x label')
ax.set_ylabel('y label')
ax.legend()

#lets add a title to the plot
fig=plt.figure()
ax=plt.axes()
#ax.grid(linestyle='--;)
x=np.linspace(0,10,1000)
ax.plot(x,np.sin(x),label='sin',linestyle ='dashed')
ax.plot(x,np.cos(x),label='cos',linestyle='dotted')
ax.plot(x,np.sin(x+1),label='sin',linestyle ='dashdot')
ax.set_title('Mutliple Lines')
ax.set_xlabel('x label')
ax.set_ylabel('y label')
ax.legend()

fig=plt.figure()
ax=plt.axes()
x=np.linspace(0,10,1000)
ax.plot(x,np.sin(x))
ax.set_xlim(-5,15)
ax.set_ylim(-3,3)

fig,ax=plt.subplots()

fig,axs=plt.subplots(2,2,figsize=(10,6))
x=np.linspace(0,10,1000)
axs[0,0].plot(x,np.sin(x))
axs[0,1].plot(x,np.cos(x),color='maroon')
axs[1,0].plot(x,np.sin(x+2),color='blue')
axs[1,1].plot(x,np.sin(x+4),color='green')

data={'apple':10,'orange':15, 'lemon':5,'lime':20}
names=list(data.keys())
values=list(data.values())
fig=plt.figure()
ax=plt.axes() #color:grayscales 0-1
ax.bar(names,values);

data={'apple':10,'orange':15, 'lemon':5,'lime':20}
names=list(data.keys())
values=list(data.values())
fig=plt.figure(figsize=(4,3))
ax=plt.axes()
ax.bar(names,values,color='teal',width=0.35)
ax.set_xlabel('fruit')
ax.set_ylabel('quatity')
ax.set_title('fruit quatity')

data={'apple':10,'orange':15, 'lemon':5,'lime':20,
      'pomegrate':11,'banana':13,'pear':9}
names=list(data.keys())
values=list(data.values())
ax=plt.axes()
ax.barh(names,values)
ax.set_xlabel('quatity')
ax.set_ylabel('fruit')
ax.set_title('fruit quatity')

labels=['G1','G2','G3','G4','G5']
men_means=[20,34,30,35,27]
women_means=[25,32,34,20,25]
x=np.arange(len(labels)) #lavel location
width=0.25 #width
fig,ax=plt.subplots()
rects1=ax.bar(x-width/2,men_means,width,label='Men')
rects2=ax.bar(x+width/2,women_means,width,label='Women')
#add some text for labels ,title and custom x-axis tick labels ,etc.
ax.set_ylabel('scores')
ax.set_title('scores by group and gender')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
#plot show

fig,ax=plt.subplots()
ax.grid(linestyle='--',color='0.75',axis='y')
ax.set_axisbelow(True)  #grid below chart
rects1=ax.bar(x-width/2,men_means,width,label='Men')
rects2=ax.bar(x+width/2,women_means,width,label='Women')
#add some text for labels ,title and custom x-axis tick labels ,etc.
ax.set_ylabel('scores')
ax.set_title('scores by group and gender')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
#add bar label
ax.bar_label(rects1,padding=3)
ax.bar_label(rects2,padding=3)
ax.set_ylim(0,40)

"""stacked bar chart"""

fig,ax=plt.subplots()
ax.grid(linestyle='--',color='0.75',axis='y');
ax.set_axisbelow(True)#grid behind bars
p1=ax.bar(labels,men_means,width,label='Men')
p2=ax.bar(labels,women_means,width,bottom=mean_means,label='women')
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.legend()
#label with label_type'center' instead of the default edge
ax.bar_label(p1, label_type='center')
ax.bar_label(p2, label_type='center')
ax.bar_label(p2)
ax.bar_ylim(0,70);

x=np.random.randn(20)
y=np.random.randn(20)
fig,ax=plt.subplots()
ax.scatter(x,y);

fig,ax=plt.subplots()
ax.scatter(x,y,marker='x')

fig,axs=plt.subplots(2,3,sharex=True,sharey=True,sharey=True,figsize=(16,12))
#marker symbol




#marker from path
verts=[[-1,-1],[1,-1],]

"""colors"""

plt.style.use('seaborn-darkgrid')
z1=np.sqrt(x**2 + y**2)
fig,ax=plt.subplots()
pos=ax.scatter(x,y,c=z1,cmap='cool',marker='3')
fig.colorbar(pos)

x=np.random.randn(100)
y=np.random.randn(100)
z1=np.sqrt(x**2 +y**2)
z2=np.random.randint(10,200,size=len(x))
fig,ax=plt.subplots()
pos=ax.scatter(x,y,c=z1,s=z2,alpha=0.55,cmap='viridis')
fig.colorbar(pos);

x=np.linspace(0,10,30)
y=np.sin(x)
plt.plot(x,y,'o',color='violet')

#create some data
spread=np.random.rand(50)*100
center=np.ones(25)*50
flier_high=np.random.rand(10)*100+100
flier_low=np.random.rand(10)*-100
data=np.concatenate((spread,center,flier_high,flier_low))
#basic boxplot
fig,ax=plt.subplots()
ax.boxplot(data)
ax.set_title('basic box plot')

#notched boxplot without outliers
fig,ax=plt.subplots()
ax.boxplot(data,1,'')
ax.set_title('Notched box plot without outliers')