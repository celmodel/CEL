# -*- coding: utf-8 -*-
"""
Created on Thu May 12 15:00:57 2019

@author: ragna
"""

from IPython import get_ipython
get_ipython().magic('reset -sf')

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

%matplotlib notebook

fig = plt.figure()
ax = fig.add_subplot(111, projection = "3d")

ax.set_title('CEL model')
ax.set_xlabel("Level")
ax.set_ylabel("") 
ax.set_zlabel("Exercises")
ax.set_xlim3d(0,15)
ax.set_ylim3d(0,5) 
plt.gca().invert_xaxis()
locs, labels = plt.yticks()
plt.yticks(np.arange(5), ('', 'CEL Level', 'Sector', 'Type', 'CI vector'), rotation=4)


xpos = [1,2,3,4,5, 1,2,3,4,5, 1,2,3,4,5,6,7, 1,2,3,4,5,6,7,8,9,10,11,12,13,14]
ypos = [0,0,0,0,0, 1,1,1,1,1, 2,2,2,2,2,2,2, 3,3,3,3,3,3,3,3,3,3,3,3,3,3]
zpos = np.zeros(31)

dx = np.ones(31)
dy = np.ones(31)
dx = dy = 0.5
#dx = 0,75 
#dy = 0.5
#dz = [np.random.random(9) for i in range(3)]  # the heights of the 4 bar sets
dz= [[1,1,1,1,1,  0,1,1,0,1, 0,0,0,0,0,0,1, 1,0,0,0,1,1,1,0,0,1,1,0,0,1],
     [1,1,1,0,0,  1,1,1,0,1, 0,0,0,0,1,0,0, 1,0,0,1,0,1,1,0,0,0,0,0,1,0], 
     [1,1,1,1,1,  1,1,1,0,1, 0,0,0,0,0,0,1, 1,0,0,0,1,0,1,0,0,0,1,0,0,0]]
print("dz=",dz)

#ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='r')
#'''
_zpos = zpos   # the starting zpos for each bar
colors = ['b', 'r', 'y']
nr=3
for i in range(3):
    ax.bar3d(xpos, ypos, _zpos, dx, dy, dz[i], color=colors[i])
    _zpos += dz[i]    # add the height of each bar to know where to start the next
    #if i<nr-1:  _zpos[i+1] = _zpos[i]+ dz[i]
#'''

    


plt.show()