''' 3D visualization of Crossed Swords 2019 exercise CEL model data in Jupiter Notebook
    Author: Ragnar Kobin
'''


from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

%matplotlib notebook


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


_x = np.arange(9)
_y = np.arange(5)
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()
dz = x + y
z = np.zeros_like(dz)
dx = dy = 0.5

#XS19
dz=  [1,1,1,0,0,0,0,0,0,   1,1,1,0,1,0,0,0,0,  0,0,0,0,1,0,0,0,0,  1,1,0,0,0,0,1,1,1,  0,0.5,1,2.9,1,2.5,2.1,0,0]
    
ax.bar3d(x, y, z, dx, dy, dz, color='r')

ax.set_title('Crossed Swords 2019 CEL model')
ax.set_xlabel('Level')
ax.set_ylabel('')
ax.set_zlabel('Occurrence')

locs, labels = plt.yticks()
plt.yticks(np.arange(6), ('', 'Level', 'Sector', 'Type', 'CI vector', 'Category'), rotation=5)

plt.gca().invert_xaxis()
plt.show()