import numpy as np
import matplotlib.pyplot as plt

# Define time array and functions
t = np.linspace(0, 86400, 100)  # 24 hours in seconds
Ti = 20 + 10*np.sin(2*np.pi*t/86400)  # internal temperature
Ta = 10 + 5*np.sin(2*np.pi*t/86400)  # ambient temperature

# Define space array and function
L = 10  # length of building in meters
x = np.linspace(0, L, 100)
Ti_x = 20 - 10*np.exp(-x/L)  # internal temperature profile along building length

# Define the parameters
L = 10        # Length of the rod (m)
dx = 0.01    # Spatial step size (m)
T0 = 20      # Initial temperature of the rod (C)
k = 1.5      # Thermal conductivity (W/mC)
rho = 2400   # Density (kg/m^3)
cp = 880     # Specific heat capacity (J/kgC)
h1 = 10      # Heat transfer coefficient at x=0 (W/m^2C)
h2 = 100     # Heat transfer coefficient at x=L (W/m^2C)
tmax = 86400 # Maximum simulation time (s)
dt = 1000      # Time step size (s)
A = 1  # Assuming a cross-sectional area of 1 square meter

# Calculate the constants
alpha = k/(rho*cp)
r1 = h1*dx/(k*A)
r2 = h2*dx/(k*A)
nt = int(tmax/dt) + 1
nx = int(L/dx) + 1

# Initialize the temperature array
T = np.ones((nt,nx))*T0

# Apply the boundary conditions
T[:,0] = T0
T[:,-1] = T0

# Implement the finite difference method
for n in range(1,nt):
    for i in range(1,nx-1):
        T[n,i] = T[n-1,i] + alpha*dt/dx**2*(T[n-1,i+1]-2*T[n-1,i]+T[n-1,i-1])
    T[n,0] = T[n-1,0] + alpha*dt/dx**2*(T[n-1,1]-T[n-1,0]) + 2*h1*dt/(rho*cp*dx)*(Ta[n]-T[n-1,0])
    T[n,-1] = T[n-1,-1] + alpha*dt/dx**2*(T[n-1,-2]-T[n-1,-1]) + 2*h2*dt/(rho*cp*dx)*(Ta[n]-T[n-1,-1])

# Plot the temperature distribution at the final time
plt.plot(np.linspace(0,L,nx),T[-1,:])
plt.xlabel('Position (m)')
plt.ylabel('Temperature (C)')
plt.show()
