import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(projection='3d')


data = np.array([[-1.,-1.,0.],
                 [-1., 1.,0.],
                 [ 1., 1.,0.],
                 [ 1.,-1.,0.]])


# Make data
# u = np.linspace(0, 2 * np.pi, 100)
# v = np.linspace(0, np.pi, 100)
# x = [-1.,-1.,1.,-1.]
# y = [-1., 1.,1., 1.]
# z = [ 0., 0.,0., 0.]       

X = np.array([-1, 1])
Y = np.array([-1, 1])
X, Y = np.meshgrid(X, Y)
print(X)
print(Y)
# R = np.sqrt(X**2 + Y**2)*0
Z = X*0
print(Z)
# # Plot the surface
# ax.plot_surface(X,Y,Z, color='purple', lw=0.5, rstride=1, cstride=1, alpha=0.5)
ax.plot_surface(X, Y, Z, cmap="autumn_r",edgecolor='royalblue', linewidth=1, rstride=1, cstride=1)
# ax.contour(X, Y, Z+1, 10, lw=3, colors="k", linestyles="solid")
# ax.plot_trisurf(data[:,0],data[:,1],data[:,2], linewidth = 1)


# Set an equal aspect ratio
ax.set_aspect('equal')

plt.show()