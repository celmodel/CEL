# -*- coding: utf-8 -*-
"""
Created on Thu May 12 15:10:51 2019

@author: Ragnar Kobin
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

%matplotlib notebook


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


_x = np.arange(9)
print("_x",_x)
_y = np.arange(5)
print("_y",_y)
_xx, _yy = np.meshgrid(_x, _y)
print("_xx",_xx)
print("_yy",_yy)
x, y = _xx.ravel(), _yy.ravel()
print("x",x)
print("y",y)
dz = x + y
z = np.zeros_like(dz)
print("z",z)
dx = dy = 0.5

#LS19
#dz=  [1,1,1,1,1,0,0,0,0,   0,1,1,0,1,0,0,0,0,  0,0,0,0,0,0,1,0,0,  1,1,0,0,0,1,0,0,1,  0,3.1,0.9,3.4,1.6,0,1,0,0]
#XS19
dz=  [1,1,1,0,0,0,0,0,0,   1,1,1,0,1,0,0,0,0,  0,0,0,0,1,0,0,0,0,  1,1,0,0,0,0,1,1,1,  0,0.5,1,2.9,1,2.5,2.1,0,0]
    
'''
print("x= ",x)
print("y= ",y)
print("z= ",z)
print("dx= ",dx)
print("dy= ",dy)
print("dz= ",dz)
'''
#ax.bar3d(x, y, z, dx, dy, dz, color='#00ceaa')
ax.bar3d(x, y, z, dx, dy, dz, color='r')

#ax.set_title('Locked Shields 2019 CEL model')
ax.set_title('Crossed Swords 2019 CEL model')
ax.set_xlabel('Level')
ax.set_ylabel('')
ax.set_zlabel('Occurrence')

locs, labels = plt.yticks()
plt.yticks(np.arange(6), ('', 'Level', 'Sector', 'Type', 'CI vector', 'Category'), rotation=5)

plt.gca().invert_xaxis()
plt.show()