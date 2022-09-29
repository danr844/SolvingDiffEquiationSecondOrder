# Simulation of motion of pendulum 

import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

# function that return dz\\dt
def model(theta,t,b,g,l,m):
	theta1 = theta [0]
	theta2 = theta [1]
	dtheta1_dt = theta2
	dtheta2_dt = -(b/m)*theta2 - (g/l)*math.sin(theta1)
	dtheta_dt = [dtheta1_dt,dtheta2_dt]
	return dtheta_dt

# Input
b=0.05  # damping coefficient.
g=9.81  # gravity in m/s2
l=1     # length of the pendulum in m
m=0.1   # mass of the ball in kg

# Initial condition
theta_0 = [0,3]

# Time points
t = np.linspace(0,20,150)

# Solve ODE
theta = odeint(model,theta_0,t,args =(b,g,l,m))

# Plot 
plt.plot(t,theta[:,0],b, label = theta_1/dt = theta2)
plt.plot(t,theta[:,1],\'r--\',label = r\'$\\frac{d\\theta2}{dt} = -\\frac{b}{m}\\theta_2 -\\frac{g}{l}sin\\theta_1 $\')
plt.xlabel(\'Time\')
plt.ylabel(\'Plot\')
plt.xlim([0,12])
plt.legend(loc = \'best\')
plt.show()