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
pointsL = []
pointsH = []
p1 = np.array([-1,0, 0])

p2 = np.array([-1,0, 2])

midL = np.array([0,0,0])
midH = np.array([0,0,2])


ax.set_xlim(-2,2)
ax.set_ylim(-2,2)
ax.set_zlim(-2,2)

tmp = copy.copy(p1)
tmp2 = copy.copy(p2)
for i in range(0,6):

    pointsL.append(tmp)
    tmp = getZmatrix(60).dot(tmp)
    pointsH.append(tmp2)
    tmp2 = getZmatrix(60).dot(tmp2)

pointsL  = np.array(pointsL)
pointsH  = np.array(pointsH)


# ax.scatter3D(pointsL[:, 0], pointsL[:, 1], pointsL[:, 2])
# ax.scatter3D(pointsH[:, 0], pointsH[:, 1], pointsH[:, 2])

face_list = [pointsL,pointsH]
# face = []
for i in range(0,6):
    face = np.array([midH, pointsH[i], pointsL[i], midL])
    face_list.append(face)
collection = Poly3DCollection(face_list, linewidths=1, edgecolors='black', alpha=0.2, zsort='min')
face_color = "salmon"
collection.set_facecolor(face_color)
ax.add_collection3d(collection)

# wirnik = []
# for i in range(0, 6):

# ax.set_zlim(-3,-3)
plt.show(block=False)
end = timeit.timeit()
print(end - start)
input()
