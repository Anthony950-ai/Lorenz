# my name is Anthony O'Neal and this is my work
# Lorenz attractor code for self organized criticality project
#
import numpy as np
import matplotlib.pyplot as plt
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
from scipy.integrate import odeint

# array for rayleigh's number values
arr = [5,10,15,20]

#loop through values plotting for each one
for i in arr:

    #save current value for plot titles
    currR = i
    def lorenz(x, y, z, s=10, r=i, b=2.667):
        '''
        Given:
           x, y, z: a point of interest in three dimensional space
           s, r, b: parameters defining the lorenz attractor
        Returns:
           x_dot, y_dot, z_dot: values of the lorenz attractor's partial
               derivatives at the point x, y, z
        '''
        x_dot = s*(y - x)
        y_dot = r*x - y - x*z
        z_dot = x*y - b*z
        return x_dot, y_dot, z_dot

    def xdot(x,y):
        return 10*(y - x)


    dt = 0.01
    num_steps = 10000

    # Need one more for the initial values
    xs = np.empty(num_steps + 1)
    ys = np.empty(num_steps + 1)
    zs = np.empty(num_steps + 1)

    # Set initial values
    xs[0], ys[0], zs[0] = (0., 1., 1.05)

    # Step through "time", calculating the partial derivatives at the current point
    # and using them to estimate the next point
    for i in range(num_steps):
        x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i])
        xs[i + 1] = xs[i] + (x_dot * dt)
        ys[i + 1] = ys[i] + (y_dot * dt)
        zs[i + 1] = zs[i] + (z_dot * dt)

    #plot for each of the of the x,y, and z variables for every step
    ts = np.linspace(0,10001,10001)
    print(ts)
    print(xs)
    print(len(xs))
    print(len(ts))
    plt.plot(ts, xs)
    plt.xlabel("t")
    plt.ylabel("x(t)")
    plt.title("x(t); r =" + str(currR))
    plt.show()

    plt.plot(ts,ys)
    plt.xlabel("t")
    plt.ylabel("y(t)")
    plt.title("y(t); r =" + str(currR))
    plt.show()

    plt.plot(ts,zs)
    plt.xlabel("t")
    plt.ylabel("z(t)")
    plt.title("z(t); r =" + str(currR))
    plt.show()

    # Plot
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    ax.plot(xs, ys, zs, lw=0.5)
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    ax.set_title("Lorenz Attractor")

    plt.show()
