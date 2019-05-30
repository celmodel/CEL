''' 3D visualization of LS, XS and CC exercise CEL model data in Jupiter Notebook
    Author: Ragnar Kobin
'''

from IPython import get_ipython
get_ipython().magic('reset -sf')

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

%matplotlib notebook


fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

dx = dy = 0.5

x = [0,1,2,3, 4, 5, 6,7,8,0,1,2,3,4,5,6,7,8,0,1,2,3, 4, 5, 6 ,7, 8, 0 ,1, 2, 3,4,5,6,7,8,0,1,2,3,4, 5, 6, 7, 8]
y= [0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,]

dz =[[1,1,1,1,1,0,0,0,0,   0,1,1,0,1,0,0,0,0,  0,0,0,0,0,0,1,0,0,  1,1,0,0,0,1,0,0,1,  0,0,0,0,0,0,0,0,0], 
     [1,1,1,0,0,0,0,0,0,   1,1,1,0,1,0,0,0,0,  0,0,0,0,1,0,0,0,0,  1,1,0,0,0,0,1,1,1,  0,0,0,0,0,0,0,0,0],
     [1,1,1,1,1,0,0,0,0,   1,1,1,0,1,0,0,0,0,  0,0,0,0,0,0,1,0,0,  1,1,0,0,0,1,0,0,1,  0,0,0,0,0,0,0,0,0]]
            
z = np.zeros_like(dz)
                                                        
colors = ['b', 'r','y']
nr=3
_z = z
for i in range(nr):
    ax.bar3d(x, y, _z[i], dx, dy, dz[i], color=colors[i])
    if i<nr-1:  _z[i+1] = _z[i]+ dz[i]
         
ax.set_title('Locked Shields(B), Crossed Swords(R) and Cyber Coalition(Y)')
ax.set_xlabel('')
ax.set_ylabel('')
ax.set_zlabel('Occurrence')

locs, labels = plt.yticks()
plt.yticks(np.arange(6), ('', 'Level', 'Sector', 'Type', 'CI vector', ''), rotation=5)

plt.gca().invert_xaxis()
plt.show()
