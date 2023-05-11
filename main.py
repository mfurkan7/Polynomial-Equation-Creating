import matplotlib.pyplot as plt
import numpy as np

# Voltage and time data
voltage = [4, 4.25, 4.5, 4.75, 5, 5.25, 5.5, 5.75, 6]
time = [600, 560, 520, 490, 450, 430, 405, 390, 380]

# Polynomial coefficients
coeffs = np.polyfit(voltage, time, 2)

# Polynomial equation
a, b, c = coeffs
equation = f"T = {a:.3f}v^2 + {b:.3f}v + {c:.3f}"

# Print the equation
print("Polynomial equation:", equation)

# Plot the data
plt.plot(voltage, time, 'o', label='Data')

# Calculate the polynomial function and add it to the plot
x = np.linspace(min(voltage), max(voltage), 100)
y = a*x**2 + b*x + c
plt.plot(x, y, label='Polynomial equation')

# Add axis labels and plot title
plt.xlabel('Voltage')
plt.ylabel('Time')
plt.title('Voltage-Time Relationship with Polynomial Function')

# Show the plot
plt.legend()
plt.show()