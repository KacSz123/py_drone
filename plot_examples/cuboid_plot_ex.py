from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
import numpy as np
import math
import copy
import timeit
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def getZmatrix(ang_deeg):
    rad = math.radians(ang_deeg)
    return np.array([[math.cos(rad),-math.sin(rad), 0],
                     [math.sin(rad), math.cos(rad), 0],
                     [      0      ,    0         , 1]])





start = timeit.timeit()

points = [[ 1,-1, 0],
          [-1,-1, 0],
          [ 1,-1, 1],
          [-1,-1, 1],
          [ 1, 1, 0],
          [-1, 1, 0],
          [ 1, 1, 1],
          [-1, 1, 1]
          ]


# p1 = np.array([-1,0, 0])

# p2 = np.array([-1,0, 2])
face_list = []

a = 1

face = np.array([points[0],points[1],points[3],points[2]])
face_list.append(face)
face = np.array([points[0],points[2],points[6],points[4]])
face_list.append(face)
face = np.array([points[0],points[1],points[5],points[4]])

face = np.array([points[7],points[6],points[4],points[5]])
face_list.append(face)
face = np.array([points[7],points[5],points[1],points[3]])
face_list.append(face)
face = np.array([points[7],points[6],points[2],points[3]])
face_list.append(face)


ax.set_xlim(-2,2)
ax.set_ylim(-2,2)
ax.set_zlim(-2,2)

collection = Poly3DCollection(face_list, linewidths=1, edgecolors='black', alpha=0.2, zsort='min')
face_color = "salmon"
collection.set_facecolor(face_color)
ax.add_collection3d(collection)
z_offset = 0.1
for i in range(0, len(points)):
    ax.scatter3D(points[i][0],points[i][1],points[i][2], color = 'b')
    ax.text(points[i][0],points[i][1],points[i][2]+z_offset, '%s'%(i+1),size=15, zorder=1, color='k')
ax.quiver(-1.5,-1.5, -1., 0, 0, 1, length=2, normalize=True, linewidths=3, color = 'blue')
ax.text(-1.5,-1.5,  -0., '%s'%'Z',size=20)
ax.quiver(-1.5,-1.5, -1., 0, 1, 0, length=2, normalize=True, linewidths=3, color = 'green')
ax.text(-1.5,-0.5,  -1., '%s'%'Y',size=20)
ax.quiver(-1.5,-1.5,  -1., 1, 0, 0, length=2, normalize=True, linewidths=3, color = 'red')
ax.text(-0.5,-1.5,  -1., '%s'%'X',size=20)
# wirnik = []
# for i in range(0, 6):

# ax.set_zlim(-3,-3)
plt.show(block=False)
end = timeit.timeit()
print(end - start)
input()
