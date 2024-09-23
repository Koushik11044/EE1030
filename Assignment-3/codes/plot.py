#Code by GVV Sharma
#September 12, 2023
#Revised July 21, 2024
#released under GNU GPL
#Point Vectors


import sys                                          #for path to external scripts
sys.path.insert(0, '/home/koushik/matgeo/codes/CoordGeo')        #path to my scripts
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

#if using termux
import subprocess
import shlex
#end if

#Given points
O = np.array(([0, 0])).reshape(-1,1)
B = np.array(([5, 0])).reshape(-1,1)
A = np.array(([0, 3])).reshape(-1,1)
C = np.loadtxt("output.dat").reshape(-1,1)

#Generating all lines
x_OB = line_gen(O,B)
x_OA = line_gen(A,O)
x_BC = line_gen(B,C)
x_AC = line_gen(A,C)
x_AB = line_gen(A,B)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$Diagonal-AB$')
plt.plot(x_OB[0,:],x_OB[1,:],label='$line-OB$')
plt.plot(x_OA[0,:],x_OA[1,:],label='$line-OA$')
plt.plot(x_AC[0,:],x_AC[1,:],label='$line-AC$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$line-BC$')

#Labeling the coordinates
colors = np.arange(1,5)
tri_coords = np.block([[O,B,A,C]])
plt.scatter(tri_coords[0,:], tri_coords[1,:], c=colors)
vert_labels = ['O','B','A','C']
for i, txt in enumerate(vert_labels):
    #plt.annotate(txt, # this is the text
    plt.annotate(f'{txt}\n({tri_coords[0,i]:.2f}, {tri_coords[1,i]:.2f})',
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(25,5), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

# use set_position
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
'''
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
'''
plt.grid() # minor
plt.axis('equal')
plt.title('Rectangle AOBC')
plt.legend()
plt.show()
