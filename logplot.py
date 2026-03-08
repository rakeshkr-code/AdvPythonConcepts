import matplotlib.pyplot as plt
import numpy as np

# Sample data (log scales require positive values)
# x = np.linspace(1, 10, 100)
# take x from 10 to 100_00_00_000 to see the effect of log scale better
x = np.linspace(10, 100_00_00_000, 100)
y = np.sqrt(x)  # some function of x

# Create the plot
plt.plot(x, y)

# Set the y-axis to a logarithmic scale
plt.xscale('log')

# Add labels and show the plot
plt.xlabel('X-axis (Logarithmic Scale)')
plt.ylabel('Y-axis')
plt.title('Plot with Logarithmic X-axis')
# save plot as png file
plt.savefig('log_scale_plot.png')
plt.show()