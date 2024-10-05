#Code by GVV Sharma
#July 22, 2024
#released under GNU GPL
#Line 


import sys                                          #for path to external scripts
sys.path.insert(0, '/home/koushik/matgeo/codes/CoordGeo')        #path to my scripts
import numpy as np
import mpmath as mp
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import ctypes

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen


#if using termux
import subprocess
import shlex
#end if

# Load the shared library
mylib = ctypes.CDLL('./intercept.so')  # Use '.dll' for Windows

# Define the argument and return types
mylib.find_x_intercept.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.c_float, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float)]
mylib.find_x_intercept.restype = None

# Prepare data
n = np.array([3.0, -1.0], dtype=np.float32)
c = -2.0
x_intercept = ctypes.c_float()
y_intercept = ctypes.c_float()

# Call the C function
mylib.find_x_intercept(n.ctypes.data_as(ctypes.POINTER(ctypes.c_float)), c, ctypes.byref(x_intercept), ctypes.byref(y_intercept))
# Extract values from ctypes.c_float
x_intercept_value = x_intercept.value
y_intercept_value = y_intercept.value

# Create NumPy array using the extracted values
C = np.array(([x_intercept_value, 0])).reshape(-1, 1)
#Given Points
A = np.array(([-2, 0])).reshape(-1,1) 
B = np.array(([1, 0])).reshape(-1,1)
#Line parameters
n = np.array(([3, -1])).reshape(-1,1)  
c = -2  
n1 = np.array(([1, 0])).reshape(-1,1)
c1=-2
n2 = np.array(([1, 0])).reshape(-1,1)
c2=1
k1 = -6
k2 = 6
#Generating Lines
x_A = line_norm(n,c,k1,k2)
x_B = line_norm(n1,c1,k1,k2)
x_C = line_norm(n2,c2,k1,k2)

#Plotting all lines
plt.plot(x_A[0,:],x_A[1,:],label=r'$(3 ~-1)\mathbf{x}=-2$')
plt.plot(x_B[0,:],x_B[1,:],label=r'$x=-2$')
plt.plot(x_C[0,:],x_C[1,:],label=r'$x=1$')
# Define colors for each point
colors = ['red', 'blue','green']  # Provide a color for each point A and B

# Labeling the coordinates
tri_coords = np.block([[A, B, C]])  # Shape (2, 2)
plt.scatter(tri_coords[0, :], tri_coords[1, :], c=colors)

# Annotate points A and B
vert_labels = ['A(-2,0)', 'B(1,0)','C']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt,  # this is the text
                 (tri_coords[0, i], tri_coords[1, i]),  # this is the point to label
                 textcoords="offset points",  # how to position the text
                 xytext=(0, 10),  # distance from text to points (x,y)
                 ha='center')  # horizontal alignment

# Use set_position for axes
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

plt.legend(loc='best')
plt.grid()  # minor
plt.axis('equal')
plt.xlabel('x')
plt.ylabel('y')
plt.title('The graph of Line y=3x+2 ')
plt.show()
