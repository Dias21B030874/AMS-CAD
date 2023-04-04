import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize


# Define the heat equation function
def heat_eqn(x, k0):
    ro = 2700  # Density of aluminum (kg/m^3)
    cp = 900  # Specific heat capacity of aluminum (J/kg-K)
    T0 = 20  # Initial temperature (°C)
    L = 0.1  # Length of aluminum bar (m)
    t_final = 600  # Final time (s)

    # Define the spatial and temporal discretization
    dx = x[1] - x[0]
    dt = 0.1

    # Calculate the thermal diffusivity
    alpha = k0 / (ro * cp)

    # Initialize the temperature profile
    T = np.zeros_like(x)
    T[0] = T[-1] = T0

    # Calculate the temperature profile using finite differences
    for n in range(int(t_final / dt)):
        T[1:-1] += alpha * dt / dx ** 2 * (T[2:] - 2 * T[1:-1] + T[:-2])

    return T


# Define the objective function to minimize
def objective(k0, x_exp, T_exp):
    T_pred = heat_eqn(x_exp, k0)
    return np.sum((T_pred - T_exp) ** 2)


# Load the experimental data
x = np.linspace(0, 0.1, 101)
T_exp = np.array([20, 21, 24, 31, 41, 53, 63, 70, 75, 77, 78])
x_exp = x[::10]  # select every 10th element from x

# Find the optimal value of k0
k0_init = 150
result = minimize(objective, k0_init, args=(x_exp, T_exp))
k0_opt = result.x[0]

# Predict the temperature profile using the optimal value of k0
T_pred = heat_eqn(x_exp, k0_opt)

# Plot the experimental data and the model predictions
plt.plot(x_exp, T_exp, 'o', label='Experimental Data')
plt.plot(x_exp, T_pred, '-', label='Model Predictions')
plt.xlabel('Distance (m)')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.show()
