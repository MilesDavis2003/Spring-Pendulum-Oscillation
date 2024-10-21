import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Parameters
m = 1.0     # mass of the block
M = 0.5     # mass of the pendulum
g = 9.81    # acceleration due to gravity
l = 1.0     # length of the pendulum
k = 50.0    # spring constant

# Define the system of differential equations
def equations(u, t, m, M, l, k, g):
    x, x_dot, theta, theta_dot = u

    # Accelerations
    x_ddot = (-k*x + M*l*theta_dot**2*np.sin(theta) - M*g*np.sin(theta)*np.cos(theta)) / (m + M)
    theta_ddot = (-g*np.sin(theta) - x_ddot*np.cos(theta)) / l

    return [x_dot, x_ddot, theta_dot, theta_ddot]

# Initial conditions: [x, x_dot, theta, theta_dot]
initial_conditions = [0.0, 0.0, np.pi/4, 0.0]  # x=0, theta=45 degrees

# Time points
t = np.linspace(0, 20, 1000)

# Solve the equations
sol = odeint(equations, initial_conditions, t, args=(m, M, l, k, g))

# Extract solutions
x_t = sol[:, 0]
theta_t = sol[:, 2]

# Plot results
plt.figure()
plt.plot(t, x_t, label='Displacement of mass (x)')
plt.plot(t, theta_t, label='Pendulum angle (theta)')
plt.legend()
plt.xlabel('Time (s)')
plt.ylabel('Displacement/Angle')
plt.title('Coupled Spring-Pendulum System')
plt.show()
