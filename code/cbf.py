import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

k = 1.0
h0 = 20
t = np.linspace(0, 6, 500)  # Adjusted time range for better visualization

def y(t, h0, k):
    return h0 * np.exp(-k * t)

y_t = y(t, h0, k)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 6))

# Initialize the plot elements: a line and a point
line, = ax.plot([], [], color='blue', linewidth=2, label=r'$y(t) = y(0) e^{-kt}$')
point, = ax.plot([], [], 'ro')  # Point to highlight the current y(t)
time_template = 'Time = %.1f s'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes, fontsize=12)

# Set up the plot limits and labels
ax.set_xlim(0, 6)
ax.set_ylim(-0.1, h0 + 1)
ax.set_title('Exponential Decay: $y(t) = y(0) e^{-kt}$', fontsize=14)
ax.set_xlabel('Time', fontsize=12)
ax.set_ylabel('Value', fontsize=12)
ax.axhline(0, color='grey', linewidth=1, linestyle='--')
ax.axhline(h0, color='grey', linewidth=1, linestyle='--')
ax.grid(True)
ax.legend()

# Initialization function: plot background for each frame
def init():
    line.set_data([], [])
    point.set_data([], [])
    time_text.set_text('')
    return line, point, time_text

# Animation function: this is called sequentially
def animate(i):
    if i == 0:
        return init()
    # Create the data to plot
    this_time = t[:i]
    this_y = y_t[:i]
    # Update the line and the point
    line.set_data(this_time, this_y)
    point.set_data([this_time[-1]], [this_y[-1]])  # Wrap in lists to ensure sequences
    # Update the time text
    time_text.set_text(time_template % this_time[-1])
    return line, point, time_text

# Create an animation
ani = animation.FuncAnimation(fig, animate, frames=len(t), init_func=init, interval=50, blit=True)

# Save the animation as a GIF
ani.save('exponential_decay.gif', writer='pillow', fps=20)

# Show the animation
plt.show()